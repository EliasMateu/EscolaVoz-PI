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
        const response = await $fetch<Category[]>(`${config.public.apiBase}/categories/`)
        this.categories = response
      } catch (error) {
        console.error('Error fetching categories:', error)
      }
    },

    async fetchDemands() {
      const config = useRuntimeConfig()
      const auth = useAuthStore()
      
      this.isLoading = true
      try {
        const response = await $fetch<{ results: Demand[] }>(`${config.public.apiBase}/demands/`, {
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
        })
        this.demands = response.results || response
      } catch (error) {
        console.error('Error fetching demands:', error)
      } finally {
        this.isLoading = false
      }
    },

    async createDemand(data: CreateDemandData) {
      const config = useRuntimeConfig()
      const auth = useAuthStore()
      
      this.isLoading = true
      try {
        const response = await $fetch<Demand>(`${config.public.apiBase}/demands/`, {
          method: 'POST',
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
          body: data,
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
  },
})