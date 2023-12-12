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
            <li class="list-group-item">CGST (8%) + SGST (8%): ₹{{ total.tax.toFixed(2) }}</li>
            <li class="list-group-item"><strong>Total: ₹{{ total.total.toFixed(2) }}</strong></li>
          </ul>
          <button class="btn btn-success btn-block mt-3">Checkout</button>
        </div>
      </div>
    </div>
  </div>
</div>
</template>


<script>
import CartCard from "@/components/CartCard.vue";
export default {
  name: "CartView",
  components:{
    CartCard
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
      let total = sub_total + (sub_total * 0.16);
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
