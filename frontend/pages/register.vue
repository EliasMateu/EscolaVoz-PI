<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900 py-12 px-4 sm:px-6 lg:px-8 transition-colors">
    <div class="max-w-md w-full space-y-8">
      <div class="flex justify-between items-center">
        <div></div>
        <div class="flex items-center gap-3">
          <LocaleToggle />
          <ThemeToggle />
        </div>
      </div>

      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900 dark:text-white">
          {{ t('register') }}
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600 dark:text-gray-400">
          EscolaVoz - Gestão de Demandas Escolares
        </p>
      </div>
      
      <form class="mt-8 space-y-6" @submit.prevent="handleRegister">
        <div v-if="error" class="bg-red-50 dark:bg-red-900/30 border border-red-200 dark:border-red-800 text-red-700 dark:text-red-400 px-4 py-3 rounded">
          {{ error }}
        </div>

        <div class="rounded-md shadow-sm space-y-4">
          <div>
            <label for="cpf" class="block text-sm font-medium text-gray-700 dark:text-gray-300">CPF</label>
            <input 
              id="cpf" 
              v-model="form.cpf"
              type="text" 
              required 
              maxlength="11"
              placeholder="Somente números"
              class="mt-1 appearance-none block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-white rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-800"
            >
          </div>

          <div>
            <label for="first_name" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Nome</label>
            <input 
              id="first_name" 
              v-model="form.first_name"
              type="text" 
              required 
              class="mt-1 appearance-none block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-white rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-800"
            >
          </div>

          <div>
            <label for="last_name" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Sobrenome</label>
            <input 
              id="last_name" 
              v-model="form.last_name"
              type="text" 
              required 
              class="mt-1 appearance-none block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-white rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-800"
            >
          </div>

          <div>
            <label for="school_code" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Código da Escola</label>
            <input 
              id="school_code" 
              v-model="form.school_code"
              type="text" 
              required 
              placeholder="Código fornecido pela diretoria"
              class="mt-1 appearance-none block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-white rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-800"
            >
          </div>

          <div>
            <label for="password" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Senha</label>
            <input 
              id="password" 
              v-model="form.password"
              type="password" 
              required 
              minlength="8"
              class="mt-1 appearance-none block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-white rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-800"
            >
          </div>

          <div>
            <label for="password_confirm" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Confirmar Senha</label>
            <input 
              id="password_confirm" 
              v-model="form.password_confirm"
              type="password" 
              required 
              class="mt-1 appearance-none block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-white rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-800"
            >
          </div>
        </div>

        <div>
          <button 
            type="submit" 
            :disabled="isLoading"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50"
          >
            <span v-if="isLoading">Criando conta...</span>
            <span v-else>{{ t('register') }}</span>
          </button>
        </div>

        <div class="text-center">
          <NuxtLink to="/login" class="font-medium text-primary-600 hover:text-primary-500 dark:text-primary-400">
            {{ t('login') }}
          </NuxtLink>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useThemeStore, translations } from '~/composables/useTheme'

definePageMeta({
  layout: false
})

const auth = useAuthStore()
const store = useThemeStore()

const t = (key: string) => translations[store.locale][key as keyof typeof translations['pt-BR']] || key

const form = reactive({
  cpf: '',
  first_name: '',
  last_name: '',
  school_code: '',
  password: '',
  password_confirm: '',
})

const error = ref('')
const isLoading = computed(() => auth.isLoading)

const handleRegister = async () => {
  error.value = ''

  if (form.password !== form.password_confirm) {
    error.value = 'As senhas não coincidem'
    return
  }

  if (form.password.length < 8) {
    error.value = 'A senha deve ter pelo menos 8 caracteres'
    return
  }

  const result = await auth.register(form)
  
  if (result.success) {
    navigateTo('/dashboard', { replace: true })
  } else {
    error.value = result.error || 'Erro ao criar conta'
  }
}

onMounted(() => {
  store.initTheme()
  if (auth.isAuthenticated) {
    navigateTo('/dashboard', { replace: true })
  }
})
</script>