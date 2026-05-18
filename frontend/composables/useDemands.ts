import { defineStore } from 'pinia'
import type { Demand, Category, CreateDemandData } from '~/types'

export const useDemandStore = defineStore('demands', {
  state: () => ({
    demands: [] as Demand[],
    categories: [] as Category[],
    isLoading: false,
  }),

  actions: {
    async fetchCategories() {
      const config = useRuntimeConfig()
      try {
        const response = await $fetch<{ count: number; results: Category[] } | Category[]>(`${config.public.apiBase}/categories/`)
        this.categories = Array.isArray(response) ? response : response.results || []
      } catch (error) {
        console.error('Error fetching categories:', error)
        this.categories = []
      }
    },

    async fetchDemands() {
      const config = useRuntimeConfig()
      const auth = useAuthStore()
      
      this.isLoading = true
      try {
        const response = await $fetch<{ count: number; results: Demand[] } | Demand[]>(`${config.public.apiBase}/demands/`, {
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
        })
        this.demands = Array.isArray(response) ? response : response.results || []
      } catch (error) {
        console.error('Error fetching demands:', error)
        this.demands = []
      } finally {
        this.isLoading = false
      }
    },

    async createDemand(data: CreateDemandData) {
      const config = useRuntimeConfig()
      const auth = useAuthStore()
      
      this.isLoading = true
      try {
        const formData = new FormData()
        formData.append('title', data.title)
        formData.append('description', data.description)
        formData.append('category', data.category)
        formData.append('priority', data.priority)
        if (data.image) {
          formData.append('image', data.image)
        }

        const response = await $fetch<Demand>(`${config.public.apiBase}/demands/`, {
          method: 'POST',
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
          body: formData,
        })
        this.demands.unshift(response)
        return { success: true }
      } catch (error: any) {
        return { 
          success: false, 
          error: error.data?.detail || 'Erro ao criar demanda' 
        }
      } finally {
        this.isLoading = false
      }
    },

    async fetchDemand(id: string): Promise<Demand | null> {
      const config = useRuntimeConfig()
      const auth = useAuthStore()
      
      this.isLoading = true
      try {
        const response = await $fetch<Demand>(`${config.public.apiBase}/demands/${id}/`, {
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
        })
        return response
      } catch (error) {
        console.error('Error fetching demand:', error)
        return null
      } finally {
        this.isLoading = false
      }
    },

    async updateDemand(id: string, data: Partial<CreateDemandData & { status?: string; priority?: string; removeImage?: boolean }>) {
      const config = useRuntimeConfig()
      const auth = useAuthStore()
      
      this.isLoading = true
      try {
        let body: any = data
        
        if (data.image !== undefined) {
          const formData = new FormData()
          if (data.title) formData.append('title', data.title)
          if (data.description !== undefined) formData.append('description', data.description)
          if (data.category) formData.append('category', data.category)
          if (data.status) formData.append('status', data.status)
          if (data.priority) formData.append('priority', data.priority)
          if (data.image) {
            formData.append('image', data.image)
          }
          if (data.removeImage) {
            formData.append('image', '')
          }
          body = formData
        }

        const response = await $fetch<Demand>(`${config.public.apiBase}/demands/${id}/`, {
          method: 'PATCH',
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
          body,
        })
        const index = this.demands.findIndex(d => d.id === id)
        if (index !== -1) {
          this.demands[index] = response
        }
        return { success: true, data: response }
      } catch (error: any) {
        return { 
          success: false, 
          error: error.data?.detail || 'Erro ao atualizar demanda' 
        }
      } finally {
        this.isLoading = false
      }
    },
  },
})