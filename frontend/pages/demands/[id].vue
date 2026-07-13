<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900">
    <div class="max-w-4xl mx-auto px-3 sm:px-4 py-4 sm:py-8">
      <div v-if="isLoading" class="flex items-center justify-center py-12">
        <svg class="animate-spin h-8 w-8 text-primary-600" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
      </div>

      <div v-else-if="!demand" class="text-center py-12">
        <p class="text-gray-500 dark:text-gray-400">Demanda não encontrada.</p>
        <NuxtLink to="/dashboard" class="text-primary-600 hover:text-primary-500 mt-2 inline-block">
          Voltar ao dashboard
        </NuxtLink>
      </div>

      <div v-else>
        <NuxtLink to="/dashboard" class="inline-flex items-center text-sm text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300 mb-3 sm:mb-4">
          <svg class="w-5 h-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
          Voltar
        </NuxtLink>

        <div class="bg-white dark:bg-gray-800 shadow rounded-lg overflow-hidden">
          <div class="px-4 sm:px-6 py-4 border-b border-gray-200 dark:border-gray-700">
            <div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-3">
              <div class="flex-1 min-w-0">
                <h1 class="text-lg sm:text-xl font-bold text-gray-900 dark:text-white truncate">
                  {{ demand.title }}
                </h1>
                <div class="flex flex-wrap items-center gap-2 sm:gap-3 mt-2">
                  <span :class="['inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium', statusClass(demand.status)]">
                    {{ statusLabel(demand.status) }}
                  </span>
                  <span :class="['inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium', priorityClass(demand.priority)]">
                    {{ priorityLabel(demand.priority) }}
                  </span>
                </div>
              </div>
              <div v-if="isAdmin" class="flex flex-wrap items-center gap-2">
                <button
                  v-if="canEdit"
                  @click="toggleEdit"
                  class="px-3 py-1.5 text-sm font-medium text-gray-700 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors"
                >
                  {{ isEditing ? 'Cancelar' : 'Editar' }}
                </button>
                <button
                  v-if="!isEditing && demand.status === 'PENDING'"
                  @click="handleStartProgress"
                  class="px-3 py-1.5 text-sm font-medium text-white bg-primary-600 rounded-lg hover:bg-primary-700 transition-colors"
                >
                  Iniciar
                </button>
                <button
                  v-if="demand.status === 'IN_PROGRESS' && !isEditing"
                  @click="handleComplete"
                  class="px-3 py-1.5 text-sm font-medium text-white bg-green-600 rounded-lg hover:bg-green-700 transition-colors"
                >
                  Concluir
                </button>
              </div>
            </div>
          </div>

          <div class="px-6 py-4 space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                  Categoria
                </h3>
                <p v-if="!isEditing" class="mt-1 text-sm text-gray-900 dark:text-white">
                  {{ demand.category_name }}
                </p>
                <select
                  v-else
                  v-model="editForm.category"
                  class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                >
                  <option v-for="cat in categories" :key="cat.id" :value="cat.id">
                    {{ cat.name }}
                  </option>
                </select>
              </div>

              <div>
                <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                  Escola
                </h3>
                <p class="mt-1 text-sm text-gray-900 dark:text-white">
                  {{ demand.school_name }}
                </p>
              </div>

              <div>
                <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                  Criado por
                </h3>
                <p class="mt-1 text-sm text-gray-900 dark:text-white">
                  {{ demand.created_by_name }}
                </p>
              </div>

              <div>
                <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                  Data de criação
                </h3>
                <p class="mt-1 text-sm text-gray-900 dark:text-white">
                  {{ formatDate(demand.created_at) }}
                </p>
              </div>

              <div v-if="demand.updated_at !== demand.created_at">
                <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                  Última atualização
                </h3>
                <p class="mt-1 text-sm text-gray-900 dark:text-white">
                  {{ formatDate(demand.updated_at) }}
                </p>
              </div>

              <div v-if="demand.resolved_at">
                <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                  Data de conclusão
                </h3>
                <p class="mt-1 text-sm text-gray-900 dark:text-white">
                  {{ formatDate(demand.resolved_at) }}
                </p>
              </div>

              <div v-if="isAdmin && isEditing">
                <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                  Status
                </h3>
                <select
                  v-model="editForm.status"
                  class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                >
                  <option value="PENDING">Pendente</option>
                  <option value="IN_PROGRESS">Em Andamento</option>
                  <option value="COMPLETED">Concluída</option>
                  <option value="REJECTED">Rejeitada</option>
                </select>
              </div>

              <div v-if="isAdmin && isEditing">
                <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                  Prioridade
                </h3>
                <select
                  v-model="editForm.priority"
                  class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                >
                  <option value="LOW">Baixa</option>
                  <option value="MEDIUM">Média</option>
                  <option value="HIGH">Alta</option>
                  <option value="URGENT">Urgente</option>
                </select>
              </div>
            </div>

            <div>
              <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-2">
                Descrição
              </h3>
              <p v-if="!isEditing" class="text-sm text-gray-900 dark:text-white whitespace-pre-wrap">
                {{ demand.description || 'Sem descrição.' }}
              </p>
              <textarea
                v-else
                v-model="editForm.description"
                rows="6"
                class="block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                placeholder="Descreva os detalhes da demanda..."
              ></textarea>
            </div>

            <div v-if="getImageUrl(demand) || (isEditing && (editForm.image || imagePreview))">
              <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-2">
                Imagem
              </h3>
              <div v-if="!isEditing && getImageUrl(demand)" class="mt-2">
                <img 
                  :src="getImageUrl(demand)" 
                  alt="Imagem da demanda" 
                  class="max-w-md rounded-lg border border-gray-200 dark:border-gray-700"
                >
              </div>
              <div v-else-if="isEditing" class="mt-2">
                <div v-if="imagePreview" class="relative w-48 h-48 rounded-lg overflow-hidden border border-gray-300 dark:border-gray-600 mb-2">
                  <img :src="imagePreview" alt="Preview" class="w-full h-full object-cover">
                  <button 
                    type="button"
                    @click="removeImage"
                    class="absolute top-1 right-1 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center text-xs hover:bg-red-600"
                  >
                    ×
                  </button>
                </div>
                <label 
                  for="image-upload"
                  class="cursor-pointer px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 inline-block"
                >
                  {{ demand.image_url ? 'Alterar imagem' : 'Adicionar imagem' }}
                </label>
                <input 
                  id="image-upload" 
                  type="file"
                  accept="image/*"
                  class="hidden"
                  @change="handleImageChange"
                >
                <button 
                  v-if="demand.image_url && !editForm.image"
                  type="button"
                  @click="handleRemoveImage"
                  class="ml-2 px-4 py-2 border border-red-300 dark:border-red-600 rounded-md shadow-sm text-sm font-medium text-red-700 dark:text-red-300 bg-red-50 dark:bg-red-900/30 hover:bg-red-100 dark:hover:bg-red-900/50"
                >
                  Remover
                </button>
              </div>
            </div>

            <div v-if="isEditing">
              <div class="flex justify-end gap-3 pt-4 border-t border-gray-200 dark:border-gray-700">
                <button
                  @click="toggleEdit"
                  class="px-4 py-2 text-sm font-medium text-gray-700 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors"
                >
                  Cancelar
                </button>
                <button
                  @click="handleSave"
                  :disabled="isSaving"
                  class="px-4 py-2 text-sm font-medium text-white bg-primary-600 rounded-lg hover:bg-primary-700 transition-colors disabled:opacity-50"
                >
                  {{ isSaving ? 'Salvando...' : 'Salvar alterações' }}
                </button>
              </div>
            </div>
          </div>
        </div>

        <div v-if="error" class="mt-4 bg-red-50 dark:bg-red-900/30 border border-red-200 dark:border-red-800 text-red-700 dark:text-red-400 px-4 py-3 rounded">
          {{ error }}
        </div>

        <div v-if="successMessage" class="mt-4 bg-green-50 dark:bg-green-900/30 border border-green-200 dark:border-green-800 text-green-700 dark:text-green-400 px-4 py-3 rounded">
          {{ successMessage }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Demand, Category } from '~/types'

