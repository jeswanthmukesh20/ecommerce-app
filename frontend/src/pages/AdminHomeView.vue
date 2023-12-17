<template>
  <!-- Cart Items -->
  <div class="container">
      <div class="container">
        <h1>Users</h1>
        <table class="table">
          <thead>
          <tr>

            <th scope="col">username</th>
            <th scope="col">Email</th>
            <th scope="col">Role</th>
            <th scope="col">Action</th>
          </tr>
          </thead>
          <tbody>
          <TableRow v-for="user in users"
                    :key="user.user_id"
                    :username="user.username"
                    :email="user.email"
                    :role="user.role"
                    :user-id="user.user_id"
                    @deleteUser="deleteUser"
          />
          </tbody>
        </table>
      </div>



    <div class="container">
      <h1>Categories</h1>
        <table class="table">
          <thead>
          <tr>
            <th scope="col">Category Name</th>
            <th scope="col">Requested User</th>
            <th scope="col">Status</th>
            <th scope="col">Action</th>
          </tr>
          </thead>
          <tbody>
          <CategoryRow v-for="category in categories"
                       :key="category.id"
                       :status="category.status"
                       :user="category.username"
                       :name="category.category_name"
                       :categoryId="category.id"
                       @setAction="setAction"
          />
          </tbody>
        </table>
      </div>
  </div>
</template>


<script>
import axios from "axios";
import TableRow from "@/components/TableRow.vue";
import CategoryRow from "@/components/CategoryRow.vue";
export default {
  name: "AdminHomeView",
  components:{
    TableRow,
    CategoryRow
  },
  data(){
    return {
      users: [],
      categories: []
    }
  },
  mounted(){
    this.fetchUsers()
    this.fetchCategories()
  },
  methods: {
    deleteUser: function(userId){
      axios.post("http://localhost:8000/admin", {
        user_id: userId
      },{
        headers: {
          Authorization: `Bearer ${this.$store.state.user.access_token}`
        }
      }).then(resp => {
        console.log(resp)
      }).catch(err => {
        console.log(err)
      })
    },
    fetchUsers(){
      axios.get("http://localhost:8000/admin", {
        headers: {
          Authorization: `Bearer ${this.$store.state.user.access_token}`
        }
      }).then(resp => {
        this.users = resp.data
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
    fetchCategories(){
      axios.get("http://localhost:8000/admin/category", {
        headers: {
          Authorization: `Bearer ${this.$store.state.user.access_token}`
        }
      }).then(resp => {
        this.categories = resp.data
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
    setAction(categoryId){
      axios.post("http://localhost:8000/admin/category", {
        category_id: categoryId
      },{
        headers: {
          Authorization: `Bearer ${this.$store.state.user.access_token}`
        }
      }).then(resp => {
        this.categories = resp.data
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
    }
  },
  computed: {

  }
}
</script>

<style scoped>
.container {
  margin-top: 8rem;
  background-color: white;
  margin-bottom: 3rem;
  padding: 2rem;
}
.table {
  margin-top: 2rem;
}
</style>
