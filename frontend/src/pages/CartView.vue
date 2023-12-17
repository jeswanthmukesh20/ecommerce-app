<template>
<!-- Cart Items -->
<div class="container">
  <div class="row">
    <div class="col-lg-8">
      <h2>Your Cart</h2>
      <!-- Item 1 -->
      <CartCard v-for="product in products"
                :title="product.product_name"
                :imageURL="product.imageURL"
                :key="product.product_id"
                :product_id="product.product_id"
                :category="product.category"
                :price="product.price"
                :quantity="product.quantity"/>

      <!-- Add more items similarly -->
    </div>

    <!-- Total Bill -->
    <div class="col-lg-4">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Total Bill</h5>
          <ul class="list-group list-group-flush">
            <li class="list-group-item">Subtotal: ₹{{ total.sub_total }}</li>
            <li class="list-group-item">CGST (9%) + SGST (9%): ₹{{ total.tax.toFixed(2) }}</li>
            <li class="list-group-item"><strong>Total: ₹{{ total.total.toFixed(2) }}</strong></li>
          </ul>
          <button @click="checkout" class="btn btn-success btn-block mt-3">Checkout</button>
        </div>
      </div>
    </div>
  </div>
</div>
</template>


<script>
import CartCard from "@/components/CartCard.vue";
import axios from "axios";
export default {
  name: "CartView",
  components:{
    CartCard
  },
  mounted(){
    axios.get("http://localhost:8000/user_actions", {
      headers: {
        Authorization: `Bearer ${this.$store.state.user.access_token}`
      }
    }).then(resp => {
      console.log(resp)
    }).catch(err => {
      this.$store.dispatch("setUser", {
        username: "",
        user_id: "",
        role: "",
        access_token: ""
      })
      this.$router.push({path: "/login", next: "/cart"})
      console.log(err)
    })
  },
  methods: {
    checkout: function() {

      let config = {
        headers: {
          Authorization: `Bearer ${this.$store.state.user.access_token}`
        }
      }
      console.log(config)
      axios.post("http://localhost:8000/user_actions", {
        orders: this.$store.state.cart
      }, config).then(resp => {
        console.log(resp)
        this.$store.dispatch("setOrder", resp.data.order_id)
      }).catch(err => {
        console.log(err.response.status)
      })
      this.$store.dispatch("emptyCart");
      this.$router.push('/checkout')
    }
  },
  computed: {
    products(){
      return this.$store.state.cart
    },
    total(){
      let sub_total = 0;
      this.$store.state.cart.forEach(product => {
        sub_total += (product.quantity * product.price);
      })
      let total = sub_total + (sub_total * 0.18);
      return {
        total: total,
        tax: total - sub_total,
        sub_total: sub_total
      }
    }
  }
}
</script>

<style scoped>
.container {
  margin-top: 8rem;
  background-color: white;
  margin-bottom: 3rem;
  padding: 3rem;
}
.col-lg-4 {
  margin-top: 3rem;
}
</style>
