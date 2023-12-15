<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="login-container">
          <h2 class="text-center mb-4">Login</h2>
          <form>
            <div class="mb-3">
              <label for="username" class="form-label">Username</label>
              <input type="text" class="form-control" id="username" name="username" v-model="username" required>
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">Password</label>
              <input type="password" v-model="password" class="form-control" id="password" name="password" required>
            </div>
            <div class="d-grid mt-3 mb-3">
              Don't have an account? <a href="/register">Register now</a>
            </div>
          </form>
          <div class="d-grid">
            <button @click="submit" class="btn btn-primary">Login</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "LoginView",
  methods: {
    submit(){
      axios.post("http://localhost:8000/login", {

        username: this.username,
        password: this.password
      }).then(resp => {
        console.log(resp)
        console.log(resp)
        this.$store.dispatch("setUser", resp.data);
        this.$router.push("/")
      }).catch(err => {
        console.log(err);
      })
    }
  },
  data() {
    return {
      username: "",
      password: "",
      user: {
      }
    }
  }
}
</script>

<style scoped>
.login-container {
  margin-top: 100px;
}
.container {
  background-color: white;
  margin-top: 10rem;
  padding-bottom: 4rem;
}
</style>