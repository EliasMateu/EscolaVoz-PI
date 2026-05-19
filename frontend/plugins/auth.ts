export default defineNuxtPlugin(async () => {
  if (import.meta.client) {
    const auth = useAuthStore()
    const accessToken = localStorage.getItem('accessToken')
    const refreshToken = localStorage.getItem('refreshToken')

    if (accessToken && refreshToken) {
      auth.accessToken = accessToken
      auth.refreshToken = refreshToken
      await auth.fetchUser()
    }
  }
})