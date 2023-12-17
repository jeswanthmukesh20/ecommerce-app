import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate';
export default new createStore({
    plugins: [createPersistedState()],
    state(){
        return {
            cartItem: 0,
            cart: [],
            category: "All",
            user: {
                username: "",
                user_id: "",
                role: "",
                access_token: "",
                email: ""
            },
            products: [],
            orderId: ""
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
        },
        emptyCart(state){
            state.cart = []
            state.cartItem = 0
        },
        setCategory(state, category){
            state.category = category;
        },
        setProducts(state, products){
            state.products = products;
        },
        setOrder(state, orderId){
            state.orderId = orderId;
        }
    },
    actions: {
        setUser({ commit }, user) {
            commit('SET_USER', user);
        },
        emptyCart({ commit }) {
            commit("emptyCart");
        },
        SET_Products({ commit }, products){
            commit("setProducts", products)
        },
        setOrder({commit}, orderId){
            commit("setOrder", orderId);
        }
    },
    modules: {
    }
});