<template>
  <div class="card mb-4">
    <div class="row no-gutters">
      <div class="col-md-4">
        <img width="286" height="191" :src="imageURL" class="card-img item-img" alt="Item 1">
      </div>
      <div class="col-md-8">
        <div class="card-body">
          <h5 class="card-title">{{ title }}</h5>
          <p class="card-text">Description of Item 1.</p>
          <p class="card-text"><strong>Price: ₹{{ price }}</strong></p>
          <p class="card-text">Quantity: {{ quantity }}</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "CartCard",
  props: {
    imageURL: {
      type: String,
      default: ""
    },
    title: {
      type: String,
      default: "Product"
    },
    price: {
      type: Number
    },
    product_id: {
      type: String
    },
    category: {
      type: String
    },
    quantity: {
      type: Number
    }
  }
}
</script>

<style scoped>

.card-img {
  object-fit: cover;

}
.card:hover {
  box-shadow: 10px 5px 35px  rgba(104,104,104,0.33);
}
</style>