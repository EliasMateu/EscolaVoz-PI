<template>
  <div>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 sm:gap-6">
    <div class="bg-white dark:bg-gray-800 overflow-hidden shadow rounded-lg">
      <div class="p-5">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <svg class="h-6 w-6 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
          <div class="ml-5 w-0 flex-1">
            <dl>
              <dt class="text-sm font-medium text-gray-500 dark:text-gray-400 truncate">{{ t('total') }}</dt>
              <dd class="text-lg font-medium text-gray-900 dark:text-white">{{ demands.length }}</dd>
            </dl>
          </div>
        </div>
      </div>
    </div>

    <div class="bg-white dark:bg-gray-800 overflow-hidden shadow rounded-lg">
      <div class="p-5">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <svg class="h-6 w-6 text-yellow-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div class="ml-5 w-0 flex-1">
            <dl>
              <dt class="text-sm font-medium text-gray-500 dark:text-gray-400 truncate">{{ t('pending') }}</dt>
              <dd class="text-lg font-medium text-gray-900 dark:text-white">{{ pendingCount }}</dd>
            </dl>
          </div>
        </div>
      </div>
    </div>

    <div class="bg-white dark:bg-gray-800 overflow-hidden shadow rounded-lg">
      <div class="p-5">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <svg class="h-6 w-6 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div class="ml-5 w-0 flex-1">
            <dl>
              <dt class="text-sm font-medium text-gray-500 dark:text-gray-400 truncate">{{ t('completed') }}</dt>
              <dd class="text-lg font-medium text-gray-900 dark:text-white">{{ completedCount }}</dd>
            </dl>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="mt-8">
    <div class="bg-white dark:bg-gray-800 shadow overflow-hidden sm:rounded-lg">
      <div class="px-4 py-5 sm:px-6 flex justify-between items-center">
        <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-white">
          {{ t('myDemands') }}
        </h3>
        <NuxtLink 
          to="/demands/new" 
          class="bg-primary-600 text-white px-4 py-2 rounded-lg hover:bg-primary-700 text-sm font-medium transition-colors"
        >
          {{ t('newDemand') }}
        </NuxtLink>
      </div>
      <div class="border-t border-gray-200 dark:border-gray-700">
        <div v-if="demands.length === 0" class="text-center py-12 text-gray-500 dark:text-gray-400">
          {{ t('noDemands') }}
        </div>
        <ul v-else class="divide-y divide-gray-200 dark:divide-gray-700">
          <li v-for="demand in demands" :key="demand.id" class="px-3 sm:px-6 py-3 sm:py-4 hover:bg-gray-50 dark:hover:bg-gray-700/50 transition-colors">
            <NuxtLink :to="`/demands/${demand.id}`" class="block">
            <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
              <div class="flex-1 min-w-0">
                <p class="text-sm font-medium text-primary-600 dark:text-primary-400 truncate">
                  {{ demand.title }}
                </p>
                <p class="text-xs sm:text-sm text-gray-500 dark:text-gray-400">
                  {{ demand.category_name }} • {{ t(demand.priority.toLowerCase()) }}
                </p>
              </div>
              <div class="flex-shrink-0">
                <span 
                  :class="statusClass(demand.status)"
                  class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full"
                >
                  {{ statusLabel(demand.status) }}
                </span>
              </div>
            </div>
            <div class="mt-2 flex items-center text-xs sm:text-sm text-gray-500 dark:text-gray-400">
              <svg class="flex-shrink-0 mr-1.5 h-4 w-4 sm:h-5 sm:w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
              {{ formatDate(demand.created_at) }}
            </div>
            </NuxtLink>
          </li>
        </ul>
      </div>
    </div>
  </div>

  <div v-if="user?.school_name" class="mt-4 text-sm text-gray-600 dark:text-gray-400">
    {{ t('school') }}: <strong>{{ user.school_name }}</strong>
  </div>
  </div>
</template>

<script setup lang="ts">
import { useThemeStore, translations } from '~/composables/useTheme'

definePageMeta({
  layout: 'dashboard'
})

const auth = useAuthStore()
const demandStore = useDemandStore()
const store = useThemeStore()

const t = (key: string) => translations[store.locale][key as keyof typeof translations['pt-BR']] || key

const user = computed(() => auth.user)
const demands = computed(() => demandStore.demands)
const pendingCount = computed(() => demands.value.filter(d => d.status === 'PENDING').length)
const completedCount = computed(() => demands.value.filter(d => d.status === 'COMPLETED').length)

onMounted(() => {
  store.initTheme()
  demandStore.fetchDemands()
})

const statusClass = (status: string) => {
  const classes: Record<string, string> = {
    PENDING: 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900/30 dark:text-yellow-400',
    IN_PROGRESS: 'bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-400',
    COMPLETED: 'bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400',
    REJECTED: 'bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400',
  }
  return classes[status] || 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300'
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

const formatDate = (date: string) => {
  return new Date(date).toLocaleDateString('pt-BR')
}
</script>