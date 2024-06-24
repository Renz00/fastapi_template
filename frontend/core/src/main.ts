import 'primevue/resources/themes/aura-light-noir/theme.css';
import '/node_modules/primeflex/primeflex.css';
import 'primeicons/primeicons.css';
import '@/assets/main.css';


import { createApp } from 'vue';
import PrimeVue from 'primevue/config';
import { createPinia } from 'pinia';

import App from '@/App.vue';
import router from '@/router';

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(PrimeVue);

app.mount('#app');
