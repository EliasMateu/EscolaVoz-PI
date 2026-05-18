<template>
  <div>
    <div class="mb-6">
          </NuxtLink>
          <NuxtLink 
            to="/admin" 
            class="inline-flex items-center px-3 py-1.5 text-sm font-medium text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white bg-gray-100 dark:bg-gray-700 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors"
          >
            <svg class="w-4 h-4 mr-1.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            Estatísticas
          </NuxtLink>
        </div>
      </div>
    </header>

    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="px-4 sm:px-0 mb-6">
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-4">
          <h3 class="text-sm font-medium text-gray-700 dark:text-gray-300 mb-3">Filtros</h3>
          <KanbanFilters 
            :schools="schools" 
            :categories="categories"
            @update:filters="handleFilterChange"
          />
        </div>

        <div class="mt-4 flex items-center justify-between">
          <p class="text-sm text-gray-500 dark:text-gray-400">
            Total de demandas: <span class="font-medium text-gray-900 dark:text-white">{{ filteredDemands.length }}</span>
          </p>
        </div>
      </div>

      <div v-if="isLoading" class="flex items-center justify-center py-12">
        <svg class="animate-spin h-8 w-8 text-primary-600" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
        </svg>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-4 gap-6 px-4 sm:px-0">
        <div class="bg-gray-100 dark:bg-gray-800/50 rounded-xl p-4 border border-gray-200 dark:border-gray-700">
          <div class="flex items-center justify-between mb-4">
            <h3 class="font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
              <span class="w-3 h-3 bg-yellow-500 rounded-full animate-pulse"></span>
              Pendente
            </h3>
            <span class="text-sm font-medium text-gray-900 dark:text-white bg-white dark:bg-gray-700 px-2 py-0.5 rounded-full">
              {{ pendingDemands.length }}
            </span>
          </div>
          <div class="space-y-3 overflow-y-auto max-h-[75vh] pr-1">
            <div 
              v-for="demand in pendingDemands" 
              :key="demand.id"
              class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm border border-gray-100 dark:border-gray-600 cursor-pointer hover:shadow-md hover:border-primary-300 dark:hover:border-primary-600 transition-all duration-200 group"
              @click="openDetail(demand)"
            >
              <div class="flex justify-between items-start mb-2">
                <span class="text-sm font-semibold text-gray-900 dark:text-white group-hover:text-primary-600 dark:group-hover:text-primary-400 line-clamp-1">
                  {{ demand.title }}
                </span>
              </div>
              <p class="text-xs text-gray-500 dark:text-gray-400 mb-3 line-clamp-2 min-h-[2rem]">
                {{ demand.description || 'Sem descrição' }}
              </p>
              <div class="flex items-center justify-between text-xs">
                <span :class="priorityClass(demand.priority)" class="px-2 py-0.5 rounded-full font-medium">
                  {{ priorityLabel(demand.priority) }}
                </span>
                <span class="text-gray-400">{{ formatDate(demand.created_at) }}</span>
              </div>
              <div v-if="demand.school_name" class="mt-2 pt-2 border-t border-gray-100 dark:border-gray-600">
                <span class="text-xs text-gray-400 flex items-center gap-1">
                  <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                  </svg>
                  {{ demand.school_name }}
                </span>
              </div>
            </div>
            <div v-if="pendingDemands.length === 0" class="text-center py-8 text-gray-400 text-sm flex flex-col items-center">
              <svg class="w-12 h-12 mb-2 opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
              </svg>
              Nenhuma demanda
            </div>
          </div>
        </div>

        <div class="bg-gray-100 dark:bg-gray-800/50 rounded-xl p-4 border border-gray-200 dark:border-gray-700">
          <div class="flex items-center justify-between mb-4">
            <h3 class="font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
              <span class="w-3 h-3 bg-blue-500 rounded-full"></span>
              Em Andamento
            </h3>
            <span class="text-sm font-medium text-gray-900 dark:text-white bg-white dark:bg-gray-700 px-2 py-0.5 rounded-full">
              {{ inProgressDemands.length }}
            </span>
          </div>
          <div class="space-y-3 overflow-y-auto max-h-[75vh] pr-1">
            <div 
              v-for="demand in inProgressDemands" 
              :key="demand.id"
              class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm border border-gray-100 dark:border-gray-600 cursor-pointer hover:shadow-md hover:border-primary-300 dark:hover:border-primary-600 transition-all duration-200 group"
              @click="openDetail(demand)"
            >
              <div class="flex justify-between items-start mb-2">
                <span class="text-sm font-semibold text-gray-900 dark:text-white group-hover:text-primary-600 dark:group-hover:text-primary-400 line-clamp-1">
                  {{ demand.title }}
                </span>
              </div>
              <p class="text-xs text-gray-500 dark:text-gray-400 mb-3 line-clamp-2 min-h-[2rem]">
                {{ demand.description || 'Sem descrição' }}
              </p>
              <div class="flex items-center justify-between text-xs">
                <span :class="priorityClass(demand.priority)" class="px-2 py-0.5 rounded-full font-medium">
                  {{ priorityLabel(demand.priority) }}
                </span>
                <span class="text-gray-400">{{ formatDate(demand.created_at) }}</span>
              </div>
              <div v-if="demand.school_name" class="mt-2 pt-2 border-t border-gray-100 dark:border-gray-600">
                <span class="text-xs text-gray-400 flex items-center gap-1">
                  <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                  </svg>
                  {{ demand.school_name }}
                </span>
              </div>
            </div>
            <div v-if="inProgressDemands.length === 0" class="text-center py-8 text-gray-400 text-sm flex flex-col items-center">
              <svg class="w-12 h-12 mb-2 opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              Nenhuma demanda
            </div>
          </div>
        </div>

        <div class="bg-gray-100 dark:bg-gray-800/50 rounded-xl p-4 border border-gray-200 dark:border-gray-700">
          <div class="flex items-center justify-between mb-4">
            <h3 class="font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
              <span class="w-3 h-3 bg-green-500 rounded-full"></span>
              Concluída
            </h3>
            <span class="text-sm font-medium text-gray-900 dark:text-white bg-white dark:bg-gray-700 px-2 py-0.5 rounded-full">
              {{ completedDemands.length }}
            </span>
          </div>
          <div class="space-y-3 overflow-y-auto max-h-[75vh] pr-1">
            <div 
              v-for="demand in completedDemands" 
              :key="demand.id"
              class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm border border-gray-100 dark:border-gray-600 cursor-pointer hover:shadow-md hover:border-primary-300 dark:hover:border-primary-600 transition-all duration-200 group"
              @click="openDetail(demand)"
            >
              <div class="flex justify-between items-start mb-2">
                <span class="text-sm font-semibold text-gray-900 dark:text-white group-hover:text-primary-600 dark:group-hover:text-primary-400 line-clamp-1">
                  {{ demand.title }}
                </span>
              </div>
              <p class="text-xs text-gray-500 dark:text-gray-400 mb-3 line-clamp-2 min-h-[2rem]">
                {{ demand.description || 'Sem descrição' }}
              </p>
              <div class="flex items-center justify-between text-xs">
                <span :class="priorityClass(demand.priority)" class="px-2 py-0.5 rounded-full font-medium">
                  {{ priorityLabel(demand.priority) }}
                </span>
                <span class="text-gray-400">{{ formatDate(demand.created_at) }}</span>
              </div>
              <div v-if="demand.school_name" class="mt-2 pt-2 border-t border-gray-100 dark:border-gray-600">
                <span class="text-xs text-gray-400 flex items-center gap-1">
                  <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                  </svg>
                  {{ demand.school_name }}
                </span>
              </div>
            </div>
            <div v-if="completedDemands.length === 0" class="text-center py-8 text-gray-400 text-sm flex flex-col items-center">
              <svg class="w-12 h-12 mb-2 opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              Nenhuma demanda
            </div>
          </div>
        </div>

        <div class="bg-gray-100 dark:bg-gray-800/50 rounded-xl p-4 border border-gray-200 dark:border-gray-700">
          <div class="flex items-center justify-between mb-4">
            <h3 class="font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
              <span class="w-3 h-3 bg-red-500 rounded-full"></span>
              Rejeitada
            </h3>
            <span class="text-sm font-medium text-gray-900 dark:text-white bg-white dark:bg-gray-700 px-2 py-0.5 rounded-full">
              {{ rejectedDemands.length }}
            </span>
          </div>
          <div class="space-y-3 overflow-y-auto max-h-[75vh] pr-1">
            <div 
              v-for="demand in rejectedDemands" 
              :key="demand.id"
              class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm border border-gray-100 dark:border-gray-600 cursor-pointer hover:shadow-md hover:border-primary-300 dark:hover:border-primary-600 transition-all duration-200 group"
              @click="openDetail(demand)"
            >
              <div class="flex justify-between items-start mb-2">
                <span class="text-sm font-semibold text-gray-900 dark:text-white group-hover:text-primary-600 dark:group-hover:text-primary-400 line-clamp-1">
                  {{ demand.title }}
                </span>
              </div>
              <p class="text-xs text-gray-500 dark:text-gray-400 mb-3 line-clamp-2 min-h-[2rem]">
                {{ demand.description || 'Sem descrição' }}
              </p>
              <div class="flex items-center justify-between text-xs">
                <span :class="priorityClass(demand.priority)" class="px-2 py-0.5 rounded-full font-medium">
                  {{ priorityLabel(demand.priority) }}
                </span>
                <span class="text-gray-400">{{ formatDate(demand.created_at) }}</span>
              </div>
              <div v-if="demand.school_name" class="mt-2 pt-2 border-t border-gray-100 dark:border-gray-600">
                <span class="text-xs text-gray-400 flex items-center gap-1">
                  <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                  </svg>
                  {{ demand.school_name }}
                </span>
              </div>
            </div>
            <div v-if="rejectedDemands.length === 0" class="text-center py-8 text-gray-400 text-sm flex flex-col items-center">
              <svg class="w-12 h-12 mb-2 opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" />
              </svg>
              Nenhuma demanda
            </div>
          </div>
        </div>
      </div>
    </main>

    <div v-if="selectedDemand" class="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-4" @click.self="selectedDemand = null">
      <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-2xl w-full max-w-lg overflow-hidden">
        <div class="bg-gradient-to-r from-primary-600 to-primary-700 px-6 py-4">
          <div class="flex justify-between items-center">
            <h3 class="text-xl font-bold text-white">{{ selectedDemand.title }}</h3>
            <button @click="selectedDemand = null" class="text-white/80 hover:text-white transition-colors">
              <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>
        
        <div class="p-6 space-y-4">
          <div class="flex flex-wrap gap-3">
            <div class="flex items-center gap-2">
              <span class="text-sm text-gray-500 dark:text-gray-400">Status:</span>
              <span :class="statusClass(selectedDemand.status)" class="text-xs px-3 py-1 rounded-full font-medium">
                {{ statusLabel(selectedDemand.status) }}
              </span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-sm text-gray-500 dark:text-gray-400">Prioridade:</span>
              <span :class="priorityClass(selectedDemand.priority)" class="text-xs px-3 py-1 rounded-full font-medium">
                {{ priorityLabel(selectedDemand.priority) }}
              </span>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <p class="text-xs text-gray-400 dark:text-gray-500 mb-1">Categoria</p>
              <p class="text-sm font-medium text-gray-900 dark:text-white">{{ selectedDemand.category_name }}</p>
            </div>
            <div>
              <p class="text-xs text-gray-400 dark:text-gray-500 mb-1">Escola</p>
              <p class="text-sm font-medium text-gray-900 dark:text-white">{{ selectedDemand.school_name || 'N/A' }}</p>
            </div>
            <div>
              <p class="text-xs text-gray-400 dark:text-gray-500 mb-1">Criado em</p>
              <p class="text-sm font-medium text-gray-900 dark:text-white">{{ formatDate(selectedDemand.created_at) }}</p>
            </div>
            <div v-if="selectedDemand.resolved_at">
              <p class="text-xs text-gray-400 dark:text-gray-500 mb-1">Concluído em</p>
              <p class="text-sm font-medium text-gray-900 dark:text-white">{{ formatDate(selectedDemand.resolved_at) }}</p>
            </div>
          </div>

          <div v-if="selectedDemand.description">
            <p class="text-xs text-gray-400 dark:text-gray-500 mb-2">Descrição</p>
            <p class="text-sm text-gray-700 dark:text-gray-300 bg-gray-50 dark:bg-gray-700/50 rounded-lg p-3">
              {{ selectedDemand.description }}
            </p>
          </div>
        </div>
      </template>

