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