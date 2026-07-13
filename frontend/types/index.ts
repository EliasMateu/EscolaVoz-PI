export interface User {
  id: string
  email: string | null
  cpf: string | null
  first_name: string
  last_name: string
  role: 'EMPLOYEE' | 'PRINCIPAL' | 'DIRECTORY' | 'SEDUC'
  school: string | null
  school_name?: string | null
  is_active: boolean
  date_joined: string
}

export interface AuthResponse {
  user: User
  refresh: string
  access: string
}

export interface LoginData {
  email: string
  password: string
}

export interface RegisterData {
  email?: string
  cpf: string
  first_name: string
  last_name: string
  password: string
  password_confirm: string
  school_code: string
}

export interface Category {
  id: string
  name: string
  description: string
  is_active: boolean
}

export interface Demand {
  id: string
  title: string
  description: string
  category: string
  category_name: string
  school: string
  school_name: string
  created_by: string
  created_by_name: string
  status: 'PENDING' | 'IN_PROGRESS' | 'COMPLETED' | 'REJECTED'
  priority: 'LOW' | 'MEDIUM' | 'HIGH' | 'URGENT'
  image: string | null
  image_url: string | null
  created_at: string
  updated_at: string
  resolved_at: string | null
}

export interface CreateDemandData {
  title: string
  description: string
  category: string
  priority: 'LOW' | 'MEDIUM' | 'HIGH' | 'URGENT'
  school?: string
  image?: File | null
}