<template>
  <div class="col mt-5">
    <div class="card" style="width: 18rem;">
      <img @click="alert(`Clicked ${title}`)" width="286" height="191" class="card-img-top" :src="require(`@/assets/img/${imageURL}`)" alt="Card image cap">
      <div class="card-body">
        <h5 @click="alert(`Clicked ${title}`)" data-toggle="tooltip" data-placement="bottom" :title="title" class="card-title">{{ title.slice(0, 20) + "..." }}</h5>
        <p>₹{{ price }}</p>
        <p class="quantity" v-if="getQuantity">Only {{ quantity}} stocks left!</p>
        <p class="quantity" v-if="outOfStock">out of stock!</p>
        <p @click="alert(`Clicked ${title}`)" class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <a v-if="!outOfStock" @click="addCart" class="btn btn-success">
          <img src="../assets/img/add.png" height="18px" width="18px" alt="">
          Add to Cart
        </a>
        <a v-else  class="btn btn-success disabled">
          <img src="../assets/img/add.png" height="18px" width="18px" alt="">
          Add to Cart
        </a>
<!--        <a href="#" class="btn btn-success">Add to Cart</a>-->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductCard",
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
  },
  methods: {
    alert: function (message){
      alert(message);
    },

    addCart(){
      let limitExceeded = false;
      this.$store.state.cart.forEach(product => {
        if((product.quantity + 1) > this.quantity && product.product_id === this.product_id){
          limitExceeded = true;
        }
      })
      if(!limitExceeded){
        this.$store.commit("addCart", {
          product_id: this.product_id,
          price: this.price,
          imageURL: this.imageURL,
          product_name: this.title,
          category: this.category
        });
      }else{
        alert("Maximum buy limit for this product is reached")
      }
    }
  },
  computed: {
    getQuantity(){
      return this.quantity <= 10 && this.quantity !== 0;
    },
    outOfStock(){
      return this.quantity === 0;
    }
  }
}
</script>
<style>
.card-img-top {
  object-fit: cover;

}
.card:hover {
  box-shadow: 10px 5px 35px  rgba(104,104,104,0.33);
}
.btn-success{
  font-weight: bold;
  align-content: center;
}
.quantity {
  color: orangered;
  font-weight: bold;
}
</style>
