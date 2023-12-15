<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 offset-md-3">
        <h2>User Profile</h2>
        <hr>

        <div>
          <h4>User Information</h4>
          <p><strong>Username:</strong> <span id="username">{{ $store.state.user.username }}</span></p>
          <p><strong>Email:</strong> <span id="email">{{ $store.state.user.email }}</span></p>
        </div>
        <hr>

        <div>
          <h4>Update Information</h4>
          <form id="updateForm">
            <div class="mb-3">
              <label for="newUsername" class="form-label">New Username</label>
              <input v-model="username" type="text" class="form-control" id="newUsername">
            </div>
            <div class="mb-3">
              <label for="newEmail" class="form-label">New Email</label>
              <input v-model="email" type="email" class="form-control" id="newEmail">
            </div>
            <div class="mb-3">
              <label for="newPassword" class="form-label">New Password</label>
              <input v-model="password" type="password" class="form-control" id="newPassword">
            </div>
          </form>
          <button @click="submit" type="submit" class="btn btn-primary">Update</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

import axios from "axios";
export default {
  name: "UserProfile",
  data(){
    return {
      username: "",
      email: "",
      password: ""
    }
  },
  methods: {
    submit: function(){
      axios.put("http://localhost:8000/user_actions", {
        username: this.username,
        email: this.email,
        password: this.password
      }, {
        headers: {
          Authorization: `Bearer ${this.$store.state.user.access_token}`
        }
      }).then(resp => {
        console.log(resp)
        axios.get("http://localhost:8000/user_actions", {
          headers: {
            Authorization: `Bearer ${this.$store.state.user.access_token}`
          }
        }).then(resp => {
          console.log(resp)
          let user = resp.data;
          user.access_token = this.$store.state.user.access_token
          this.$store.dispatch("setUser", user)
        }).catch(err => {
          console.log(err);
          this.$router.push("/login")
        })
      }).catch(err => {
        console.log(err)
        this.$router.push("/login")
      })
    }
  }
}
</script>

<style scoped>
.container {
  background-color: white;
  margin-top: 10rem;
  padding: 3rem;
}
</style>