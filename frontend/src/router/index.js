import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LogView from '../views/LogView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/logs',
      name: 'logs',
      component: LogView
    },
    {
      path: '/:pathMatch(.*)',
      redirect: "/"
    }
  ]
})

export default router
