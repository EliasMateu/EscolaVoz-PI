<template>
  <aside 
    :class="[
      'fixed lg:relative z-50 h-screen w-64 bg-white dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700 shrink-0 flex flex-col transform transition-transform duration-300',
      isOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'
    ]"
  >
    <div class="flex items-center justify-between h-16 px-4 border-b border-gray-200 dark:border-gray-700">
      <NuxtLink to="/dashboard" class="flex items-center gap-2" @click="$emit('close')">
        <span class="text-xl font-bold text-primary-600">EscolaVoz</span>
      </NuxtLink>
      <button 
        @click="$emit('close')"
        class="lg:hidden p-2 -mr-2 text-gray-500 hover:text-gray-700 dark:text-gray-400"
      >
        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>

    <div class="flex items-center gap-3 px-4 py-4 border-b border-gray-200 dark:border-gray-700">
      <div v-if="mounted" class="w-10 h-10 rounded-full bg-primary-100 dark:bg-primary-900/30 flex items-center justify-center shrink-0">
        <span class="text-primary-600 dark:text-primary-400 font-semibold text-sm">
          {{ hasUser ? userInitials : '?' }}
        </span>
      </div>
      <div v-else class="w-10 h-10 rounded-full bg-primary-100 dark:bg-primary-900/30 flex items-center justify-center shrink-0">
        <span class="text-primary-600 dark:text-primary-400 font-semibold text-sm">?</span>
      </div>
      <div v-if="mounted" class="flex-1 min-w-0">
        <p class="text-sm font-medium text-gray-900 dark:text-white truncate">
          {{ hasUser ? userName : 'Usuário' }}
        </p>
        <p class="text-xs text-gray-500 dark:text-gray-400 truncate">
          {{ hasUser ? userRole : '' }}
        </p>
      </div>
      <div v-else class="flex-1 min-w-0">
        <p class="text-sm font-medium text-gray-900 dark:text-white truncate">Usuário</p>
        <p class="text-xs text-gray-500 dark:text-gray-400 truncate"></p>
      </div>
    </div>

    <nav class="flex-1 overflow-y-auto py-4 px-3 space-y-1">
      <NuxtLink 
        to="/dashboard"
        @click="$emit('close')"
        class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors w-full"
        :class="isActive('/dashboard') 
          ? 'bg-primary-50 dark:bg-primary-900/20 text-primary-600 dark:text-primary-400' 
          : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'"
      >
        <svg class="w-5 h-5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
        </svg>
        Dashboard
      </NuxtLink>

      <NuxtLink 
        to="/demands/new"
        @click="$emit('close')"
        class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors w-full"
        :class="isActive('/demands/new') 
          ? 'bg-primary-50 dark:bg-primary-900/20 text-primary-600 dark:text-primary-400' 
          : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'"
      >
        <svg class="w-5 h-5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        Nova Demanda
      </NuxtLink>

      <button 
          v-if="mounted && hasUser && isAdmin"
          @click="adminOpen = !adminOpen"
        class="flex items-center justify-between w-full px-3 py-2.5 rounded-lg text-sm font-medium text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
      >
        <span class="flex items-center gap-3">
          <svg class="w-5 h-5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
          </svg>
          Administração
        </span>
        <svg 
          :class="['w-4 h-4 transition-transform shrink-0', adminOpen ? 'rotate-180' : '']" 
          fill="none" viewBox="0 0 24 24" stroke="currentColor"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      <div v-if="mounted && isAdmin && adminOpen" class="pl-4 space-y-1 mt-1">
        <NuxtLink 
          to="/admin"
          @click="$emit('close')"
          class="flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-colors w-full"
          :class="isActive('/admin') && !isActive('/admin/')
            ? 'bg-primary-50 dark:bg-primary-900/20 text-primary-600 dark:text-primary-400' 
            : 'text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'"
        >
          <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
          </svg>
          Estatísticas
        </NuxtLink>

        <NuxtLink 
          to="/admin/kanban"
          @click="$emit('close')"
          class="flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-colors w-full"
          :class="isActive('/admin/kanban')
            ? 'bg-primary-50 dark:bg-primary-900/20 text-primary-600 dark:text-primary-400' 
            : 'text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'"
        >
          <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17V7m0 10a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2a2 2 0 012 2m0 10a2 2 0 002 2h2a2 2 0 002-2M9 7a2 2 0 012-2h2a2 2 0 012 2m0 10V7m0 10a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2h-2a2 2 0 00-2 2" />
          </svg>
          Kanban
        </NuxtLink>

        <NuxtLink 
          v-if="mounted && isSEDUC"
          to="/admin/categories"
          @click="$emit('close')"
          class="flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-colors w-full"
          :class="isActive('/admin/categories')
            ? 'bg-primary-50 dark:bg-primary-900/20 text-primary-600 dark:text-primary-400' 
            : 'text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'"
        >
          <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
          </svg>
          Categorias
        </NuxtLink>
      </div>

      <div v-if="mounted && hasUser && user?.school_name" class="pt-4 mt-4 border-t border-gray-200 dark:border-gray-700">
        <p class="px-3 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider mb-2">
          Escola
        </p>
        <div class="px-3 py-2 text-sm text-gray-600 dark:text-gray-400">
          <p class="font-medium">{{ user.school_name }}</p>
          <p class="text-xs">{{ user.school_code }}</p>
        </div>
      </div>
    </nav>

    <div class="p-4 border-t border-gray-200 dark:border-gray-700 space-y-3">
      <div class="flex items-center justify-between">
        <button 
          @click="store.toggleTheme()"
          class="p-2 rounded-lg text-gray-500 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700 transition-colors"
          :title="store.theme === 'light' ? 'Modo escuro' : 'Modo claro'"
        >
          <svg v-if="store.theme === 'light'" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
          </svg>
          <svg v-else class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
          </svg>
        </button>
        
        <div class="relative" ref="localeRef">
          <button 
            @click="showLocaleMenu = !showLocaleMenu"
            class="px-2 py-1 text-xs font-medium rounded bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300"
          >
            {{ store.locale === 'pt-BR' ? 'PT' : 'EN' }}
          </button>
          <div v-if="showLocaleMenu" class="absolute bottom-full mb-2 left-0 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg shadow-lg py-1 z-10">
            <button 
              @click="setLocale('pt-BR')"
              class="block w-full px-4 py-2 text-sm text-left text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
            >
              🇧🇷 Português
            </button>
            <button 
              @click="setLocale('en')"
              class="block w-full px-4 py-2 text-sm text-left text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
            >
              🇺🇸 English
            </button>
          </div>
        </div>
      </div>
      
      <button 
        @click="handleLogout"
        class="w-full flex items-center justify-center gap-2 px-4 py-2 text-sm font-medium text-red-600 dark:text-red-400 bg-red-50 dark:bg-red-900/20 rounded-lg hover:bg-red-100 dark:hover:bg-red-900/30 transition-colors"
      >
        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
        </svg>
        Sair
      </button>
    </div>
  </aside>
