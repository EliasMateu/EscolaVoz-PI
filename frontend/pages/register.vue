<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Criar nova conta
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600">
          EscolaVoz - Gestão de Demandas Escolares
        </p>
      </div>
      
      <form class="mt-8 space-y-6" @submit.prevent="handleRegister">
        <div v-if="error" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
          {{ error }}
        </div>

        <div class="rounded-md shadow-sm space-y-4">
          <div>
            <label for="cpf" class="block text-sm font-medium text-gray-700">CPF</label>
            <input 
              id="cpf" 
              v-model="form.cpf"
              type="text" 
              required 
              maxlength="11"
              placeholder="Somente números"
              class="mt-1 appearance-none block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
            >
          </div>

          <div>
            <label for="first_name" class="block text-sm font-medium text-gray-700">Nome</label>
            <input 
              id="first_name" 
              v-model="form.first_name"
              type="text" 
              required 
              class="mt-1 appearance-none block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
            >
          </div>

          <div>
            <label for="last_name" class="block text-sm font-medium text-gray-700">Sobrenome</label>
            <input 
              id="last_name" 
              v-model="form.last_name"
              type="text" 
              required 
              class="mt-1 appearance-none block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
            >
          </div>

          <div>
            <label for="school_code" class="block text-sm font-medium text-gray-700">Código da Escola</label>
            <input 
              id="school_code" 
              v-model="form.school_code"
              type="text" 
              required 
              placeholder="Código fornecido pela diretoria"
              class="mt-1 appearance-none block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
            >
          </div>

          <div>
            <label for="password" class="block text-sm font-medium text-gray-700">Senha</label>
            <input 
              id="password" 
              v-model="form.password"
              type="password" 
              required 
              minlength="8"
              class="mt-1 appearance-none block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
            >
          </div>

          <div>
            <label for="password_confirm" class="block text-sm font-medium text-gray-700">Confirmar Senha</label>
            <input 
              id="password_confirm" 
              v-model="form.password_confirm"
              type="password" 
              required 
              class="mt-1 appearance-none block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
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
            <span v-else>Cadastrar</span>
          </button>
        </div>

        <div class="text-center">
          <NuxtLink to="/login" class="font-medium text-primary-600 hover:text-primary-500">
            Já tem uma conta? Entrar
          </NuxtLink>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
const auth = useAuthStore()
const router = useRouter()

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
    router.push('/dashboard')
  } else {
    error.value = result.error || 'Erro ao criar conta'
  }
}

onMounted(() => {
  if (auth.isAuthenticated) {
    router.push('/dashboard')
  }
})
</script>