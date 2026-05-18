export default defineNuxtRouteMiddleware((to) => {
  if (!import.meta.client) return
  
  const auth = useAuthStore()
  
  const publicRoutes = ['/', '/login', '/register']
  
  if (!publicRoutes.includes(to.path) && !auth.isAuthenticated) {
    return navigateTo('/login')
  }
  
  if ((to.path === '/login' || to.path === '/register') && auth.isAuthenticated) {
    return navigateTo('/dashboard')
  }
})