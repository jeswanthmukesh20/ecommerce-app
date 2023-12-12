<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 offset-md-3">
        <div class="registration-form">
          <h2>Register</h2>
          <form>
            <div class="form-group">
              <label for="username">Username</label>
              <input v-model="username" type="text" class="form-control" id="username" name="username" required>
            </div>
            <div class="form-group">
              <label for="email">Email</label>
              <input v-model="email" type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="form-group">
              <label for="password">Password</label>
              <input v-model="password" type="password" class="form-control" id="password" name="password" required>
            </div>
            <div class="form-group">
              <label for="confirm-password">Confirm Password</label>
              <input v-model="confirm_password" type="password" class="form-control" id="confirm-password" name="confirm-password" required>
            </div>
            <div class="d-grid mt-3 mb-4">
              Already have an account? <a href="/login">Login</a>
            </div>
          </form>
          <button @click="submit" type="submit" class="btn btn-primary">Register</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RegisterView",
  data(){
    return {
      username: "",
      email: "",
      password: "",
      confirm_password: ""
    }
  },
  methods: {
    submit(){
      if(this.password === this.confirm_password) {
        axios.post("http://localhost:8000/register/user", {
          username: this.username,
          password: this.password,
          email: this.email
        }).then(resp => {
          console.log(resp)
          this.$router.push("/login")
        }).catch(err => {
          console.log(err)
        })
      }else{
        alert("Password does not match")
      }
    }
  }
}
</script>


<style scoped>
.container {
  margin-top: 10rem;
  background-color: white;
  padding: 3rem;
}
form {
  margin-top: 3rem;
}
</style>