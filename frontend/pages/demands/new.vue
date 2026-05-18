<template>
  <div>
    <div class="max-w-3xl mx-auto">
      <div class="bg-white dark:bg-gray-800 shadow px-4 py-5 sm:rounded-lg sm:p-6">
        <form @submit.prevent="handleSubmit">
          <div v-if="error" class="mb-4 bg-red-50 dark:bg-red-900/30 border border-red-200 dark:border-red-800 text-red-700 dark:text-red-400 px-4 py-3 rounded">
            {{ error }}
          </div>

          <div class="space-y-6">
            <div>
              <label for="title" class="block text-sm font-medium text-gray-700 dark:text-gray-300">{{ t('title') }}</label>
              <input 
                id="title" 
                v-model="form.title"
                type="text" 
                required 
                class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                placeholder="Resumo da demanda"
              >
            </div>

            <div>
              <label for="category" class="block text-sm font-medium text-gray-700 dark:text-gray-300">{{ t('categories') }}</label>
              <select 
                id="category" 
                v-model="form.category"
                required 
                class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
              >
                <option value="">Selecione uma categoria</option>
                <option v-for="cat in categories" :key="cat.id" :value="cat.id">
                  {{ cat.name }}
                </option>
              </select>
            </div>

            <div>
              <label for="priority" class="block text-sm font-medium text-gray-700 dark:text-gray-300">{{ t('priority') }}</label>
              <select 
                id="priority" 
                v-model="form.priority"
                required 
                class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
              >
                <option value="LOW">{{ t('low') }}</option>
                <option value="MEDIUM">{{ t('medium') }}</option>
                <option value="HIGH">{{ t('high') }}</option>
                <option value="URGENT">{{ t('urgent') }}</option>
              </select>
            </div>

            <div>
              <label for="description" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                {{ t('description') }}
              </label>
              <textarea 
                id="description" 
                v-model="form.description"
                rows="4" 
                class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
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
              {{ isLoading ? 'Enviando...' : t('save') }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useThemeStore, translations } from '~/composables/useTheme'

definePageMeta({
  layout: 'dashboard'
})

const demandStore = useDemandStore()
const router = useRouter()
const store = useThemeStore()

const t = (key: string) => translations[store.locale][key as keyof typeof translations['pt-BR']] || key

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
  store.initTheme()
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