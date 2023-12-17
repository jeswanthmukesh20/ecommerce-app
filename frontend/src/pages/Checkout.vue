<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card">
          <div class="card-header bg-success text-white">
            <h2>Checkout Complete</h2>
          </div>
          <div class="card-body">
            <p class="lead">Thank you for shopping with us!</p>
            <p>Your order has been successfully processed.</p>
            <p>Your Order id: {{getOrder}}.</p>
            <a href="/" class="btn btn-primary">Continue Shopping</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "CheckoutView",
  computed: {
    getOrder(){
      return this.$store.state.orderId
    }
  }
}
</script>

<style scoped>
.container {
  margin-top: 10rem;
}
</style>