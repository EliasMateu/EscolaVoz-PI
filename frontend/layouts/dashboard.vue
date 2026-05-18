<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900">
    <div class="flex">
      <AppSidebar :is-open="sidebarOpen" @close="sidebarOpen = false" />

      <div class="flex-1 lg:ml-64">
        <header class="sticky top-0 z-30 bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 shadow-sm">
          <div class="flex items-center justify-between h-16 px-4 sm:px-6 lg:px-8">
            <div class="flex items-center gap-4">
              <button 
                @click="sidebarOpen = true"
                class="lg:hidden p-2 rounded-lg text-gray-500 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700"
              >
                <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                </svg>
              </button>
              <h1 class="text-xl font-semibold text-gray-900 dark:text-white">
                {{ pageTitle }}
              </h1>
            </div>
            <div class="flex items-center gap-2">
              <NuxtLink 
                to="/demands/new"
                class="hidden sm:inline-flex items-center px-4 py-2 text-sm font-medium text-white bg-primary-600 rounded-lg hover:bg-primary-700 transition-colors"
              >
                <svg class="w-4 h-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                </svg>
                Nova Demanda
              </NuxtLink>
            </div>
          </div>
        </header>

        <main class="p-4 sm:p-6 lg:p-8">
          <slot />
        </main>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const route = useRoute()

const sidebarOpen = ref(false)

const pageTitle = computed(() => {
  const titles: Record<string, string> = {
    '/dashboard': 'Dashboard',
    '/demands/new': 'Nova Demanda',
    '/admin': 'Dashboard Admin',
    '/admin/kanban': 'Kanban de Demandas',
    '/admin/categories': 'Gerenciar Categorias',
  }
  
  for (const [path, title] of Object.entries(titles)) {
    if (route.path === path || route.path.startsWith(path + '/')) {
      return title
    }
  }
  return 'EscolaVoz'
})

watch(() => route.path, () => {
  sidebarOpen.value = false
})
</script>