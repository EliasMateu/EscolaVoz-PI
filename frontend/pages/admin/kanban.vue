<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors">
    <header class="bg-white dark:bg-gray-800 shadow">
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
        <h1 class="text-3xl font-bold text-gray-900 dark:text-white">Kanban - Demandas</h1>
        <div class="flex items-center space-x-4">
          <LocaleToggle />
          <ThemeToggle />
          <NuxtLink to="/dashboard" class="text-gray-600 hover:text-gray-900 dark:text-gray-300 dark:hover:text-white">
            {{ t('dashboard') }}
          </NuxtLink>
          <NuxtLink to="/admin" class="text-gray-600 hover:text-gray-900 dark:text-gray-300 dark:hover:text-white">
            {{ t('back') }}
          </NuxtLink>
        </div>
      </div>
    </header>

    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="px-4 sm:px-0">
        <div v-if="isLoading" class="text-center py-12">
          <div class="text-gray-500 dark:text-gray-400">Carregando...</div>
        </div>

        <div v-else class="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div class="bg-gray-100 dark:bg-gray-800 rounded-lg p-4">
            <div class="flex items-center justify-between mb-4">
              <h3 class="font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
                <span class="w-3 h-3 bg-yellow-500 rounded-full"></span>
                {{ t('pending') }}
              </h3>
              <span class="text-sm text-gray-500 dark:text-gray-400">{{ pendingDemands.length }}</span>
            </div>
            <div class="space-y-3 overflow-y-auto max-h-[70vh]">
              <div 
                v-for="demand in pendingDemands" 
                :key="demand.id"
                class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm cursor-pointer hover:shadow-md transition-shadow"
                @click="openDetail(demand)"
              >
                <div class="flex justify-between items-start mb-2">
                  <span class="text-sm font-medium text-primary-600 dark:text-primary-400">{{ demand.title }}</span>
                  <span :class="priorityClass(demand.priority)" class="text-xs px-2 py-1 rounded-full">
                    {{ priorityLabel(demand.priority) }}
                  </span>
                </div>
                <p class="text-xs text-gray-500 dark:text-gray-400 mb-2 line-clamp-2">{{ demand.description }}</p>
                <div class="flex items-center justify-between text-xs text-gray-400">
                  <span>{{ demand.category_name }}</span>
                  <span>{{ formatDate(demand.created_at) }}</span>
                </div>
              </div>
              <div v-if="pendingDemands.length === 0" class="text-center py-8 text-gray-400 text-sm">
                Nenhuma demanda
              </div>
            </div>
          </div>

          <div class="bg-gray-100 dark:bg-gray-800 rounded-lg p-4">
            <div class="flex items-center justify-between mb-4">
              <h3 class="font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
                <span class="w-3 h-3 bg-blue-500 rounded-full"></span>
                {{ t('inProgress') }}
              </h3>
              <span class="text-sm text-gray-500 dark:text-gray-400">{{ inProgressDemands.length }}</span>
            </div>
            <div class="space-y-3 overflow-y-auto max-h-[70vh]">
              <div 
                v-for="demand in inProgressDemands" 
                :key="demand.id"
                class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm cursor-pointer hover:shadow-md transition-shadow"
                @click="openDetail(demand)"
              >
                <div class="flex justify-between items-start mb-2">
                  <span class="text-sm font-medium text-primary-600 dark:text-primary-400">{{ demand.title }}</span>
                  <span :class="priorityClass(demand.priority)" class="text-xs px-2 py-1 rounded-full">
                    {{ priorityLabel(demand.priority) }}
                  </span>
                </div>
                <p class="text-xs text-gray-500 dark:text-gray-400 mb-2 line-clamp-2">{{ demand.description }}</p>
                <div class="flex items-center justify-between text-xs text-gray-400">
                  <span>{{ demand.category_name }}</span>
                  <span>{{ formatDate(demand.created_at) }}</span>
                </div>
              </div>
              <div v-if="inProgressDemands.length === 0" class="text-center py-8 text-gray-400 text-sm">
                Nenhuma demanda
              </div>
            </div>
          </div>

          <div class="bg-gray-100 dark:bg-gray-800 rounded-lg p-4">
            <div class="flex items-center justify-between mb-4">
              <h3 class="font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
                <span class="w-3 h-3 bg-green-500 rounded-full"></span>
                {{ t('completed') }}
              </h3>
              <span class="text-sm text-gray-500 dark:text-gray-400">{{ completedDemands.length }}</span>
            </div>
            <div class="space-y-3 overflow-y-auto max-h-[70vh]">
              <div 
                v-for="demand in completedDemands" 
                :key="demand.id"
                class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm cursor-pointer hover:shadow-md transition-shadow"
                @click="openDetail(demand)"
              >
                <div class="flex justify-between items-start mb-2">
                  <span class="text-sm font-medium text-primary-600 dark:text-primary-400">{{ demand.title }}</span>
                  <span :class="priorityClass(demand.priority)" class="text-xs px-2 py-1 rounded-full">
                    {{ priorityLabel(demand.priority) }}
                  </span>
                </div>
                <p class="text-xs text-gray-500 dark:text-gray-400 mb-2 line-clamp-2">{{ demand.description }}</p>
                <div class="flex items-center justify-between text-xs text-gray-400">
                  <span>{{ demand.category_name }}</span>
                  <span>{{ formatDate(demand.created_at) }}</span>
                </div>
              </div>
              <div v-if="completedDemands.length === 0" class="text-center py-8 text-gray-400 text-sm">
                Nenhuma demanda
              </div>
            </div>
          </div>

          <div class="bg-gray-100 dark:bg-gray-800 rounded-lg p-4">
            <div class="flex items-center justify-between mb-4">
              <h3 class="font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
                <span class="w-3 h-3 bg-red-500 rounded-full"></span>
                Rejeitada
              </h3>
              <span class="text-sm text-gray-500 dark:text-gray-400">{{ rejectedDemands.length }}</span>
            </div>
            <div class="space-y-3 overflow-y-auto max-h-[70vh]">
              <div 
                v-for="demand in rejectedDemands" 
                :key="demand.id"
                class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm cursor-pointer hover:shadow-md transition-shadow"
                @click="openDetail(demand)"
              >
                <div class="flex justify-between items-start mb-2">
                  <span class="text-sm font-medium text-primary-600 dark:text-primary-400">{{ demand.title }}</span>
                  <span :class="priorityClass(demand.priority)" class="text-xs px-2 py-1 rounded-full">
                    {{ priorityLabel(demand.priority) }}
                  </span>
                </div>
                <p class="text-xs text-gray-500 dark:text-gray-400 mb-2 line-clamp-2">{{ demand.description }}</p>
                <div class="flex items-center justify-between text-xs text-gray-400">
                  <span>{{ demand.category_name }}</span>
                  <span>{{ formatDate(demand.created_at) }}</span>
                </div>
              </div>
              <div v-if="rejectedDemands.length === 0" class="text-center py-8 text-gray-400 text-sm">
                Nenhuma demanda
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <div v-if="selectedDemand" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50" @click.self="selectedDemand = null">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 w-full max-w-lg">
        <div class="flex justify-between items-start mb-4">
          <h3 class="text-lg font-semibold text-gray-900 dark:text-white">{{ selectedDemand.title }}</h3>
          <button @click="selectedDemand = null" class="text-gray-400 hover:text-gray-600">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="space-y-3">
          <div class="flex items-center gap-2">
            <span class="text-sm text-gray-500 dark:text-gray-400">Status:</span>
            <span :class="statusClass(selectedDemand.status)" class="text-xs px-2 py-1 rounded-full">
              {{ statusLabel(selectedDemand.status) }}
            </span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-sm text-gray-500 dark:text-gray-400">Prioridade:</span>
            <span :class="priorityClass(selectedDemand.priority)" class="text-xs px-2 py-1 rounded-full">
              {{ priorityLabel(selectedDemand.priority) }}
            </span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-sm text-gray-500 dark:text-gray-400">Categoria:</span>
            <span class="text-sm text-gray-900 dark:text-gray-300">{{ selectedDemand.category_name }}</span>
          </div>
          <div v-if="selectedDemand.school_name" class="flex items-center gap-2">
            <span class="text-sm text-gray-500 dark:text-gray-400">Escola:</span>
            <span class="text-sm text-gray-900 dark:text-gray-300">{{ selectedDemand.school_name }}</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-sm text-gray-500 dark:text-gray-400">Criado em:</span>
            <span class="text-sm text-gray-900 dark:text-gray-300">{{ formatDate(selectedDemand.created_at) }}</span>
          </div>
          <div>
            <span class="text-sm text-gray-500 dark:text-gray-400">Descrição:</span>
            <p class="text-sm text-gray-900 dark:text-gray-300 mt-1">{{ selectedDemand.description || 'Sem descrição' }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useThemeStore, translations } from '~/composables/useTheme'
import type { Demand } from '~/composables/useDemands'

definePageMeta({
  layout: false
})

const demandStore = useDemandStore()
const auth = useAuthStore()
const store = useThemeStore()

const t = (key: string) => translations[store.locale][key as keyof typeof translations['pt-BR']] || key

const isLoading = computed(() => demandStore.isLoading)
const selectedDemand = ref<Demand | null>(null)

const allDemands = computed(() => demandStore.demands)
const pendingDemands = computed(() => allDemands.value.filter(d => d.status === 'PENDING'))
const inProgressDemands = computed(() => allDemands.value.filter(d => d.status === 'IN_PROGRESS'))
const completedDemands = computed(() => allDemands.value.filter(d => d.status === 'COMPLETED'))
const rejectedDemands = computed(() => allDemands.value.filter(d => d.status === 'REJECTED'))

onMounted(() => {
  store.initTheme()
  if (auth.user?.role === 'SEDUC' || auth.user?.role === 'DIRECTORY') {
    demandStore.fetchDemands()
  } else {
    navigateTo('/dashboard')
  }
})

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