import { createApp } from 'vue'
import App from './App.vue'
import store from './store/main.js'

createApp(App).use(store).mount('#app')
// app.use(store)