definePageMeta({
  layout: 'dashboard',
  middleware: 'auth',
})

const route = useRoute()
const demandStore = useDemandStore()
const categoryStore = useCategoryStore()
const auth = useAuthStore()
const store = useThemeStore()

const demandId = route.params.id as string

const demand = ref<Demand | null>(null)
const isLoading = ref(true)
const isEditing = ref(false)
const isSaving = ref(false)
const error = ref('')
const successMessage = ref('')

const isAdmin = computed(() => {
  return auth.user?.role === 'SEDUC' || auth.user?.role === 'DIRECTORY'
})

const canEdit = computed(() => {
  if (!demand.value) return false
  if (isAdmin.value) return true
  return false
})

const categories = computed(() => {
  const data = categoryStore.categories
  if (!data) return []
  if (Array.isArray(data)) return data
  if (data?.results) return data.results
  return []
})

const editForm = reactive({
  title: '',
  description: '',
  category: '',
  status: '',
  priority: '',
  image: null as File | null,
})

const imagePreview = ref<string | null>(null)
const removeImageFlag = ref(false)

const handleImageChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  
  if (file) {
    if (file.size > 5 * 1024 * 1024) {
      error.value = 'A imagem deve ter no máximo 5MB'
      return
    }
    editForm.image = file
    imagePreview.value = URL.createObjectURL(file)
    removeImageFlag.value = false
  }
}

