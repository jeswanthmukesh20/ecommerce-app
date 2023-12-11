import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate';
export default new createStore({
    plugins: [createPersistedState()],
    state(){
        return {
            cartItem: 0,
            cart: [],
            user: {
                username: "",
                user_id: "",
                is_admin: false,
                token: ""
            }
        }
    },
    getters: {
        getUser: state => state.user
    },
    mutations: {
        addCart(state, payload){
            state.cartItem++;

                let present = false;
                state.cart.forEach(product => {
                    if(product.product_id === payload.product_id){
                        product.quantity++;
                        present = true;
                        console.log(true)
                    }
                })
                if(!present){
                    payload.quantity = 1;
                    state.cart.push(payload)
                }

            console.log(state.cart)
        },
        SET_USER(state, user) {
            state.user = user;
        }
    },
    actions: {
        setUser({ commit }, user) {
            commit('SET_USER', user);
        }
    },
    modules: {
    }
});