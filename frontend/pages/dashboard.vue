<template>
  <div class="min-h-screen bg-gray-50">
    <header class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
        <h1 class="text-3xl font-bold text-gray-900">Dashboard</h1>
        <div class="flex items-center space-x-4">
          <span class="text-gray-700">{{ user?.first_name }} {{ user?.last_name }}</span>
          <span class="px-2 py-1 text-xs rounded bg-gray-200">{{ user?.role }}</span>
          <button 
            @click="handleLogout"
            class="text-sm text-red-600 hover:text-red-800"
          >
            Sair
          </button>
        </div>
      </div>
    </header>

    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="px-4 py-6 sm:px-0">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="p-5">
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <svg class="h-6 w-6 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                </div>
                <div class="ml-5 w-0 flex-1">
                  <dl>
                    <dt class="text-sm font-medium text-gray-500 truncate">Total de Demandas</dt>
                    <dd class="text-lg font-medium text-gray-900">{{ demands.length }}</dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="p-5">
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <svg class="h-6 w-6 text-yellow-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <div class="ml-5 w-0 flex-1">
                  <dl>
                    <dt class="text-sm font-medium text-gray-500 truncate">Pendentes</dt>
                    <dd class="text-lg font-medium text-gray-900">{{ pendingCount }}</dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="p-5">
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <svg class="h-6 w-6 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <div class="ml-5 w-0 flex-1">
                  <dl>
                    <dt class="text-sm font-medium text-gray-500 truncate">Concluídas</dt>
                    <dd class="text-lg font-medium text-gray-900">{{ completedCount }}</dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="mt-8">
          <div class="bg-white shadow overflow-hidden sm:rounded-lg">
            <div class="px-4 py-5 sm:px-6 flex justify-between items-center">
              <h3 class="text-lg leading-6 font-medium text-gray-900">
                Minhas Demandas
              </h3>
              <NuxtLink 
                to="/demands/new" 
                class="bg-primary-600 text-white px-4 py-2 rounded-md hover:bg-primary-700 text-sm"
              >
                Nova Demanda
              </NuxtLink>
            </div>
            <div class="border-t border-gray-200">
              <div v-if="demands.length === 0" class="text-center py-12 text-gray-500">
                Nenhuma demanda cadastrada
              </div>
              <ul v-else class="divide-y divide-gray-200">
                <li v-for="demand in demands" :key="demand.id" class="px-4 py-4 sm:px-6">
                  <div class="flex items-center justify-between">
                    <div class="flex-1 min-w-0">
                      <p class="text-sm font-medium text-primary-600 truncate">
                        {{ demand.title }}
                      </p>
                      <p class="text-sm text-gray-500">
                        {{ demand.category_name }} • {{ demand.priority }}
                      </p>
                    </div>
                    <div class="ml-2 flex-shrink-0 flex">
                      <span 
                        :class="statusClass(demand.status)"
                        class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full"
                      >
                        {{ statusLabel(demand.status) }}
                      </span>
                    </div>
                  </div>
                  <div class="mt-2 sm:flex sm:justify-between">
                    <div class="flex items-center text-sm text-gray-500">
                      <svg class="flex-shrink-0 mr-1.5 h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                      </svg>
                      {{ formatDate(demand.created_at) }}
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div v-if="user?.school_name" class="mt-4 text-sm text-gray-600">
          Escola: <strong>{{ user.school_name }}</strong>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
const auth = useAuthStore()
const demandStore = useDemandStore()

const user = computed(() => auth.user)
const demands = computed(() => demandStore.demands)
const pendingCount = computed(() => demands.value.filter(d => d.status === 'PENDING').length)
const completedCount = computed(() => demands.value.filter(d => d.status === 'COMPLETED').length)

onMounted(() => {
  demandStore.fetchDemands()
})

const handleLogout = () => {
  auth.logout()
}

const statusClass = (status: string) => {
  const classes: Record<string, string> = {
    PENDING: 'bg-yellow-100 text-yellow-800',
    IN_PROGRESS: 'bg-blue-100 text-blue-800',
    COMPLETED: 'bg-green-100 text-green-800',
    REJECTED: 'bg-red-100 text-red-800',
  }
  return classes[status] || 'bg-gray-100 text-gray-800'
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