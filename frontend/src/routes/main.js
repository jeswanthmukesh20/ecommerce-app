import { createRouter, createWebHistory } from "vue-router"
import HomeView from "@/pages/HomeView.vue";
import ProfileView from "@/pages/ProfileView.vue";
import CartView from "@/pages/CartView.vue";
import LoginView from "@/pages/LoginView.vue";
import store from '../store/main'
import UnAuthorized from "@/pages/Unauthorized.vue";
import RegisterView from "@/pages/RegisterView.vue";
import CheckoutView from "@/pages/Checkout.vue";
import UserProfile from "@/pages/UserProfile.vue";


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
        component: CheckoutView,
        meta: {
            requiresAuth: true,
            requiresUser: true
        }
    },
    {
        path: "/profile",
        name: "Profile",
        component: UserProfile,
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
        if(!loggedIn && role !== "user"){
            next('/login')
        }
        else{
            next()
        }
    }else if(to.matched.some(record => record.meta.requiresManager)){
        if(!loggedIn && role !== "store manager"){
            next("/login")
        }else{
            next()
        }
    }else if(to.matched.some(record => record.meta.requiresAdmin)){
        if(!loggedIn && role !== "admin"){
            next("/login")
        }else{
            next()
        }
    }else{
        next()
    }

});


export default router;