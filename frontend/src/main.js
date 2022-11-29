import { createApp } from 'vue'
import Vue3EasyDataTable from 'vue3-easy-data-table';
import BootstrapVue3 from 'bootstrap-vue-3'
import App from './App.vue'
import router from './router'

import 'vue3-easy-data-table/dist/style.css';
//import './assets/simple-grid.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

const app = createApp(App)
app.component('EasyDataTable', Vue3EasyDataTable);
app.use(BootstrapVue3)
app.use(router)


app.mount('#app')
