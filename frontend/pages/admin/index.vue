<template>
  <div class="min-h-screen bg-gray-50">
    <header class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
        <h1 class="text-3xl font-bold text-gray-900">Dashboard Admin</h1>
        <div class="flex items-center space-x-4">
          <NuxtLink to="/dashboard" class="text-gray-600 hover:text-gray-900">
            Voltar
          </NuxtLink>
          <button 
            @click="handleExport"
            class="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700 text-sm"
          >
            Exportar CSV
          </button>
        </div>
      </div>
    </header>

    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="px-4 py-6 sm:px-0">
        <div v-if="stats" class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <div class="bg-white overflow-hidden shadow rounded-lg p-5">
            <div class="text-2xl font-bold text-gray-900">{{ stats.total }}</div>
            <div class="text-sm text-gray-500">Total de Demandas</div>
          </div>
          
          <div class="bg-white overflow-hidden shadow rounded-lg p-5">
            <div class="text-2xl font-bold text-yellow-600">{{ stats.by_status.pending }}</div>
            <div class="text-sm text-gray-500">Pendentes</div>
          </div>
          
          <div class="bg-white overflow-hidden shadow rounded-lg p-5">
            <div class="text-2xl font-bold text-blue-600">{{ stats.by_status.in_progress }}</div>
            <div class="text-sm text-gray-500">Em Andamento</div>
          </div>
          
          <div class="bg-white overflow-hidden shadow rounded-lg p-5">
            <div class="text-2xl font-bold text-green-600">{{ stats.by_status.completed }}</div>
            <div class="text-sm text-gray-500">Concluídas</div>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="bg-white shadow rounded-lg p-6">
            <h2 class="text-lg font-medium text-gray-900 mb-4">Por Categoria</h2>
            <div v-if="byCategory.length > 0" class="space-y-2">
              <div v-for="item in byCategory" :key="item.category" class="flex justify-between items-center">
                <span class="text-sm text-gray-700">{{ item.category }}</span>
                <span class="text-sm font-medium text-gray-900">{{ item.count }}</span>
              </div>
            </div>
            <div v-else class="text-gray-500 text-sm">Nenhum dado disponível</div>
          </div>

          <div class="bg-white shadow rounded-lg p-6">
            <h2 class="text-lg font-medium text-gray-900 mb-4">Por Escola</h2>
            <div v-if="bySchool.length > 0" class="space-y-2">
              <div v-for="item in bySchool" :key="item.school" class="flex justify-between items-center">
                <span class="text-sm text-gray-700">{{ item.school }}</span>
                <span class="text-sm font-medium text-gray-900">{{ item.count }}</span>
              </div>
            </div>
            <div v-else class="text-gray-500 text-sm">Nenhum dado disponível</div>
          </div>
        </div>

        <div v-if="stats" class="mt-6 bg-white shadow rounded-lg p-6">
          <h2 class="text-lg font-medium text-gray-900 mb-4">Por Prioridade</h2>
          <div class="grid grid-cols-4 gap-4">
            <div class="text-center">
              <div class="text-2xl font-bold text-gray-600">{{ stats.by_priority.LOW || 0 }}</div>
              <div class="text-sm text-gray-500">Baixa</div>
            </div>
            <div class="text-center">
              <div class="text-2xl font-bold text-yellow-600">{{ stats.by_priority.MEDIUM || 0 }}</div>
              <div class="text-sm text-gray-500">Média</div>
            </div>
            <div class="text-center">
              <div class="text-2xl font-bold text-orange-600">{{ stats.by_priority.HIGH || 0 }}</div>
              <div class="text-sm text-gray-500">Alta</div>
            </div>
            <div class="text-center">
              <div class="text-2xl font-bold text-red-600">{{ stats.by_priority.URGENT || 0 }}</div>
              <div class="text-sm text-gray-500">Urgente</div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: false
})

const dashboardStore = useDashboardStore()
const auth = useAuthStore()

const stats = computed(() => dashboardStore.stats)
const byCategory = computed(() => dashboardStore.byCategory)
const bySchool = computed(() => dashboardStore.bySchool)

onMounted(() => {
  if (auth.user?.role === 'SEDUC' || auth.user?.role === 'DIRECTORY') {
    dashboardStore.fetchStats()
    dashboardStore.fetchByCategory()
    dashboardStore.fetchBySchool()
  }
})

const handleExport = () => {
  dashboardStore.exportCSV()
}
</script>