<script setup lang="ts">
import { useThemeStore, translations } from '~/composables/useTheme'
import type { Demand } from '~/composables/useDemands'
import type { School } from '~/composables/useSchools'
import type { Category } from '~/composables/useCategories'

definePageMeta({
  layout: 'dashboard'
})

const demandStore = useDemandStore()
const schoolStore = useSchoolStore()
const categoryStore = useCategoryStore()
const auth = useAuthStore()
const store = useThemeStore()

const t = (key: string) => translations[store.locale][key as keyof typeof translations['pt-BR']] || key

const isLoading = computed(() => demandStore.isLoading)
const selectedDemand = ref<Demand | null>(null)
const filters = reactive({
  school: '',
  priority: '',
  category: '',
  date_from: '',
  date_to: '',
})

const schools = computed(() => schoolStore.schools)
const categories = computed(() => categoryStore.categories)

const allDemands = computed(() => demandStore.demands)

const filteredDemands = computed(() => {
  return allDemands.value.filter(d => {
    if (filters.school && d.school_code !== filters.school) return false
    if (filters.priority && d.priority !== filters.priority) return false
    if (filters.category && d.category !== parseInt(filters.category)) return false
    if (filters.date_from) {
      const demandDate = new Date(d.created_at)
      const fromDate = new Date(filters.date_from)
      if (demandDate < fromDate) return false
    }
    if (filters.date_to) {
      const demandDate = new Date(d.created_at)
      const toDate = new Date(filters.date_to)
      toDate.setHours(23, 59, 59)
      if (demandDate > toDate) return false
    }
    return true
  })
})

