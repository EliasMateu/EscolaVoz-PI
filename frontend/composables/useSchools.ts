import { defineStore } from 'pinia'

export interface School {
  id: number
  name: string
  code: string
  address?: string
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
        const response = await $fetch<School[]>(`${config.public.apiBase}/schools/`)
        this.schools = response
      } catch (error) {
        console.error('Error fetching schools:', error)
      }
    },
  },
})