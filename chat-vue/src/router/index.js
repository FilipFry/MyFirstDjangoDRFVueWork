import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: HomeView,
      children:[
        {
          path: '',
          name: 'home',
          redirect: { name: 'chat-main' }
        },
        {
          path: 'chat',
          name: 'chat-main',
          component: () => import('../views/Chatwindow.vue'),
        },
        {
          path: 'profile/:id',
          name: 'profile',
          component: () => import('../views/Profile.vue'),
        }
      ]
    },
  ],
})

export default router

// path - адрес
// name - внутренне название пути типа переменная
// component - шаблон 
