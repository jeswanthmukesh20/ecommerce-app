import { createApp } from 'vue'
import App from './App.vue'
import store from './store/main.js'
import router from "@/routes/main";

createApp(App).use(store).use(router).mount('#app');