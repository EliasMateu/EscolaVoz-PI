import { defineStore } from 'pinia'
import type { User, AuthResponse, LoginData, RegisterData } from '~/types'

const api = useRuntimeConfig().public.apiBase

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as User | null,
    accessToken: null as string | null,
    refreshToken: null as string | null,
    isLoading: false,
  }),

  getters: {
    isAuthenticated: (state) => !!state.accessToken && !!state.user,
    userRole: (state) => state.user?.role || null,
    userSchool: (state) => state.user?.school || null,
  },

  actions: {
    async login(credentials: LoginData) {
      this.isLoading = true
      try {
        const response = await $fetch<AuthResponse>(`${api}/auth/login/`, {
          method: 'POST',
          body: credentials,
        })

        this.user = response.user
        this.accessToken = response.access
        this.refreshToken = response.refresh

        localStorage.setItem('accessToken', response.access)
        localStorage.setItem('refreshToken', response.refresh)

        return { success: true }
      } catch (error: any) {
        return { 
          success: false, 
          error: error.data?.error || 'Erro ao fazer login' 
        }
      } finally {
        this.isLoading = false
      }
    },

    async register(data: RegisterData) {
      this.isLoading = true
      try {
        const response = await $fetch<AuthResponse>(`${api}/auth/register/`, {
          method: 'POST',
          body: data,
        })

        this.user = response.user
        this.accessToken = response.access
        this.refreshToken = response.refresh

        localStorage.setItem('accessToken', response.access)
        localStorage.setItem('refreshToken', response.refresh)

        return { success: true }
      } catch (error: any) {
        const errors = error.data || {}
        const firstError = Object.values(errors)[0]
        return { 
          success: false, 
          error: Array.isArray(firstError) ? firstError[0] : 'Erro ao criar conta' 
        }
      } finally {
        this.isLoading = false
      }
    },

    async refreshAccessToken() {
      if (!this.refreshToken) return false

      try {
        const response = await $fetch<{ access: string }>(`${api}/auth/refresh/`, {
          method: 'POST',
          body: { refresh: this.refreshToken },
        })

        this.accessToken = response.access
        localStorage.setItem('accessToken', response.access)
        return true
      } catch {
        this.logout()
        return false
      }
    },

    async fetchUser() {
      if (!this.accessToken) return

      try {
        const response = await $fetch<User>(`${api}/auth/me/`, {
          headers: {
            Authorization: `Bearer ${this.accessToken}`,
          },
        })
        this.user = response
      } catch {
        const refreshed = await this.refreshAccessToken()
        if (refreshed) {
          await this.fetchUser()
        }
      }
    },

    logout() {
      this.user = null
      this.accessToken = null
      this.refreshToken = null
      localStorage.removeItem('accessToken')
      localStorage.removeItem('refreshToken')
      navigateTo('/login')
    },

    initAuth() {
      const accessToken = localStorage.getItem('accessToken')
      const refreshToken = localStorage.getItem('refreshToken')

      if (accessToken && refreshToken) {
        this.accessToken = accessToken
        this.refreshToken = refreshToken
        this.fetchUser()
      }
    },
  },
})