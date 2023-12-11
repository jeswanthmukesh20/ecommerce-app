<template>
  <div class="col mt-5">
    <div class="card" style="width: 18rem;">
      <img @click="alert(`Clicked ${title}`)" width="286" height="191" class="card-img-top" :src="require(`@/assets/img/${imageURL}`)" alt="Card image cap">
      <div class="card-body">
        <h5 @click="alert(`Clicked ${title}`)" data-toggle="tooltip" data-placement="bottom" :title="title" class="card-title">{{ title.slice(0, 20) + "..." }}</h5>
        <p>₹{{ price }}</p>
        <p @click="alert(`Clicked ${title}`)" class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <a @click="addCart" class="btn">
          <img src="../assets/img/add.png" height="42px" width="42px" alt="">
        </a>
        <a href="#" class="btn btn-success">Buy Now</a>
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
    }
  },
  methods: {
    alert: function (message){
      alert(message);
    },

    addCart(){
      this.$store.commit("addCart", {
        "product_id": this.product_id,
        "price": this.price,
      });
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
</style>
