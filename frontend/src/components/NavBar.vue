<template>
  <nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#"><img src="../assets/Logo.png" width="182" height="42" alt=""></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav justify-content-center ml-auto mr-auto">
      <li class="nav-item active">
        <a class="nav-link" id="home" href="/">Home </a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Categories
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a @click="$store.commit('setCategory', 'All')" class="dropdown-item" href="#">All</a>
          <a @click="$store.commit('setCategory', 'Grocery')" class="dropdown-item" href="#">Grocery</a>
          <a @click="$store.commit('setCategory', 'Vegetables')" class="dropdown-item" href="#">Vegetables</a>
          <a @click="$store.commit('setCategory', 'Snacks')" class="dropdown-item" href="#">Snacks</a>
        </div>
      </li>
      <li class="nav-item ml-3">
        <form  class="form-inline my-2 mr-5 my-lg-0">
          <input style="width: 500px" class="form-control mr-sm-2" type="search"  placeholder="Search for products and more.." aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </li>
    </ul>

    <a class="btn nav-item ml-3" href="/cart">
    <img data-toggle="tooltip"  data-placement="bottom" title="your cart" src="../assets/img/cart.png" height="42px" width="42px" alt="" >
      <span v-if="itemCount" style=" top: -15px; left: -10px" class="badge sticky-top text-lg badge-danger">{{ ($store.state.cartItem < 11) ? $store.state.cartItem : '10+' }}</span>

      </a>
    <div v-if="userLoggedIn"  class="dropdown ">
      <a  class="dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        {{userData.username}}
        <img data-toggle="tooltip" data-placement="bottom" title="your profile" src="../assets/img/user.png" height="62px" width="72px" alt="" class="rounded-circle nav-item btn">

      </a>

      <div class="dropdown-menu" aria-labelledby="navbarDropdown">
        <a class="dropdown-item btn" href="/profile">Profile</a>
        <a class="dropdown-item btn btn-danger" @click="logout">Logout</a>
      </div>

    </div>
    <div @click="this.$router.push('/login')" v-else class="btn btn-primary">Login</div>
  </div>
</nav>
</template>

<script>

export default {
  name: 'NabBar',
  props: {
    page: {
      type: String
    },
  },
  methods: {
    logout(){
      this.$store.dispatch("setUser", {
        username: "",
        user_id: "",
        role: "",
        access_token: ""
      })
      this.$router.push("/login")
    }
  },
  data(){
    return {
      loggenIn: (this.$store.state.user.access_token !== ""),
      user: this.$store.state.user,
    }
  },
  computed:{
    userData(){
      return this.$store.state.user
    },
    userLoggedIn(){
      return this.$store.state.user.access_token !== ""
    },
    itemCount(){
      return this.$store.state.cartItem > 0
    }
  }

}

</script>
<style scoped>
.dropdown-toggle{
  color: black;
}
</style>