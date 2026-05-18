import os
import base64
from abc import ABC, abstractmethod
from typing import Optional
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import UploadedFile


class BaseStorage(ABC):
    """Abstract base class for storage backends"""
    
    @abstractmethod
    def save(self, file: UploadedFile, path: str) -> str:
        """Save a file and return the saved path/URL"""
        pass
    
    @abstractmethod
    def delete(self, path: str) -> bool:
        """Delete a file, return True if successful"""
        pass
    
    @abstractmethod
    def get_url(self, path: str) -> str:
        """Get the full URL for a file"""
        pass
    
    @abstractmethod
    def exists(self, path: str) -> bool:
        """Check if a file exists"""
        pass


class LocalStorage(BaseStorage):
    """Local filesystem storage"""
    
    def __init__(self, base_url: str = None):
        self.base_url = base_url or os.environ.get('MEDIA_URL', '/media/')
        self.root = os.environ.get('MEDIA_ROOT', '/app/media')
    
    def save(self, file: UploadedFile, path: str) -> str:
        full_path = os.path.join(self.root, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        with open(full_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        return path
    
    def delete(self, path: str) -> bool:
        full_path = os.path.join(self.root, path)
        try:
            if os.path.exists(full_path):
                os.remove(full_path)
                return True
        except Exception:
            pass
        return False
    
    def get_url(self, path: str) -> str:
        return f"{self.base_url}{path}"
    
    def exists(self, path: str) -> bool:
        full_path = os.path.join(self.root, path)
        return os.path.exists(full_path)


class DatabaseStorage(BaseStorage):
    """Store images as base64 in database"""
    
    def save(self, file: UploadedFile, path: str) -> str:
        # Read file and convert to base64
        file_content = file.read()
        base64_content = base64.b64encode(file_content).decode('utf-8')
        
        # Get file extension
        ext = os.path.splitext(file.name)[1].lower()
        
        # Create a data URL
        mime_type = self._get_mime_type(ext)
        data_url = f"data:{mime_type};base64,{base64_content}"
        
        # Store in custom model (you need to create this)
        from demands.models import DemandAttachment
        attachment = DemandAttachment.objects.create(
            file_name=file.name,
            file_data=data_url,
            content_type=mime_type,
            file_size=len(file_content)
        )
        
        return str(attachment.id)
    
    def delete(self, path: str) -> bool:
        try:
            from demands.models import DemandAttachment
            attachment = DemandAttachment.objects.get(id=path)
            attachment.delete()
            return True
        except Exception:
            return False
    
    def get_url(self, path: str) -> str:
        # For database storage, we return the data URL directly
        # The view will handle serving it
        return f"/api/demands/attachments/{path}/"
    
    def exists(self, path: str) -> bool:
        try:
            from demands.models import DemandAttachment
            return DemandAttachment.objects.filter(id=path).exists()
        except Exception:
            return False
    
    def _get_mime_type(self, ext: str) -> str:
        mime_types = {
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.webp': 'image/webp',
            '.svg': 'image/svg+xml',
            '.bmp': 'image/bmp',
        }
        return mime_types.get(ext, 'application/octet-stream')


class S3Storage(BaseStorage):
    """AWS S3 storage"""
    
    def __init__(self):
        self.bucket_name = os.environ.get('AWS_S3_BUCKET_NAME', '')
        self.region = os.environ.get('AWS_S3_REGION', 'us-east-1')
        self.custom_domain = os.environ.get('AWS_S3_CUSTOM_DOMAIN', '')
        self.endpoint_url = os.environ.get('AWS_S3_ENDPOINT_URL', '')
        
        try:
            import boto3
            self.client = boto3.client(
                's3',
                region_name=self.region,
                endpoint_url=self.endpoint_url if self.endpoint_url else None,
                aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            )
        except ImportError:
            self.client = None
    
    def save(self, file: UploadedFile, path: str) -> str:
        if not self.client:
            raise Exception("boto3 not installed")
        
        self.client.upload_fileobj(
            file,
            self.bucket_name,
            path,
            ExtraArgs={
                'ContentType': file.content_type
            }
        )
        
        return path
    
    def delete(self, path: str) -> bool:
        if not self.client:
            return False
        
        try:
            self.client.delete_object(Bucket=self.bucket_name, Key=path)
            return True
        except Exception:
            return False
    
    def get_url(self, path: str) -> str:
        if self.custom_domain:
            return f"https://{self.custom_domain}/{path}"
        return f"https://{self.bucket_name}.s3.{self.region}.amazonaws.com/{path}"
    
    def exists(self, path: str) -> bool:
        if not self.client:
            return False
        
        try:
            self.client.head_object(Bucket=self.bucket_name, Key=path)
            return True
        except Exception:
            return False


class AzureBlobStorage(BaseStorage):
    """Azure Blob Storage"""
    
    def __init__(self):
        self.connection_string = os.environ.get('AZURE_STORAGE_CONNECTION_STRING', '')
        self.container_name = os.environ.get('AZURE_STORAGE_CONTAINER_NAME', 'demands')
        
        try:
            from azure.storage.blob import BlobServiceClient
            self.service = BlobServiceClient.from_connection_string(self.connection_string)
            self.client = self.service.get_container_client(self.container_name)
        except ImportError:
            self.service = None
            self.client = None
    
    def save(self, file: UploadedFile, path: str) -> str:
        if not self.client:
            raise Exception("azure-storage-blob not installed")
        
        blob = self.client.get_blob_client(path)
        blob.upload_blob(file, overwrite=True)
        
        return path
    
    def delete(self, path: str) -> bool:
        if not self.client:
            return False
        
        try:
            self.client.delete_blob(path)
            return True
        except Exception:
            return False
    
    def get_url(self, path: str) -> str:
        if self.service:
            return f"{self.service.primary_endpoint}/{path}"
        return f"/api/demands/azure-blobs/{path}/"
    
    def exists(self, path: str) -> bool:
        if not self.client:
            return False
        
        try:
            self.client.get_blob_client(path).get_blob_properties()
            return True
        except Exception:
            return False


def get_storage():
    """Factory function to get the appropriate storage backend"""
    storage_type = os.environ.get('STORAGE_TYPE', 'local').lower()
    
    if storage_type == 's3':
        return S3Storage()
    elif storage_type == 'azure':
        return AzureBlobStorage()
    elif storage_type == 'database':
        return DatabaseStorage()
    else:
        return LocalStorage()