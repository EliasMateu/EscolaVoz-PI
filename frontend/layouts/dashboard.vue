<template>
  <div class="flex h-screen w-full bg-gray-50 dark:bg-gray-900">
    <AppSidebar :isOpen="sidebarOpen" @close="sidebarOpen = false" />

    <div 
      v-if="sidebarOpen" 
      class="fixed inset-0 bg-black/50 z-40 lg:hidden"
      @click="sidebarOpen = false"
    />

    <main class="flex-1 flex flex-col w-full min-w-0 h-screen">
      <header class="sticky top-0 z-30 bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 shadow-sm shrink-0">
        <div class="flex items-center justify-between h-16 px-4 sm:px-6 w-full">
          <button 
            @click="sidebarOpen = true"
            class="lg:hidden p-2 -ml-2 text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200"
          >
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
          
          <h1 class="text-lg sm:text-xl font-semibold text-gray-900 dark:text-white">
            {{ pageTitle }}
          </h1>
          
          <div class="flex items-center gap-2">
            <NuxtLink 
              to="/demands/new"
              class="sm:inline-flex items-center px-3 sm:px-4 py-2 text-sm font-medium text-white bg-primary-600 rounded-lg hover:bg-primary-700 transition-colors"
            >
              <svg class="w-4 h-4 sm:mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
              </svg>
              <span class="hidden sm:inline">Nova Demanda</span>
            </NuxtLink>
          </div>
        </div>
      </header>

      <div class="flex-1 w-full min-w-0 overflow-auto p-3 sm:p-6">
        <slot />
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
const sidebarOpen = ref(false)
const route = useRoute()

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
</script>