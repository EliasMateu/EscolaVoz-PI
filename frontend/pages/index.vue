<template>
  <div class="min-h-screen bg-white dark:bg-gray-900 transition-colors">
    <header class="fixed w-full bg-white dark:bg-gray-900 shadow-sm z-50 border-b dark:border-gray-800">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <div class="flex items-center">
            <span class="text-2xl font-bold text-primary-600">EscolaVoz</span>
          </div>
          <div class="hidden md:flex items-center space-x-8">
            <a href="#sobre" class="text-gray-700 dark:text-gray-300 hover:text-primary-600">{{ t('about') }}</a>
            <a href="#funcionalidades" class="text-gray-700 dark:text-gray-300 hover:text-primary-600">{{ t('features') }}</a>
            <a href="#niveis" class="text-gray-700 dark:text-gray-300 hover:text-primary-600">{{ t('accessLevels') }}</a>
            <a href="#contato" class="text-gray-700 dark:text-gray-300 hover:text-primary-600">{{ t('contact') }}</a>
            <div class="flex items-center gap-3 border-l pl-4 border-gray-300 dark:border-gray-700">
              <LocaleToggle />
              <ThemeToggle />
            </div>
            <NuxtLink to="/login" class="text-gray-700 dark:text-gray-300 hover:text-primary-600 font-medium">{{ t('login') }}</NuxtLink>
            <NuxtLink to="/register" class="bg-primary-600 text-white px-4 py-2 rounded-md hover:bg-primary-700 font-medium">
              {{ t('register') }}
            </NuxtLink>
          </div>
        </div>
      </nav>
    </header>

    <section class="relative bg-gradient-to-b from-primary-50 to-white dark:from-gray-800 dark:to-gray-900 pt-32 pb-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-6xl font-bold text-gray-900 dark:text-white mb-6">
          {{ t('heroTitle') }}
        </h1>
        <p class="text-xl text-gray-600 dark:text-gray-300 mb-8 max-w-2xl mx-auto">
          {{ t('heroDesc') }}
        </p>
        <div class="flex justify-center space-x-4">
          <NuxtLink to="/register" class="bg-primary-600 text-white px-8 py-3 rounded-lg text-lg font-medium hover:bg-primary-700">
            {{ t('register') }}
          </NuxtLink>
          <NuxtLink to="/login" class="border-2 border-primary-600 text-primary-600 dark:text-primary-400 px-8 py-3 rounded-lg text-lg font-medium hover:bg-primary-50 dark:hover:bg-gray-800">
            {{ t('login') }}
          </NuxtLink>
        </div>
      </div>
    </section>

    <section id="sobre" class="py-20 bg-gray-50 dark:bg-gray-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold text-gray-900 dark:text-white">{{ t('aboutTitle') }}</h2>
        </div>
        <div class="grid md:grid-cols-3 gap-8">
          <div class="bg-white dark:bg-gray-700 p-8 rounded-lg shadow-sm">
            <div class="text-primary-600 text-xl font-bold mb-4">{{ t('whatIs') }}</div>
            <p class="text-gray-600 dark:text-gray-300">
              {{ t('whatIsDesc') }}
            </p>
          </div>
          <div class="bg-white dark:bg-gray-700 p-8 rounded-lg shadow-sm">
            <div class="text-primary-600 text-xl font-bold mb-4">{{ t('goal') }}</div>
            <p class="text-gray-600 dark:text-gray-300">
              {{ t('goalDesc') }}
            </p>
          </div>
          <div class="bg-white dark:bg-gray-700 p-8 rounded-lg shadow-sm">
            <div class="text-primary-600 text-xl font-bold mb-4">{{ t('target') }}</div>
            <p class="text-gray-600 dark:text-gray-300">
              {{ t('targetDesc') }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <section id="funcionalidades" class="py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold text-gray-900 dark:text-white">{{ t('featuresTitle') }}</h2>
        </div>
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div class="text-center">
            <div class="bg-primary-100 dark:bg-primary-900/30 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600 dark:text-primary-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">{{ t('feature1Title') }}</h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm">{{ t('feature1Desc') }}</p>
          </div>
          <div class="text-center">
            <div class="bg-primary-100 dark:bg-primary-900/30 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600 dark:text-primary-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">{{ t('feature2Title') }}</h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm">{{ t('feature2Desc') }}</p>
          </div>
          <div class="text-center">
            <div class="bg-primary-100 dark:bg-primary-900/30 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600 dark:text-primary-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">{{ t('feature3Title') }}</h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm">{{ t('feature3Desc') }}</p>
          </div>
          <div class="text-center">
            <div class="bg-primary-100 dark:bg-primary-900/30 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600 dark:text-primary-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">{{ t('feature4Title') }}</h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm">{{ t('feature4Desc') }}</p>
          </div>
        </div>
      </div>
    </section>

    <section id="niveis" class="py-20 bg-gray-50 dark:bg-gray-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold text-gray-900 dark:text-white">{{ t('accessLevelsTitle') }}</h2>
        </div>
        <div class="grid md:grid-cols-4 gap-6">
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-sm border-t-4 border-blue-500">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">{{ t('employee') }}</h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm">{{ t('employeeDesc') }}</p>
          </div>
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-sm border-t-4 border-green-500">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">{{ t('principal') }}</h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm">{{ t('principalDesc') }}</p>
          </div>
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-sm border-t-4 border-yellow-500">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">{{ t('directory') }}</h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm">{{ t('directoryDesc') }}</p>
          </div>
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-sm border-t-4 border-red-500">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">SEDUC</h3>
            <p class="text-gray-600 dark:text-gray-400 text-sm">{{ t('seducDesc') }}</p>
          </div>
        </div>
      </div>
    </section>

    <section id="contato" class="py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold text-gray-900 dark:text-white">{{ t('contactTitle') }}</h2>
        </div>
        <div class="max-w-xl mx-auto text-center">
          <p class="text-gray-600 dark:text-gray-400 mb-8">
            {{ t('contactDesc') }}
          </p>
          <div class="space-y-4">
            <div class="flex items-center justify-center space-x-3">
              <svg class="w-6 h-6 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
              <span class="text-gray-700 dark:text-gray-300">contato@escolavicon.com.br</span>
            </div>
            <div class="flex items-center justify-center space-x-3">
              <svg class="w-6 h-6 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6.5v11a2 2 0 002 2h.982" />
              </svg>
              <span class="text-gray-700 dark:text-gray-300">(15) 1234-5678</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <footer class="bg-gray-900 text-white py-8">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row justify-between items-center">
          <div class="mb-4 md:mb-0">
            <span class="text-xl font-bold">EscolaVoz</span>
            <p class="text-gray-400 text-sm">Projeto Integrador - UNIVESP</p>
          </div>
          <div class="text-gray-400 text-sm">
            © 2026 EscolaVoz. Todos os direitos reservados.
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { useThemeStore, translations } from '~/composables/useTheme'

definePageMeta({
  layout: false
})

const store = useThemeStore()

onMounted(() => {
  store.initTheme()
})

const t = (key: string) => translations[store.locale][key as keyof typeof translations['pt-BR']] || key
</script>