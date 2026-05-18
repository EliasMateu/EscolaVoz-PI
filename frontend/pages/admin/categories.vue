<template>
  <div>
    <div class="max-w-4xl mx-auto">
      <div class="bg-white dark:bg-gray-800 shadow rounded-lg p-6 mb-6">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-lg font-medium text-gray-900 dark:text-white">{{ t('categories') }}</h2>
          <button @click="openModal()" class="bg-primary-600 text-white px-4 py-2 rounded-lg hover:bg-primary-700 text-sm font-medium transition-colors">
            + Nova Categoria
          </button>
        </div>

        <div v-if="categories.length === 0" class="text-center py-8 text-gray-500 dark:text-gray-400">
          Nenhuma categoria cadastrada
        </div>

        <table v-else class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
          <thead class="bg-gray-50 dark:bg-gray-700">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Nome</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Descrição</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Status</th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Ações</th>
            </tr>
          </thead>
          <tbody class="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
            <tr v-for="cat in categories" :key="cat.id">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900 dark:text-white">{{ cat.name }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">{{ cat.description || '-' }}</td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span :class="cat.is_active ? 'bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400' : 'bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400'" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full">
                  {{ cat.is_active ? 'Ativa' : 'Inativa' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <button @click="openModal(cat)" class="text-primary-600 hover:text-primary-900 dark:text-primary-400 mr-3">Editar</button>
                <button @click="confirmDelete(cat)" class="text-red-600 hover:text-red-900 dark:text-red-400">Excluir</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div v-if="showModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 w-full max-w-md">
        <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-4">
          {{ editingCategory ? 'Editar Categoria' : 'Nova Categoria' }}
        </h3>
        
        <div v-if="error" class="mb-4 bg-red-50 dark:bg-red-900/30 border border-red-200 dark:border-red-800 text-red-700 dark:text-red-400 px-4 py-3 rounded">
          {{ error }}
        </div>

        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Nome</label>
            <input v-model="form.name" type="text" required class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white">
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Descrição</label>
            <textarea v-model="form.description" rows="3" class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"></textarea>
          </div>
          <div v-if="editingCategory" class="flex items-center">
            <input v-model="form.is_active" type="checkbox" id="is_active" class="h-4 w-4 text-primary-600 border-gray-300 rounded">
            <label for="is_active" class="ml-2 block text-sm text-gray-900 dark:text-gray-300">Categoria ativa</label>
          </div>
        </div>

        <div class="mt-6 flex justify-end space-x-3">
          <button @click="closeModal()" class="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700">Cancelar</button>
          <button @click="saveCategory()" :disabled="isLoading" class="px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 disabled:opacity-50">{{ isLoading ? 'Salvando...' : 'Salvar' }}</button>
        </div>
      </div>
    </div>

    <div v-if="showDeleteConfirm" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 w-full max-w-md">
        <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-4">Confirmar Exclusão</h3>
        <p class="text-gray-600 dark:text-gray-400 mb-6">Tem certeza que deseja excluir a categoria "{{ categoryToDelete?.name }}"?</p>
        <div class="flex justify-end space-x-3">
          <button @click="showDeleteConfirm = false" class="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700">Cancelar</button>
          <button @click="deleteCategory()" :disabled="isLoading" class="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 disabled:opacity-50">{{ isLoading ? 'Excluindo...' : 'Excluir' }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useThemeStore, translations } from '~/composables/useTheme'
import type { Category } from '~/composables/useCategories'

definePageMeta({
  layout: 'dashboard'
})

const categoryStore = useCategoryStore()
const auth = useAuthStore()
const store = useThemeStore()

const t = (key: string) => translations[store.locale][key as keyof typeof translations['pt-BR']] || key

const categories = computed(() => categoryStore.categories)
const isLoading = computed(() => categoryStore.isLoading)

const showModal = ref(false)
const showDeleteConfirm = ref(false)
const editingCategory = ref<Category | null>(null)
const categoryToDelete = ref<Category | null>(null)
const error = ref('')

const form = reactive({ name: '', description: '', is_active: true })

onMounted(() => {
  store.initTheme()
  if (auth.user?.role === 'SEDUC' || auth.user?.role === 'DIRECTORY') {
    categoryStore.fetchCategories()
  } else {
    navigateTo('/dashboard')
  }
})

const openModal = (category?: Category) => {
  if (category) {
    editingCategory.value = category
    form.name = category.name
    form.description = category.description || ''
    form.is_active = category.is_active
  } else {
    editingCategory.value = null
    form.name = ''
    form.description = ''
    form.is_active = true
  }
  error.value = ''
  showModal.value = true
}

const closeModal = () => { showModal.value = false; editingCategory.value = null }

const saveCategory = async () => {
  error.value = ''
  if (!form.name) { error.value = 'Nome é obrigatório'; return }
  
  let result
  if (editingCategory.value) {
    result = await categoryStore.updateCategory(editingCategory.value.id, { name: form.name, description: form.description })
  } else {
    result = await categoryStore.createCategory({ name: form.name, description: form.description })
  }
  if (result.success) { closeModal(); categoryStore.fetchCategories() }
  else { error.value = result.error || 'Erro ao salvar' }
}

const confirmDelete = (category: Category) => { categoryToDelete.value = category; showDeleteConfirm.value = true }

const deleteCategory = async () => {
  if (!categoryToDelete.value) return
  const result = await categoryStore.deleteCategory(categoryToDelete.value.id)
  if (result.success) { showDeleteConfirm.value = false; categoryToDelete.value = null }
  else { error.value = result.error || 'Erro ao excluir' }
}
</script>