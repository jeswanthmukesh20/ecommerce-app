<template>
  <NabBar page="link" />
<!--  <div class="jumbotron jumbotron-fluid">-->
<!--    <div class="container">-->

<!--    </div>-->
<!--  </div>-->

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
              <img src="./assets/img/sort.png" height="24px" width="24px" alt="no sort"> Sort By
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
      <ProductCard v-for="product in products" :key="product.product_id" :price="product.price" :title="product.product_name" :imageURL="product.main_image" :product_id="product.product_id"/>
    </div>
  </div>
<!--  <div class="container">-->
<!--    <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">-->
<!--      <p class="col-md-4 mb-0 text-body-secondary">© 2023 Company, Inc</p>-->

<!--      <a href="#" class="col-md-4 d-flex a lign-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none">-->
<!--        <img class="bi me-2" src='./assets/Logo.png' width="182" height="42"/>-->
<!--      </a>-->

<!--      <ul class="nav col-md-4 justify-content-end">-->
<!--        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">Home</a></li>-->
<!--        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">Features</a></li>-->
<!--        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">Pricing</a></li>-->
<!--        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">FAQs</a></li>-->
<!--        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">About</a></li>-->
<!--      </ul>-->
<!--    </footer>-->
<!--  </div>-->
  <div id="footer" class="container">
    <footer class="py-3 my-4">
      <ul class="nav justify-content-center border-bottom pb-3 mb-3">
        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">Home</a></li>
        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">Features</a></li>
        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">Pricing</a></li>
        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">FAQs</a></li>
        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">About</a></li>
      </ul>
      <p class="text-center text-body-secondary">© 2023 Kirana Kart, Inc</p>
    </footer>
  </div>
</template>

<script>
import NabBar from "@/components/NavBar.vue";
import ProductCard from "@/components/ProductCard.vue";
import axios from "axios";
export default {
  name: 'App',
  components: {
    NabBar,
    ProductCard
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
#products, #footer{
  background-color: white;
}
#products {
  margin-top: 12rem;
}

</style>
