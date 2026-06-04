import { defineStore } from 'pinia'

export interface School {
  id: number
  name: string
  code: string
  address?: string
}

interface PaginatedResponse {
  count: number
  next: string | null
  previous: string | null
  results: School[]
}

export const useSchoolStore = defineStore('schools', {
  state: () => ({
    schools: [] as School[],
    isLoading: false,
  }),

  actions: {
    async fetchSchools() {
      const config = useRuntimeConfig()
      try {
        const response = await $fetch<PaginatedResponse | School[]>(`${config.public.apiBase}/schools/`)
        this.schools = Array.isArray(response) ? response : response.results || []
      } catch (error) {
        console.error('Error fetching schools:', error)
        this.schools = []
      }
    },
  },
})