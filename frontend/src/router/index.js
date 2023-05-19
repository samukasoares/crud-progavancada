import Vue from 'vue';
import Router from 'vue-router';
import create from '@/components/create';
import alterar from '@/components/alterar'
import VueResource from 'vue-resource';
import list from '@/components/list'

Vue.use(VueResource);
Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'list',
      component: list,
    },
    {
      path: '/list',
      name: 'list',
      component: list,
    },
    {
      path: '/create',
      name: 'create',
      component: create
    },
    {
      path: '/alterar',
      name: 'alterar',
      component: alterar
    }
  ],
});