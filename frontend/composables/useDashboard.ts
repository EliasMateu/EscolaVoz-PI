import { defineStore } from 'pinia'

interface Stats {
  total: number
  pending: number
  in_progress: number
  completed: number
  rejected: number
}

interface CategoryData {
  category: string
  count: number
}

interface SchoolData {
  school: string
  count: number
}

export const useDashboardStore = defineStore('dashboard', {
  state: () => ({
    stats: null as Stats | null,
    byCategory: [] as CategoryData[],
    bySchool: [] as SchoolData[],
    isLoading: false,
  }),

  actions: {
    async fetchStats() {
      const config = useRuntimeConfig()
      const auth = useAuthStore()
      
      this.isLoading = true
      try {
        const response = await $fetch<Stats>(`${config.public.apiBase}/dashboard/stats/`, {
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
        })
        this.stats = response
      } catch (error) {
        console.error('Error fetching stats:', error)
      } finally {
        this.isLoading = false
      }
    },

    async fetchByCategory() {
      const config = useRuntimeConfig()
      const auth = useAuthStore()
      
      try {
        const response = await $fetch<Record<string, number>>(`${config.public.apiBase}/dashboard/by-category/`, {
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
        })
        this.byCategory = Object.entries(response).map(([category, count]) => ({ category, count }))
      } catch (error) {
        console.error('Error fetching by category:', error)
      }
    },

    async fetchBySchool() {
      const config = useRuntimeConfig()
      const auth = useAuthStore()
      
      try {
        const response = await $fetch<Record<string, number>>(`${config.public.apiBase}/dashboard/by-school/`, {
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
        })
        this.bySchool = Object.entries(response).map(([school, count]) => ({ school, count }))
      } catch (error) {
        console.error('Error fetching by school:', error)
      }
    },

    async exportCSV() {
      const config = useRuntimeConfig()
      const auth = useAuthStore()
      
      try {
        const response = await $fetch<string>(`${config.public.apiBase}/dashboard/export/`, {
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
          responseType: 'blob',
        })
        
        const url = window.URL.createObjectURL(response as any)
        const a = document.createElement('a')
        a.href = url
        a.download = 'demandas.csv'
        a.click()
        window.URL.revokeObjectURL(url)
      } catch (error) {
        console.error('Error exporting CSV:', error)
      }
    },
  },
})