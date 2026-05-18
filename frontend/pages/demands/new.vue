<template>
  <div class="min-h-screen bg-gray-50">
    <header class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
        <h1 class="text-3xl font-bold text-gray-900">Nova Demanda</h1>
        <NuxtLink to="/dashboard" class="text-gray-600 hover:text-gray-900">
          Voltar
        </NuxtLink>
      </div>
    </header>

    <main class="max-w-3xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="bg-white shadow px-4 py-5 sm:rounded-lg sm:p-6">
        <form @submit.prevent="handleSubmit">
          <div v-if="error" class="mb-4 bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
            {{ error }}
          </div>

          <div class="space-y-6">
            <div>
              <label for="title" class="block text-sm font-medium text-gray-700">Título</label>
              <input 
                id="title" 
                v-model="form.title"
                type="text" 
                required 
                class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                placeholder="Resumo da demanda"
              >
            </div>

            <div>
              <label for="category" class="block text-sm font-medium text-gray-700">Categoria</label>
              <select 
                id="category" 
                v-model="form.category"
                required 
                class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
              >
                <option value="">Selecione uma categoria</option>
                <option v-for="cat in categories" :key="cat.id" :value="cat.id">
                  {{ cat.name }}
                </option>
              </select>
            </div>

            <div>
              <label for="priority" class="block text-sm font-medium text-gray-700">Prioridade</label>
              <select 
                id="priority" 
                v-model="form.priority"
                required 
                class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
              >
                <option value="LOW">Baixa</option>
                <option value="MEDIUM">Média</option>
                <option value="HIGH">Alta</option>
                <option value="URGENT">Urgente</option>
              </select>
            </div>

            <div>
              <label for="description" class="block text-sm font-medium text-gray-700">
                Descrição
              </label>
              <textarea 
                id="description" 
                v-model="form.description"
                rows="4" 
                class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                placeholder="Descreva os detalhes da demanda..."
              ></textarea>
            </div>
          </div>

          <div class="mt-6 flex justify-end">
            <button 
              type="submit" 
              :disabled="isLoading"
              class="bg-primary-600 border border-transparent rounded-md shadow-sm py-2 px-4 text-sm font-medium text-white hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50"
            >
              {{ isLoading ? 'Enviando...' : 'Enviar Demanda' }}
            </button>
          </div>
        </form>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: false
})

const demandStore = useDemandStore()
const router = useRouter()

const form = reactive({
  title: '',
  description: '',
  category: '',
  priority: 'MEDIUM' as 'LOW' | 'MEDIUM' | 'HIGH' | 'URGENT',
})

const error = ref('')
const isLoading = computed(() => demandStore.isLoading)
const categories = computed(() => demandStore.categories)

onMounted(() => {
  demandStore.fetchCategories()
})

const handleSubmit = async () => {
  error.value = ''
  
  if (!form.title || !form.category) {
    error.value = 'Preencha os campos obrigatórios'
    return
  }

  const result = await demandStore.createDemand(form)
  
  if (result.success) {
    router.push('/dashboard')
  } else {
    error.value = result.error || 'Erro ao criar demanda'
  }
}
</script>