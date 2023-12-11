import { createStore } from 'vuex'

export default new createStore({
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