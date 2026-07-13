<template>
  <div class="relative" ref="wrapperRef">
    <button
      type="button"
      @click="open = !open"
      class="mt-1 block w-full border border-gray-300 dark:border-gray-600 rounded-md shadow-sm py-2 px-3 focus:ring-primary-500 focus:border-primary-500 sm:text-sm bg-white dark:bg-gray-700 text-gray-900 dark:text-white text-left flex items-center justify-between gap-2"
      :class="{ 'ring-2 ring-primary-500 border-primary-500': open }"
    >
      <span :class="{ 'text-gray-400 dark:text-gray-500': !selectedLabel }">
        {{ selectedLabel || placeholder }}
      </span>
      <svg
        :class="['w-4 h-4 shrink-0 text-gray-400 transition-transform', open && 'rotate-180']"
        fill="none" viewBox="0 0 24 24" stroke="currentColor"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </button>

    <div
      v-if="open"
      class="fixed z-50 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg shadow-lg py-1 max-h-60 overflow-auto"
      :style="dropdownStyle"
    >
      <button
        v-for="opt in options"
        :key="opt.value"
        type="button"
        @click="select(opt.value)"
        class="block w-full px-4 py-2 text-sm text-left transition-colors"
        :class="modelValue === opt.value
          ? 'bg-primary-50 dark:bg-primary-900/20 text-primary-600 dark:text-primary-400 font-medium'
          : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'"
      >
        {{ opt.label }}
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  modelValue: string
  options: { value: string; label: string }[]
  placeholder?: string
}>()

const emit = defineEmits<{
  'update:modelValue': [value: string]
}>()

const open = ref(false)
const wrapperRef = ref<HTMLElement | null>(null)
const dropdownStyle = ref({})

const selectedLabel = computed(() => {
  return props.options.find(o => o.value === props.modelValue)?.label || ''
})

const select = (value: string) => {
  emit('update:modelValue', value)
  open.value = false
}

const positionDropdown = () => {
  if (!wrapperRef.value) return
  const rect = wrapperRef.value.getBoundingClientRect()
  dropdownStyle.value = {
    left: rect.left + 'px',
    top: rect.bottom + 'px',
    width: rect.width + 'px',
  }
}

watch(open, (val) => {
  if (val) {
    nextTick(positionDropdown)
  }
})

const onClickOutside = (e: MouseEvent) => {
  if (wrapperRef.value && !wrapperRef.value.contains(e.target as Node)) {
    open.value = false
  }
}

onMounted(() => {
  document.addEventListener('mousedown', onClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('mousedown', onClickOutside)
})
</script>