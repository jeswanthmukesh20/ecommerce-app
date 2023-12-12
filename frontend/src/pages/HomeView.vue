<template>
  <div id="products" class="container space-around p-5">
    <nav class="navbar-light">
      <ul class="nav  justify-content-center mr-auto ml-auto ">
        <li class="nav-item">
          <a class="nav-link" href="#">Popularity</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Newest First</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Recommended</a>
        </li>
        <li class="nav-item dropdown">
          <div class="dropdown show">
            <a class="btn dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              <img src="../assets/img/sort.png" height="24px" width="24px" alt="no sort"> Sort By
            </a>

            <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
              <a class="dropdown-item" href="#">High to Low Price</a>
              <a class="dropdown-item" href="#">Low to High Price</a>
              <a class="dropdown-item" href="#">High to Low Rating</a>
              <a class="dropdown-item" href="#">Low to High Rating</a>
            </div>
          </div>
        </li>
      </ul>
    </nav>
    <hr style="width: 50%; border-radius: 6px; border-style: solid;">
    <div  class="row justify-content-center ml-3 mb-3">
      <ProductCard v-for="product in products" :key="product.product_id" :category="product.category" :price="product.price" :title="product.product_name" :imageURL="product.main_image" :product_id="product.product_id"/>
    </div>
  </div>

</template>
<script>
import ProductCard from "@/components/ProductCard.vue";
import axios from "axios";

export default {
  name: "HomeView",
  components: {
    ProductCard
  },
  data() {
    return {
      products: [],
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

</style>