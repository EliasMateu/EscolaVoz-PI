import { defineStore } from 'pinia'

export type Theme = 'light' | 'dark'
export type Locale = 'pt-BR' | 'en'

interface ThemeState {
  theme: Theme
  locale: Locale
}

export const useThemeStore = defineStore('theme', {
  state: () => ({
    theme: 'light' as Theme,
    locale: 'pt-BR' as Locale,
  }),

  actions: {
    toggleTheme() {
      this.theme = this.theme === 'light' ? 'dark' : 'light'
      this.applyTheme()
      localStorage.setItem('theme', this.theme)
    },

    setTheme(theme: Theme) {
      this.theme = theme
      this.applyTheme()
      localStorage.setItem('theme', this.theme)
    },

    applyTheme() {
      if (import.meta.client) {
        const html = document.documentElement
        if (this.theme === 'dark') {
          html.classList.add('dark')
        } else {
          html.classList.remove('dark')
        }
      }
    },

    setLocale(locale: Locale) {
      this.locale = locale
      localStorage.setItem('locale', locale)
    },

    initTheme() {
      if (import.meta.client) {
        const savedTheme = localStorage.getItem('theme') as Theme | null
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
        
        this.theme = savedTheme || (prefersDark ? 'dark' : 'light')
        this.applyTheme()

        const savedLocale = localStorage.getItem('locale') as Locale | null
        if (savedLocale) {
          this.locale = savedLocale
        }
      }
    },
  },
})

export const translations = {
  'pt-BR': {
    about: 'Sobre',
    features: 'Funcionalidades',
    accessLevels: 'Níveis de Acesso',
    contact: 'Contato',
    heroTitle: 'Sua voz na Educação',
    heroDesc: 'Canal digital para registro de demandas escolares. Conectamos escolas e Diretoria de Ensino para uma educação melhor.',
    aboutTitle: 'Sobre o Projeto',
    whatIs: 'O que é',
    whatIsDesc: 'O EscolaVoz é um aplicativo web desenvolvido como Projeto Integrador na UNIVESP, permitindo que funcionários de escolas registrem demandas de forma organizada.',
    goal: 'Objetivo',
    goalDesc: 'Criar um canal digital que auxilie a SEDUC na priorização de investimentos por unidade escolar, gerando dados estruturados para tomada de decisão.',
    target: 'Público-alvo',
    targetDesc: 'Escolas vinculadas à Diretoria de Ensino de Itapeva-SP, seus funcionários, diretores, e a própria Diretoria de Ensino e SEDUC.',
    featuresTitle: 'Funcionalidades',
    feature1Title: 'Registro de Demandas',
    feature1Desc: 'Registre demandas de forma simples e categorizada',
    feature2Title: 'Categorização',
    feature2Desc: 'Organize demandas por categorias predefinidas',
    feature3Title: 'Dashboard Analítico',
    feature3Desc: 'Visualize dados e estatísticas em tempo real',
    feature4Title: 'Exportação de Dados',
    feature4Desc: 'Exporte dados em formato CSV para análise',
    accessLevelsTitle: 'Níveis de Acesso',
    employee: 'Funcionário',
    employeeDesc: 'Registra e gerencia demandas da própria escola',
    principal: 'Diretor',
    principalDesc: 'Gerencia demandas e visualiza estatísticas da escola',
    directory: 'Diretoria',
    directoryDesc: 'Visualiza demandas da região e gerencia escolas',
    seducDesc: 'Acesso completo a todas as escolas e categorias',
    contactTitle: 'Contato',
    contactDesc: 'Para dúvidas ou sugestões, entre em contato conosco:',
    login: 'Entrar',
    register: 'Cadastrar',
    logout: 'Sair',
    dashboard: 'Dashboard',
    newDemand: 'Nova Demanda',
    myDemands: 'Minhas Demandas',
    total: 'Total',
    pending: 'Pendentes',
    inProgress: 'Em Andamento',
    completed: 'Concluídas',
    categories: 'Categorias',
    schools: 'Escolas',
    priority: 'Prioridade',
    status: 'Status',
    title: 'Título',
    description: 'Descrição',
    save: 'Salvar',
    cancel: 'Cancelar',
    back: 'Voltar',
    export: 'Exportar CSV',
    admin: 'Admin',
    profile: 'Perfil',
    settings: 'Configurações',
    school: 'Escola',
    low: 'Baixa',
    medium: 'Média',
    high: 'Alta',
    urgent: 'Urgente',
    noDemands: 'Nenhuma demanda cadastrada',
  },
  'en': {
    about: 'About',
    features: 'Features',
    accessLevels: 'Access Levels',
    contact: 'Contact',
    heroTitle: 'Your Voice in Education',
    heroDesc: 'Digital channel for school demand registration. We connect schools and Education Directorate for better education.',
    aboutTitle: 'About the Project',
    whatIs: 'What it is',
    whatIsDesc: 'EscolaVoz is a web application developed as an Integrated Project at UNIVESP, allowing school employees to register demands in an organized way.',
    goal: 'Goal',
    goalDesc: 'Create a digital channel to help SEDUC prioritize investments per school, generating structured data for decision making.',
    target: 'Target Audience',
    targetDesc: 'Schools linked to the Education Directorate of Itapeva-SP, their employees, directors, and the Education Directorate itself.',
    featuresTitle: 'Features',
    feature1Title: 'Demand Registration',
    feature1Desc: 'Register demands simply and categorized',
    feature2Title: 'Categorization',
    feature2Desc: 'Organize demands by predefined categories',
    feature3Title: 'Analytics Dashboard',
    feature3Desc: 'View data and statistics in real time',
    feature4Title: 'Data Export',
    feature4Desc: 'Export data in CSV format for analysis',
    accessLevelsTitle: 'Access Levels',
    employee: 'Employee',
    employeeDesc: 'Register and manage demands for their school',
    principal: 'Principal',
    principalDesc: 'Manage demands and view school statistics',
    directory: 'Directory',
    directoryDesc: 'View regional demands and manage schools',
    seducDesc: 'Full access to all schools and categories',
    contactTitle: 'Contact',
    contactDesc: 'For questions or suggestions, contact us:',
    login: 'Login',
    register: 'Register',
    logout: 'Logout',
    dashboard: 'Dashboard',
    newDemand: 'New Demand',
    myDemands: 'My Demands',
    total: 'Total',
    pending: 'Pending',
    inProgress: 'In Progress',
    completed: 'Completed',
    categories: 'Categories',
    schools: 'Schools',
    priority: 'Priority',
    status: 'Status',
    title: 'Title',
    description: 'Description',
    save: 'Save',
    cancel: 'Cancel',
    back: 'Back',
    export: 'Export CSV',
    admin: 'Admin',
    profile: 'Profile',
    settings: 'Settings',
    school: 'School',
    low: 'Low',
    medium: 'Medium',
    high: 'High',
    urgent: 'Urgent',
    noDemands: 'No demands registered',
  },
}

export function useTrans(key: string): string {
  const store = useThemeStore()
  return translations[store.locale][key as keyof typeof translations['pt-BR']] || key
}