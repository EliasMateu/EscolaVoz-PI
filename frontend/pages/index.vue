<template>
  <div class="min-h-screen bg-white">
    <header class="fixed w-full bg-white shadow-sm z-50">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <div class="flex items-center">
            <span class="text-2xl font-bold text-primary-600">EscolaVoz</span>
          </div>
          <div class="hidden md:flex items-center space-x-8">
            <a href="#sobre" class="text-gray-700 hover:text-primary-600">Sobre</a>
            <a href="#funcionalidades" class="text-gray-700 hover:text-primary-600">Funcionalidades</a>
            <a href="#niveis" class="text-gray-700 hover:text-primary-600">Níveis de Acesso</a>
            <a href="#contato" class="text-gray-700 hover:text-primary-600">Contato</a>
            <NuxtLink to="/login" class="text-gray-700 hover:text-primary-600 font-medium">Login</NuxtLink>
            <NuxtLink to="/register" class="bg-primary-600 text-white px-4 py-2 rounded-md hover:bg-primary-700 font-medium">
              Cadastrar
            </NuxtLink>
          </div>
        </div>
      </nav>
    </header>

    <section class="relative bg-gradient-to-b from-primary-50 to-white pt-32 pb-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-6xl font-bold text-gray-900 mb-6">
          Sua voz na Educação
        </h1>
        <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
          Canal digital para registro de demandas escolares. Conectamos escolas e Direktorat de Ensino para uma educação melhor.
        </p>
        <div class="flex justify-center space-x-4">
          <NuxtLink to="/register" class="bg-primary-600 text-white px-8 py-3 rounded-lg text-lg font-medium hover:bg-primary-700">
            Cadastrar
          </NuxtLink>
          <NuxtLink to="/login" class="border-2 border-primary-600 text-primary-600 px-8 py-3 rounded-lg text-lg font-medium hover:bg-primary-50">
            Login
          </NuxtLink>
        </div>
      </div>
    </section>

    <section id="sobre" class="py-20 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold text-gray-900">Sobre o Projeto</h2>
        </div>
        <div class="grid md:grid-cols-3 gap-8">
          <div class="bg-white p-8 rounded-lg shadow-sm">
            <div class="text-primary-600 text-xl font-bold mb-4">O que é</div>
            <p class="text-gray-600">
              O EscolaVoz é um aplicativo web desenvolvido como Projeto Integrador na UNIVESP, permitindo que funcionários de escolas registrem demandas de forma organizada.
            </p>
          </div>
          <div class="bg-white p-8 rounded-lg shadow-sm">
            <div class="text-primary-600 text-xl font-bold mb-4">Objetivo</div>
            <p class="text-gray-600">
              Criar um canal digital que auxilie a SEDUC na priorização de investimentos por unidade escolar, gerando dados estruturados para tomada de decisão.
            </p>
          </div>
          <div class="bg-white p-8 rounded-lg shadow-sm">
            <div class="text-primary-600 text-xl font-bold mb-4">Público-alvo</div>
            <p class="text-gray-600">
              Escolas vinculadas à Diretoria de Ensino de Itapeva-SP, seus funcionários, diretores, e a própria Diretoria de Ensino e SEDUC.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section id="funcionalidades" class="py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold text-gray-900">Funcionalidades</h2>
        </div>
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div class="text-center">
            <div class="bg-primary-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Registro de Demandas</h3>
            <p class="text-gray-600 text-sm">Registre demandas de forma simples e categorizada</p>
          </div>
          <div class="text-center">
            <div class="bg-primary-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Categorização</h3>
            <p class="text-gray-600 text-sm">Organize demandas por categorias predefinidas</p>
          </div>
          <div class="text-center">
            <div class="bg-primary-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Dashboard Analítico</h3>
            <p class="text-gray-600 text-sm">Visualize dados e estatísticas em tempo real</p>
          </div>
          <div class="text-center">
            <div class="bg-primary-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Exportação de Dados</h3>
            <p class="text-gray-600 text-sm">Exporte dados em formato CSV para análise</p>
          </div>
        </div>
      </div>
    </section>

    <section id="niveis" class="py-20 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold text-gray-900">Níveis de Acesso</h2>
        </div>
        <div class="grid md:grid-cols-4 gap-6">
          <div class="bg-white p-6 rounded-lg shadow-sm border-t-4 border-blue-500">
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Funcionário</h3>
            <p class="text-gray-600 text-sm">Registra e gerencia demandas da própria escola</p>
          </div>
          <div class="bg-white p-6 rounded-lg shadow-sm border-t-4 border-green-500">
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Diretor</h3>
            <p class="text-gray-600 text-sm">Gerencia demandas e visualiza estatísticas da escola</p>
          </div>
          <div class="bg-white p-6 rounded-lg shadow-sm border-t-4 border-yellow-500">
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Diretoria</h3>
            <p class="text-gray-600 text-sm">Visualiza demandas da região e gerencia escolas</p>
          </div>
          <div class="bg-white p-6 rounded-lg shadow-sm border-t-4 border-red-500">
            <h3 class="text-lg font-semibold text-gray-900 mb-2">SEDUC</h3>
            <p class="text-gray-600 text-sm">Acesso completo a todas as escolas e categorias</p>
          </div>
        </div>
      </div>
    </section>

    <section id="contato" class="py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold text-gray-900">Contato</h2>
        </div>
        <div class="max-w-xl mx-auto text-center">
          <p class="text-gray-600 mb-8">
            Para dúvidas ou sugestões, entre em contato conosco:
          </p>
          <div class="space-y-4">
            <div class="flex items-center justify-center space-x-3">
              <svg class="w-6 h-6 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
              <span class="text-gray-700">contato@escolavicon.com.br</span>
            </div>
            <div class="flex items-center justify-center space-x-3">
              <svg class="w-6 h-6 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6.5v11a2 2 0 002 2h.982" />
              </svg>
              <span class="text-gray-700">(15) 1234-5678</span>
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
definePageMeta({
  layout: false
})
</script>