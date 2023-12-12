<script setup>

</script>

<template>
<!-- Cart Items -->
<div class="container mt-5">
  <div class="row">
    <div class="col-lg-8">
      <h2>Your Cart</h2>
      <!-- Item 1 -->
      <div class="card mb-4">
        <div class="row no-gutters">
          <div class="col-md-4">
            <img src="item1.jpeg" class="card-img item-img" alt="Item 1">
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">Item 1</h5>
              <p class="card-text">Description of Item 1.</p>
              <p class="card-text"><strong>Price: $10.99</strong></p>
              <p class="card-text">Quantity: 2</p>
            </div>
          </div>
        </div>
      </div>
      <!-- Item 2 -->
      <div class="card mb-4">
        <div class="row no-gutters">
          <div class="col-md-4">
            <img src="item2.jpeg" class="card-img item-img" alt="Item 2">
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">Item 2</h5>
              <p class="card-text">Description of Item 2.</p>
              <p class="card-text"><strong>Price: $8.49</strong></p>
              <p class="card-text">Quantity: 3</p>
            </div>
          </div>
        </div>
      </div>
      <!-- Add more items similarly -->
      <!-- Item 3 -->
      <div class="card mb-4">
        <div class="row no-gutters">
          <div class="col-md-4">
            <img src="item1.jpeg" class="card-img item-img" alt="Item 3">
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">Item 3</h5>
              <p class="card-text">Description of Item 3.</p>
              <p class="card-text"><strong>Price: $5.99</strong></p>
              <p class="card-text">Quantity: 1</p>
            </div>
          </div>
        </div>
      </div>
      <!-- Item 4 -->
      <div class="card mb-4">
        <div class="row no-gutters">
          <div class="col-md-4">
            <img src="item2.jpeg" class="card-img item-img" alt="Item 4">
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">Item 4</h5>
              <p class="card-text">Description of Item 4.</p>
              <p class="card-text"><strong>Price: $12.49</strong></p>
              <p class="card-text">Quantity: 2</p>
            </div>
          </div>
        </div>
      </div>
      <!-- Add more items similarly -->
    </div>

    <!-- Total Bill -->
    <div class="col-lg-4">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Total Bill</h5>
          <ul class="list-group list-group-flush">
            <li class="list-group-item">Subtotal: $37.95</li>
            <li class="list-group-item">Tax (8%): $3.04</li>
            <li class="list-group-item"><strong>Total: $40.99</strong></li>
          </ul>
          <button class="btn btn-success btn-block mt-3">Checkout</button>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>
