<template>
  <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Add Product</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form>
            <div class="form-group">
              <label for="productImage">Product Image:</label>
              <input @change="onChange" type="file" name="product_image" class="form-control-file" id="productImage" accept="image/*" required>
            </div>
            <div class="form-group">
              <label for="productName">Product Name:</label>
              <input v-model="name" type="text" class="form-control" id="productName" placeholder="Enter product name" required>
            </div>
            <div class="form-group">
              <label for="productPrice">Price:</label>
              <input v-model="cost" type="number" class="form-control" id="productPrice" placeholder="Enter price" required>
            </div>
            <div class="form-group">
              <label for="productQuantity">Quantity:</label>
              <input v-model="productCount" type="number" class="form-control" id="productQuantity" placeholder="Enter quantity" required>
            </div>
            <div class="form-group">
              <label  for="productCategory">Category:</label>
              <select v-model="productCategory" class="form-control" id="productCategory" required>
                <option selected value="Grocery">Grocery</option>
                <option value="Vegetables">Vegetables</option>
                <option value="Cleaners">Cleaners</option>
              </select>
            </div>
            <div class="form-group">
              <label for="newCategory">Or request a new category:</label>
              <input v-model="requestedCategory" type="text" class="form-control" id="newCategory" placeholder="Enter new category">
            </div>

          </form>
        </div>
        <div class="modal-footer">
          <button @click="submitForm" type="submit" class="btn btn-primary">Add Product</button>
          <button @click="submitForm" type="button" class="btn btn-info ml-2" data-toggle="modal" data-target="#requestCategoryModal">Request New Category</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "ModalForm",
  data(){
    return {
        name: '',
        productCount: 1,
        cost: 0.0,
        productCategory: '',
        image: null,
        requestedCategory: ''

    }
  },
  methods: {
    fetchProducts(){
      axios.get("http://localhost:8000/manage_product",{
        headers: {
          Authorization: `Bearer ${this.$store.state.user.access_token}`
        }
      }).then(res => {
        console.log(res)
        this.$store.dispatch("SET_Products", res.data.products);
        this.$store.dispatch("setCategories", res.data.categories);
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
    submitForm:function() {
      console.log(this.imageFile)
      let form = new FormData();
      form.append("product_name", this.name)
      form.append("quantity", this.productCount)
      form.append("category", this.productCategory)
      form.append("price", this.cost)
      form.append("product_image", this.imageFile)
      form.append("requested_category", this.requestedCategory)
      console.log(form)
      axios.post('http://localhost:8000/manage_product', form, {
        headers: {
          Authorization: `Bearer ${this.$store.state.user.access_token}`,
          'Content-Type': 'multipart/form-data'
        }
      }).then(resp => {
        console.log(resp)
        this.fetchProducts();
      }).catch(err => {
        console.log(err)
        this.$router.push("/login")
      })
    },
    onChange: function(e){
      const file = e.target.files[0];
      console.log(file)
      if (file) {
        this.image = file;
      }
    },
  },
  computed: {
    imageFile(){
      return this.image

    }
  }
}
</script>
