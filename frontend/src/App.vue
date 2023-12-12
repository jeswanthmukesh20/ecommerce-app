<template>
  <NabBar page="link" />
  <HomeView/>
  <FooterComponent/>
</template>

<script>
import NabBar from "@/components/NavBar.vue";
import FooterComponent from "@/components/Footer.vue";
import HomeView from "@/pages/HomeView.vue";

import axios from "axios";
export default {
  name: 'App',
  components: {
    NabBar,
    FooterComponent,
    HomeView

  },
  data() {
    return {
      products: [],
      // cartItem: 0
    }
  },
  mounted() {
    // Fetch product data using Axios when the component is mounted
    this.fetchProducts();
    this.cartItem = this.$store.state.cartItem;
    console.log(this.cartItem, "cartItem")
    console.log(this.$store.state.cart, "cart")
  },
  methods: {
    fetchProducts(){
      axios.get("http://localhost:8000/shop").then(res => {
        console.log(res)
        this.products = res.data;
      }).catch(err => {
        console.log(err)
      })
    },
  },
  computed: {
    cartItem() {
      return this.$store.state.cartItem;
    }
  }
}
</script>
<style>


</style>
