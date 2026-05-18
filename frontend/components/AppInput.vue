<template>
  <div class="relative">
    <label v-if="label" :for="id" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">
      {{ label }}
      <span v-if="required" class="text-red-500">*</span>
    </label>
    <div class="relative">
      <input
        :id="id"
        v-model="model"
        :type="type"
        :placeholder="placeholder"
        :disabled="disabled"
        :readonly="readonly"
        :required="required"
        :class="inputClasses"
        @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
      />
      <div v-if="$slots.append" class="absolute inset-y-0 right-0 pr-3 flex items-center">
        <slot name="append" />
      </div>
    </div>
    <p v-if="error" class="mt-1.5 text-sm text-red-600 dark:text-red-400">{{ error }}</p>
    <p v-else-if="hint" class="mt-1.5 text-sm text-gray-500 dark:text-gray-400">{{ hint }}</p>
  </div>
</template>

<script setup lang="ts">
interface Props {
  modelValue?: string | number
  label?: string
  type?: string
  placeholder?: string
  disabled?: boolean
  readonly?: boolean
  required?: boolean
  error?: string
  hint?: string
  id?: string
}

const props = withDefaults(defineProps<Props>(), {
  type: 'text',
  disabled: false,
  readonly: false,
  required: false,
  id: () => `input-${Math.random().toString(36).substr(2, 9)}`,
})

const model = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
})

const emit = defineEmits(['update:modelValue'])

const inputClasses = computed(() => {
  const base = 'block w-full rounded-lg border bg-white dark:bg-gray-700 text-gray-900 dark:text-white transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-offset-0'
  
  const state = props.error
    ? 'border-red-300 dark:border-red-600 focus:border-red-500 focus:ring-red-500/20'
    : 'border-gray-300 dark:border-gray-600 focus:border-primary-500 focus:ring-primary-500/20'
  
  const disabled = props.disabled ? 'opacity-50 cursor-not-allowed bg-gray-100 dark:bg-gray-800' : ''
  
  const size = 'px-4 py-2.5 text-sm'
  
  const hasAppend = !!props.$slots.append ? 'pr-10' : ''
  
  return `${base} ${state} ${disabled} ${size} ${hasAppend}`
})
</script>