export default defineNuxtPlugin(() => {
  if (import.meta.client) {
    const auth = useAuthStore()
    auth.initAuth()
  }
})