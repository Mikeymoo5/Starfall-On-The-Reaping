import { createApp } from 'vue';;
import { createPinia } from 'pinia';

import 'vuetify/styles';
import '@mdi/font/css/materialdesignicons.css';

import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components'
import * as directives from 'vuetify/components'


import App from './App.vue';
import router from './router';

const pinia = createPinia()

const vuetify = createVuetify({
    components,
    directives,
});

const app = createApp(App);

app.use(router);
app.use(vuetify);
app.use(pinia);

app.mount('#app');

