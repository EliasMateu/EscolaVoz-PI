<template>
  <div class="flex flex-wrap items-center gap-3">
    <div class="flex-1 min-w-[200px] max-w-xs">
      <select
        v-model="localFilters.school"
        class="w-full rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white text-sm py-2 px-3 focus:ring-2 focus:ring-primary-500/20 focus:border-primary-500"
      >
        <option value="">Todas as escolas</option>
        <option v-for="school in schoolsList" :key="school.code" :value="school.code">
          {{ school.name }}
        </option>
      </select>
    </div>

    <div class="flex-1 min-w-[150px] max-w-xs">
      <select
        v-model="localFilters.priority"
        class="w-full rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white text-sm py-2 px-3 focus:ring-2 focus:ring-primary-500/20 focus:border-primary-500"
      >
        <option value="">Todas as prioridades</option>
        <option value="LOW">Baixa</option>
        <option value="MEDIUM">Média</option>
        <option value="HIGH">Alta</option>
        <option value="URGENT">Urgente</option>
      </select>
    </div>

    <div class="flex-1 min-w-[150px] max-w-xs">
      <select
        v-model="localFilters.category"
        class="w-full rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white text-sm py-2 px-3 focus:ring-2 focus:ring-primary-500/20 focus:border-primary-500"
      >
        <option value="">Todas as categorias</option>
        <option v-for="cat in categoriesList" :key="cat.id" :value="cat.id">
          {{ cat.name }}
        </option>
      </select>
    </div>

    <div class="flex-1 min-w-[150px] max-w-xs">
      <input
        v-model="localFilters.date_from"
        type="date"
        class="w-full rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white text-sm py-2 px-3 focus:ring-2 focus:ring-primary-500/20 focus:border-primary-500"
        placeholder="De"
      />
    </div>

    <div class="flex-1 min-w-[150px] max-w-xs">
      <input
        v-model="localFilters.date_to"
        type="date"
        class="w-full rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white text-sm py-2 px-3 focus:ring-2 focus:ring-primary-500/20 focus:border-primary-500"
        placeholder="Até"
      />
    </div>

    <button
      @click="clearFilters"
      class="px-4 py-2 text-sm font-medium text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white bg-gray-100 dark:bg-gray-700 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors"
    >
      Limpar
    </button>
  </div>
</template>

<script setup lang="ts">
interface School {
  id: number
  name: string
  code: string
}

interface Category {
  id: number
  name: string
}

interface Filters {
  school: string
  priority: string
  category: string
  date_from: string
  date_to: string
}

const props = defineProps<{
  schools: any
  categories: any
}>()

const emit = defineEmits<{
  (e: 'update:filters', filters: Filters): void
}>()

const schoolsList = computed(() => {
  if (!props.schools) return []
  if (Array.isArray(props.schools)) return props.schools
  if (props.schools && props.schools.results) return props.schools.results
  return []
})

const categoriesList = computed(() => {
  if (!props.categories) return []
  if (Array.isArray(props.categories)) return props.categories
  if (props.categories && props.categories.results) return props.categories.results
  return []
})

const localFilters = reactive<Filters>({
  school: '',
  priority: '',
  category: '',
  date_from: '',
  date_to: '',
})

watch(localFilters, (newFilters) => {
  emit('update:filters', { ...newFilters })
}, { deep: true })

const clearFilters = () => {
  localFilters.school = ''
  localFilters.priority = ''
  localFilters.category = ''
  localFilters.date_from = ''
  localFilters.date_to = ''
}
</script>