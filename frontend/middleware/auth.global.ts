export default defineNuxtRouteMiddleware((to) => {
  const auth = useAuthStore()
  
  const publicRoutes = ['/', '/login', '/register']
  
  if (!publicRoutes.includes(to.path) && !auth.isAuthenticated) {
    return navigateTo('/login')
  }
  
  if ((to.path === '/login' || to.path === '/register') && auth.isAuthenticated) {
    return navigateTo('/dashboard')
  }
})