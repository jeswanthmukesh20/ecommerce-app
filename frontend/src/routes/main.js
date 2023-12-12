import { createRouter, createWebHistory } from "vue-router"
import HomeView from "@/pages/HomeView.vue";
import ProfileView from "@/pages/ProfileView.vue";
import CartView from "@/pages/CartView.vue";
import LoginView from "@/pages/LoginView.vue";
import store from '../store/main'
import UnAuthorized from "@/pages/Unauthorized.vue";
import RegisterView from "@/pages/RegisterView.vue";
import Checkout from "@/pages/Checkout.vue";


const routes = [
    {
        path: '/',
        name: "Home",
        component: HomeView
    },
    {
        path: '/profile',
        name: "Profile",
        component: ProfileView
    },
    {
        path: '/cart',
        name: "Cart",
        component: CartView,
        meta: {
            requiresAuth: true,
            requiresUser: true
        },
    },
    {
        path: "/login",
        name: "Login",
        component: LoginView
    },
    {
        path: "/unauthorized",
        name: "Unauthorized",
        component: UnAuthorized
    },
    {
        path: "/register",
        name: "Register",
        component: RegisterView
    },
    {
        path: "/checkout",
        name: "Checkout",
        component: Checkout,
        meta: {
            requiresAuth: true,
            requiresUser: true
        }
    }

]

const router = createRouter({
    base:  "/",
    history: createWebHistory(),
    routes: routes,
});

router.beforeEach((to, from, next) => {
    const loggedIn = store.state.user.access_token
    const role = store.state.user.role
    if (to.matched.some(record => record.meta.requiresUser)) {
        if(!loggedIn || role !== "user"){
            next(loggedIn ? '/unauthorized' : '/login')
        } else{
            next()
        }
    }
    if (to.matched.some(record => record.meta.requiresAdmin)) {
        if (!loggedIn || role !== "admin") {

            next(loggedIn ? '/unauthorized' : '/login');
        } else {

            next();
        }
    } else {

        next();
    }
    if (to.matched.some(record => record.meta.requiresManager)) {
        if (!loggedIn || role !== "store manager") {

            next(loggedIn ? '/unauthorized' : '/login');
        } else {

            next();
        }
    } else {

        next();
    }
});


export default router;