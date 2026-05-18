<template>
  <div class="flex h-screen w-full bg-gray-50 dark:bg-gray-900">
    <AppSidebar />

    <main class="flex-1 flex flex-col w-full min-w-0 h-screen overflow-hidden">
      <header class="sticky top-0 z-30 bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 shadow-sm shrink-0">
        <div class="flex items-center justify-between h-16 px-4 sm:px-6 w-full">
          <h1 class="text-xl font-semibold text-gray-900 dark:text-white">
            {{ pageTitle }}
          </h1>
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

      <div class="flex-1 w-full min-w-0 overflow-auto p-4 sm:p-6">
        <slot />
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
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