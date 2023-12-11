import { createStore } from 'vuex'
// import Vue from 'vue';
// import Vuex from 'vuex';
// import createPersistedState from 'vuex-persistedstate';
//
// Vue.use(Vuex)
const store = createStore({
    // plugins: [createPersistedState()],
    state(){
        return {
            cartItem: 0
        }
    },
    getters: {

    },
    mutations: {
        increment(state){
            console.log(state.cartItem)
            state.cartItem++;
        }
    },
    actions: {

    },
    modules: {
    }
});
export default store;   