<template>
  <div>
    <div class="mb-4 sm:mb-6">
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-3 sm:p-4">
        <h3 class="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2 sm:mb-3">Filtros</h3>
        <KanbanFilters 
          :schools="schools" 
          :categories="categories"
          @update:filters="handleFilterChange"
        />
      </div>
      <div class="mt-3 sm:mt-4 flex items-center justify-between">
        <p class="text-xs sm:text-sm text-gray-500 dark:text-gray-400">
          Total: <span class="font-medium text-gray-900 dark:text-white">{{ filteredDemands.length }}</span>
        </p>
      </div>
    </div>

    <div v-if="isLoading" class="flex items-center justify-center py-12">
      <svg class="animate-spin h-8 w-8 text-primary-600" fill="none" viewBox="0 0 24 24">
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
      </svg>
    </div>

    <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4">
      <div
        class="bg-gray-100 dark:bg-gray-800/50 rounded-xl p-4 border border-gray-200 dark:border-gray-700"
        @dragover.prevent
        @dragenter.prevent
        @drop="handleDrop('PENDING')"
      >
        <div class="flex items-center justify-between mb-4">
          <h3 class="font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
            <span class="w-3 h-3 bg-yellow-500 rounded-full shrink-0"></span>
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
            class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm border border-gray-100 dark:border-gray-600 cursor-pointer hover:shadow-md transition-all duration-200"
            :class="{ 'opacity-50': draggedDemand?.id === demand.id }"
            draggable="true"
            @dragstart="handleDragStart(demand)"
            @dragend="handleDragEnd"
            @click="openDetail(demand)"
          >
            <div class="text-sm font-semibold text-gray-900 dark:text-white mb-1">{{ demand.title }}</div>
            <p class="text-xs text-gray-500 dark:text-gray-400 mb-2 line-clamp-2">{{ demand.description || 'Sem descrição' }}</p>
            <div class="flex items-center justify-between text-xs">
              <span :class="priorityClass(demand.priority)" class="px-2 py-0.5 rounded-full font-medium">{{ priorityLabel(demand.priority) }}</span>
              <span class="text-gray-400">{{ formatDate(demand.created_at) }}</span>
            </div>
          </div>
          <div v-if="pendingDemands.length === 0" class="text-center py-8 text-gray-400 text-sm">Nenhuma demanda</div>
        </div>
      </div>

      <div
        class="bg-gray-100 dark:bg-gray-800/50 rounded-xl p-4 border border-gray-200 dark:border-gray-700"
        @dragover.prevent
        @dragenter.prevent
        @drop="handleDrop('IN_PROGRESS')"
      >
        <div class="flex items-center justify-between mb-4">
          <h3 class="font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
            <span class="w-3 h-3 bg-blue-500 rounded-full shrink-0"></span>
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
            class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm border border-gray-100 dark:border-gray-600 cursor-pointer hover:shadow-md transition-all duration-200"
            :class="{ 'opacity-50': draggedDemand?.id === demand.id }"
            draggable="true"
            @dragstart="handleDragStart(demand)"
            @dragend="handleDragEnd"
            @click="openDetail(demand)"
          >
            <div class="text-sm font-semibold text-gray-900 dark:text-white mb-1">{{ demand.title }}</div>
            <p class="text-xs text-gray-500 dark:text-gray-400 mb-2 line-clamp-2">{{ demand.description || 'Sem descrição' }}</p>
            <div class="flex items-center justify-between text-xs">
              <span :class="priorityClass(demand.priority)" class="px-2 py-0.5 rounded-full font-medium">{{ priorityLabel(demand.priority) }}</span>
              <span class="text-gray-400">{{ formatDate(demand.created_at) }}</span>
            </div>
          </div>
          <div v-if="inProgressDemands.length === 0" class="text-center py-8 text-gray-400 text-sm">Nenhuma demanda</div>
        </div>
      </div>

      <div
        class="bg-gray-100 dark:bg-gray-800/50 rounded-xl p-4 border border-gray-200 dark:border-gray-700"
        @dragover.prevent
        @dragenter.prevent
        @drop="handleDrop('COMPLETED')"
      >
        <div class="flex items-center justify-between mb-4">
          <h3 class="font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
            <span class="w-3 h-3 bg-green-500 rounded-full shrink-0"></span>
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
            class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm border border-gray-100 dark:border-gray-600 cursor-pointer hover:shadow-md transition-all duration-200"
            :class="{ 'opacity-50': draggedDemand?.id === demand.id }"
            draggable="true"
            @dragstart="handleDragStart(demand)"
            @dragend="handleDragEnd"
            @click="openDetail(demand)"
          >
            <div class="text-sm font-semibold text-gray-900 dark:text-white mb-1">{{ demand.title }}</div>
            <p class="text-xs text-gray-500 dark:text-gray-400 mb-2 line-clamp-2">{{ demand.description || 'Sem descrição' }}</p>
            <div class="flex items-center justify-between text-xs">
              <span :class="priorityClass(demand.priority)" class="px-2 py-0.5 rounded-full font-medium">{{ priorityLabel(demand.priority) }}</span>
              <span class="text-gray-400">{{ formatDate(demand.created_at) }}</span>
            </div>
          </div>
          <div v-if="completedDemands.length === 0" class="text-center py-8 text-gray-400 text-sm">Nenhuma demanda</div>
        </div>
      </div>

      <div
        class="bg-gray-100 dark:bg-gray-800/50 rounded-xl p-4 border border-gray-200 dark:border-gray-700"
        @dragover.prevent
        @dragenter.prevent
        @drop="handleDrop('REJECTED')"
      >
        <div class="flex items-center justify-between mb-4">
          <h3 class="font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
            <span class="w-3 h-3 bg-red-500 rounded-full shrink-0"></span>
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
            class="bg-white dark:bg-gray-700 rounded-lg p-4 shadow-sm border border-gray-100 dark:border-gray-600 cursor-pointer hover:shadow-md transition-all duration-200"
            :class="{ 'opacity-50': draggedDemand?.id === demand.id }"
            draggable="true"
            @dragstart="handleDragStart(demand)"
            @dragend="handleDragEnd"
            @click="openDetail(demand)"
          >
            <div class="text-sm font-semibold text-gray-900 dark:text-white mb-1">{{ demand.title }}</div>
            <p class="text-xs text-gray-500 dark:text-gray-400 mb-2 line-clamp-2">{{ demand.description || 'Sem descrição' }}</p>
            <div class="flex items-center justify-between text-xs">
              <span :class="priorityClass(demand.priority)" class="px-2 py-0.5 rounded-full font-medium">{{ priorityLabel(demand.priority) }}</span>
              <span class="text-gray-400">{{ formatDate(demand.created_at) }}</span>
            </div>
          </div>
          <div v-if="rejectedDemands.length === 0" class="text-center py-8 text-gray-400 text-sm">Nenhuma demanda</div>
        </div>
      </div>
    </div>

    <div v-if="selectedDemand" class="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-3 sm:p-4" @click.self="selectedDemand = null">
      <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-2xl w-full max-w-lg max-h-[90vh] overflow-y-auto">
        <div class="bg-gradient-to-r from-primary-600 to-primary-700 px-6 py-4">
          <div class="flex justify-between items-center">
            <h3 class="text-xl font-bold text-white">{{ selectedDemand.title }}</h3>
            <button @click="selectedDemand = null" class="text-white/80 hover:text-white">
              <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>
        <div class="p-6 space-y-4">
          <div class="flex flex-wrap gap-3">
            <div class="flex items-center gap-2">
              <span class="text-sm text-gray-500">Status:</span>
              <span :class="statusClass(selectedDemand.status)" class="text-xs px-3 py-1 rounded-full font-medium">{{ statusLabel(selectedDemand.status) }}</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-sm text-gray-500">Prioridade:</span>
              <span :class="priorityClass(selectedDemand.priority)" class="text-xs px-3 py-1 rounded-full font-medium">{{ priorityLabel(selectedDemand.priority) }}</span>
            </div>
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <p class="text-xs text-gray-400 mb-1">Categoria</p>
              <p class="text-sm font-medium text-gray-900 dark:text-white">{{ selectedDemand.category_name }}</p>
            </div>
            <div>
              <p class="text-xs text-gray-400 mb-1">Escola</p>
              <p class="text-sm font-medium text-gray-900 dark:text-white">{{ selectedDemand.school_name || 'N/A' }}</p>
            </div>
          </div>
          <div v-if="selectedDemand.description">
            <p class="text-xs text-gray-400 mb-2">Descrição</p>
            <p class="text-sm text-gray-700 dark:text-gray-300 bg-gray-50 dark:bg-gray-700/50 rounded-lg p-3">{{ selectedDemand.description }}</p>
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
const filters = reactive({ school: '', priority: '', category: '', date_from: '', date_to: '' })

