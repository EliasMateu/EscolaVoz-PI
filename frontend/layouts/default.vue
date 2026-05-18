<template>
  <div class="min-h-screen bg-white dark:bg-gray-900 transition-colors">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { useThemeStore } from '~/composables/useTheme'

const store = useThemeStore()

onMounted(() => {
  store.initTheme()
})
</script>