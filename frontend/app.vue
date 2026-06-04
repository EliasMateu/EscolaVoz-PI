<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
import { useThemeStore } from '~/composables/useTheme'

const store = useThemeStore()

onMounted(() => {
  store.initTheme()
})

useHead({
  title: 'EscolaVoz',
})
</script>