import { createApp } from 'vue'
import App from './App.vue'
import store from './store/main'

const app = createApp(App).mount('#app')
app.use(store);
// app.use(store)