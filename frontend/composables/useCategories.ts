import { defineStore } from 'pinia'

export interface Category {
  id: number
  name: string
  description?: string
  is_active: boolean
}

export const useCategoryStore = defineStore('categories', {
  state: () => ({
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

    async createCategory(data: { name: string; description?: string }) {
      const config = useRuntimeConfig()
      const auth = useAuthStore()
      
      this.isLoading = true
      try {
        const response = await $fetch<Category>(`${config.public.apiBase}/categories/`, {
          method: 'POST',
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
          body: data,
        })
        this.categories.push(response)
        return { success: true }
      } catch (error: any) {
        return { 
          success: false, 
          error: error.data?.detail || 'Erro ao criar categoria' 
        }
      } finally {
        this.isLoading = false
      }
    },

    async updateCategory(id: number, data: { name: string; description?: string }) {
      const config = useRuntimeConfig()
      const auth = useAuthStore()
      
      this.isLoading = true
      try {
        const response = await $fetch<Category>(`${config.public.apiBase}/categories/${id}/`, {
          method: 'PATCH',
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
          body: data,
        })
        const index = this.categories.findIndex(c => c.id === id)
        if (index !== -1) {
          this.categories[index] = response
        }
        return { success: true }
      } catch (error: any) {
        return { 
          success: false, 
          error: error.data?.detail || 'Erro ao atualizar categoria' 
        }
      } finally {
        this.isLoading = false
      }
    },

    async deleteCategory(id: number) {
      const config = useRuntimeConfig()
      const auth = useAuthStore()
      
      this.isLoading = true
      try {
        await $fetch(`${config.public.apiBase}/categories/${id}/`, {
          method: 'DELETE',
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
        })
        this.categories = this.categories.filter(c => c.id !== id)
        return { success: true }
      } catch (error: any) {
        return { 
          success: false, 
          error: error.data?.detail || 'Erro ao excluir categoria' 
        }
      } finally {
        this.isLoading = false
      }
    },
  },
})