const schools = computed(() => {
  const data = schoolStore.schools
  if (!data) return []
  if (Array.isArray(data)) return data
  if (data?.results) return data.results
  return []
})

const categories = computed(() => {
  const data = categoryStore.categories
  if (!data) return []
  if (Array.isArray(data)) return data
  if (data?.results) return data.results
  return []
})
const allDemands = computed(() => demandStore.demands)

const filteredDemands = computed(() => {
  return allDemands.value.filter(d => {
    if (filters.school && d.school_code !== filters.school) return false
    if (filters.priority && d.priority !== filters.priority) return false
    if (filters.category && d.category !== parseInt(filters.category)) return false
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

const openDetail = (demand: Demand) => { navigateTo(`/demands/${demand.id}`) }

const draggedDemand = ref<Demand | null>(null)
const isUpdatingStatus = ref(false)

const handleDragStart = (demand: Demand) => {
  draggedDemand.value = demand
}

const handleDragEnd = () => {
  draggedDemand.value = null
}

const handleDrop = async (newStatus: string) => {
  if (!draggedDemand.value || isUpdatingStatus.value) return
  if (draggedDemand.value.status === newStatus) return

  isUpdatingStatus.value = true
  
  const result = await demandStore.updateDemand(draggedDemand.value.id, { status: newStatus })
  
  if (result.success) {
    await demandStore.fetchDemands()
  }
  
  draggedDemand.value = null
  isUpdatingStatus.value = false
}

const formatDate = (date: string) => new Date(date).toLocaleDateString('pt-BR')

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
  const labels: Record<string, string> = { LOW: 'Baixa', MEDIUM: 'Média', HIGH: 'Alta', URGENT: 'Urgente' }
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
  const labels: Record<string, string> = { PENDING: 'Pendente', IN_PROGRESS: 'Em Andamento', COMPLETED: 'Concluída', REJECTED: 'Rejeitada' }
  return labels[status] || status
}
</script>