const pendingDemands = computed(() => filteredDemands.value.filter(d => d.status === 'PENDING'))
const inProgressDemands = computed(() => filteredDemands.value.filter(d => d.status === 'IN_PROGRESS'))
const completedDemands = computed(() => filteredDemands.value.filter(d => d.status === 'COMPLETED'))
const rejectedDemands = computed(() => filteredDemands.value.filter(d => d.status === 'REJECTED'))

onMounted(() => {
  store.initTheme()
  if (auth.user?.role === 'SEDUC' || auth.user?.role === 'DIRECTORY') {
    demandStore.fetchDemands()
    schoolStore.fetchSchools()
    categoryStore.fetchCategories()
  } else {
    navigateTo('/dashboard')
  }
})

const handleFilterChange = (newFilters: typeof filters) => {
  Object.assign(filters, newFilters)
}

const openDetail = (demand: Demand) => {
  selectedDemand.value = demand
}

const formatDate = (date: string) => {
  return new Date(date).toLocaleDateString('pt-BR')
}

const priorityClass = (priority: string) => {
  const classes: Record<string, string> = {
    LOW: 'bg-gray-100 text-gray-600 dark:bg-gray-600 dark:text-gray-300',
    MEDIUM: 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900/30 dark:text-yellow-400',
    HIGH: 'bg-orange-100 text-orange-800 dark:bg-orange-900/30 dark:text-orange-400',
    URGENT: 'bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400',
  }
  return classes[priority] || classes.MEDIUM
}

const priorityLabel = (priority: string) => {
  const labels: Record<string, string> = {
    LOW: 'Baixa',
    MEDIUM: 'Média',
    HIGH: 'Alta',
    URGENT: 'Urgente',
  }
  return labels[priority] || priority
}

const statusClass = (status: string) => {
  const classes: Record<string, string> = {
    PENDING: 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900/30 dark:text-yellow-400',
    IN_PROGRESS: 'bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-400',
    COMPLETED: 'bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400',
    REJECTED: 'bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400',
  }
  return classes[status] || ''
}

const statusLabel = (status: string) => {
  const labels: Record<string, string> = {
    PENDING: 'Pendente',
    IN_PROGRESS: 'Em Andamento',
    COMPLETED: 'Concluída',
    REJECTED: 'Rejeitada',
  }
  return labels[status] || status
}
</script>