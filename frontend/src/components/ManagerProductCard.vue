<template>
  <div class="col mt-5">
    <div class="card" style="width: 18rem;">
      <img @click="alert(`Clicked ${title}`)" width="286" height="191" class="card-img-top" :src="imageURL" alt="Card image cap">
      <div class="card-body">
        <h5 @click="alert(`Clicked ${title}`)" data-toggle="tooltip" data-placement="bottom" :title="title" class="card-title">{{ title.slice(0, 20) + "..." }}</h5>
        <p>₹{{ price }}</p>
        <p class="quantity" v-if="getQuantity">Only {{ quantity}} stocks left!</p>
        <p class="quantity" v-if="outOfStock">out of stock!</p>
        <p @click="alert(`Clicked ${title}`)" class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <a class="btn btn-success">
          Edit
        </a>
        <a @click="deleteProduct" class="btn btn-success btn-danger">
          Delete
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

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
    fetchProducts(){
      axios.get("http://localhost:8000/manage_product",{
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
    deleteProduct: function(){
      axios.post("http://localhost:8000/delete_product",{
        product_id: this.product_id
      },{
        headers: {
          Authorization: `Bearer ${this.$store.state.user.access_token}`
        }
      }).then(resp => {
        console.log(resp)
        this.fetchProducts();
      }).catch(err => {
        console.log(err)
      })
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
.btn {
  margin: 1vh;
}
</style>
