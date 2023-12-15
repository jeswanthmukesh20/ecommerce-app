<template>
  <div v-if="getUser" id="products" class="container space-around p-5">
    <div  class="row justify-content-center ml-3 mb-3">
      <ProductCard
          v-for="product in getProducts"
          :key="product.product_id"
          :category="product.category"
          :price="product.price"
          :title="product.product_name"
          :imageURL="product.main_image"
          :product_id="product.product_id"
          :quantity="product.quantity"/>
    </div>
  </div>
  <div v-else-if="getManager" id="products" class="container space-around p-5">
    <ul class="nav">
      <li class="nav-item">
        <a data-toggle="modal" data-target="#exampleModal" class="nav-link btn btn-primary text-light" href="#">Add Product</a>
      </li>

    </ul>
    <div  class="row justify-content-center ml-3 mb-3">
      <ManagerProductCard
          v-for="product in getProducts"
          :key="product.product_id"
          :category="product.category"
          :price="product.price"
          :title="product.product_name"
          :imageURL="product.main_image"
          :product_id="product.product_id"
          :quantity="product.quantity"
      />
    </div>
<ModalForm/>

  </div>
</template>
<script>
import ProductCard from "@/components/ProductCard.vue";
import ManagerProductCard from "@/components/ManagerProductCard.vue";
import axios from "axios";
import ModalForm from "@/components/ModalForm.vue";


export default {
  name: "HomeView",
  components: {
    ModalForm,
    ProductCard,
    ManagerProductCard
  },
  data() {
    return {
      products: [],
      paths: {
        "user": '/shop',
        "store manager": "/manage_product",
        "admin": "/",
        "": '/shop'
      }
    }
  },
  mounted() {
    this.fetchProducts();
    console.log(this.$store.state.products)
    this.$store.commit("setCategory", "All");
    this.cartItem = this.$store.state.cartItem;
  },
  methods: {
    fetchProducts(){
      axios.get(`http://localhost:8000${this.paths[this.getRole]}`,{
        headers: {
          Authorization: `Bearer ${this.$store.state.user.access_token}`
        }
      }).then(res => {
        console.log(res)
        this.$store.dispatch("SET_Products", res.data);
      }).catch(err => {
        console.log(err)
        this.$store.dispatch("setUser", {
          username: "",
          user_id: "",
          role: "",
          access_token: "",
          email: ""
        })
        this.$router.push("/login")
      })
    },
  },
  computed: {
    cartItem() {
      return this.$store.state.cartItem;
    },
    getProducts(){

      let products = [];
      this.$store.state.products.forEach(product => {
        if(this.$store.state.category !== "All"){
          if(product.category === this.$store.state.category){
            products.push(product)
          }
        }else{
          products.push(product);
        }
      })
      return products;
    },
    getUser(){
      return this.$store.state.user.role === "user" || this.$store.state.user.role === "";
    },
    getManager(){
      return this.$store.state.user.role === "store manager"
    },
    getRole(){
      return this.$store.state.user.role;
    }
  }
}

</script>
<style scoped>
#products{
  background-color: white;
}
#products {
  margin-top: 12rem;
}
.nav-link {
  color: black
}
#dropdownMenuLink {
  color: black
}

.nav-link:hover {
  color: grey
}
#dropdownMenuLink:hover {
  color: grey
}
.box {
  width: 100%;
  height: 200px;
  background-color: #e9ecef;
}
#addProduct {
  height: 300px;
  width: 300px;
  background-color: white;
}
</style>