const removeImage = () => {
  editForm.image = null
  imagePreview.value = null
}

const handleRemoveImage = () => {
  editForm.image = null
  imagePreview.value = null
  removeImageFlag.value = true
}

const statusClass = (status: string) => {
  const classes: Record<string, string> = {
    PENDING: 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900/30 dark:text-yellow-400',
    IN_PROGRESS: 'bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-400',
    COMPLETED: 'bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400',
    REJECTED: 'bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400',
  }
  return classes[status] || ''
}

const statusLabel = (status: string) => {
  const labels: Record<string, string> = {
    PENDING: 'Pendente',
    IN_PROGRESS: 'Em Andamento',
    COMPLETED: 'Concluída',
    REJECTED: 'Rejeitada',
  }
  return labels[status] || status
}

const priorityClass = (priority: string) => {
  const classes: Record<string, string> = {
    LOW: 'bg-gray-100 text-gray-600 dark:bg-gray-600 dark:text-gray-300',
    MEDIUM: 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900/30 dark:text-yellow-400',
    HIGH: 'bg-orange-100 text-orange-800 dark:bg-orange-900/30 dark:text-orange-400',
    URGENT: 'bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400',
  }
  return classes[priority] || ''
}

const priorityLabel = (priority: string) => {
  const labels: Record<string, string> = {
    LOW: 'Baixa',
    MEDIUM: 'Média',
    HIGH: 'Alta',
    URGENT: 'Urgente',
  }
  return labels[priority] || priority
}

const getImageUrl = (d: Demand | null) => d?.image_url || null

const formatDate = (date: string) => {
  return new Date(date).toLocaleDateString('pt-BR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  })
}

const toggleEdit = () => {
  if (isEditing.value) {
    isEditing.value = false
    imagePreview.value = null
    removeImageFlag.value = false
  } else if (demand.value) {
    editForm.title = demand.value.title
    editForm.description = demand.value.description
    editForm.category = demand.value.category
    editForm.status = demand.value.status
    editForm.priority = demand.value.priority
    editForm.image = null
    imagePreview.value = demand.value.image_url
    removeImageFlag.value = false
    isEditing.value = true
  }
}

const handleSave = async () => {
  if (!demand.value) return

  isSaving.value = true
  error.value = ''
  successMessage.value = ''

  const updateData: any = {
    title: editForm.title,
    description: editForm.description,
    category: editForm.category,
  }

  if (isAdmin.value) {
    updateData.status = editForm.status
    updateData.priority = editForm.priority
  }

  if (editForm.image || removeImageFlag.value) {
    updateData.image = editForm.image
    updateData.removeImage = removeImageFlag.value
  }

  const result = await demandStore.updateDemand(demand.value.id, updateData)

  if (result.success && result.data) {
    demand.value = result.data
    isEditing.value = false
    imagePreview.value = null
    removeImageFlag.value = false
    successMessage.value = 'Demanda atualizada com sucesso!'
    setTimeout(() => {
      successMessage.value = ''
    }, 3000)
  } else {
    error.value = result.error || 'Erro ao atualizar demanda'
  }

  isSaving.value = false
}

const handleStartProgress = async () => {
  if (!demand.value) return

  isSaving.value = true
  error.value = ''

  const result = await demandStore.updateDemand(demand.value.id, { status: 'IN_PROGRESS' })

  if (result.success && result.data) {
    demand.value = result.data
  } else {
    error.value = result.error || 'Erro ao iniciar demanda'
  }

  isSaving.value = false
}

const handleComplete = async () => {
  if (!demand.value) return

  isSaving.value = true
  error.value = ''

  const result = await demandStore.updateDemand(demand.value.id, { status: 'COMPLETED' })

  if (result.success && result.data) {
    demand.value = result.data
  } else {
    error.value = result.error || 'Erro ao concluir demanda'
  }

  isSaving.value = false
}

onMounted(async () => {
  store.initTheme()
  
  await categoryStore.fetchCategories()
  
  demand.value = await demandStore.fetchDemand(demandId)
  isLoading.value = false
})
</script>