</template>

<script setup lang="ts">
import { useThemeStore } from '~/composables/useTheme'

defineProps<{
  isOpen: boolean
}>()

defineEmits<{
  close: []
}>()

const route = useRoute()
const auth = useAuthStore()
const store = useThemeStore()

const showLocaleMenu = ref(false)
const adminOpen = ref(true)
const localeRef = ref<HTMLElement | null>(null)
const mounted = ref(false)

onMounted(() => { mounted.value = true })

const user = computed(() => auth.user)
const hasUser = computed(() => !!user.value && !!user.value.email)
const isAdmin = computed(() => user.value?.role === 'SEDUC' || user.value?.role === 'DIRECTORY')
const isSEDUC = computed(() => user.value?.role === 'SEDUC')

const userInitials = computed(() => {
  const first = user.value?.first_name?.[0] || ''
  const last = user.value?.last_name?.[0] || ''
  return (first + last).toUpperCase() || '?'
})

const userName = computed(() => {
  const name = `${user.value?.first_name || ''} ${user.value?.last_name || ''}`.trim()
  return name || 'Usuário'
})

const userRole = computed(() => {
  const roles: Record<string, string> = {
    EMPLOYEE: 'Funcionário',
    PRINCIPAL: 'Diretor',
    DIRECTORY: 'Diretoria',
    SEDUC: 'SEDUC',
  }
  return roles[user.value?.role || ''] || user.value?.role
})

const isActive = (path: string) => {
  return route.path === path || route.path.startsWith(path + '/')
}

const handleLogout = () => {
  auth.logout()
  navigateTo('/login')
}

const setLocale = (locale: 'pt-BR' | 'en') => {
  store.setLocale(locale)
  showLocaleMenu.value = false
}

onMounted(() => {
  document.addEventListener('click', (e) => {
    if (localeRef.value && !localeRef.value.contains(e.target as Node)) {
      showLocaleMenu.value = false
    }
  })
})
</script>