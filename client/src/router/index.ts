import { createRouter, createWebHistory } from 'vue-router'

import LoginView from "../views/LoginView.vue";
import SignupView from "../views/SignupView.vue";
import HomeView from "../views/HomeView.vue";
import AccountView from '@/views/AccountView.vue';
import SponsorPersonView from '@/views/SponsorPersonView.vue';

const routes = [
  { path: '/', component: HomeView},
  { path: '/login', component: LoginView},
  { path: '/signup', component: SignupView},
  { path: '/account', component: AccountView},
  { path: '/sponsor/:id', component: SponsorPersonView}
]
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
