<template>
  <div class="flex items-center gap-2">
    <button
      @click="store.setLocale('pt-BR')"
      :class="[
        'px-2 py-1 text-sm rounded',
        store.locale === 'pt-BR' ? 'bg-primary-600 text-white' : 'text-gray-600 hover:bg-gray-100'
      ]"
    >
      PT
    </button>
    <button
      @click="store.setLocale('en')"
      :class="[
        'px-2 py-1 text-sm rounded',
        store.locale === 'en' ? 'bg-primary-600 text-white' : 'text-gray-600 hover:bg-gray-100'
      ]"
    >
      EN
    </button>
  </div>
</template>

<script setup lang="ts">
import { useThemeStore } from '~/composables/useTheme'
const store = useThemeStore()
</script>