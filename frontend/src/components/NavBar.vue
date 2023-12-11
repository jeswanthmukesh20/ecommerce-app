<template>
  <nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#"><img src="../assets/Logo.png" width="182" height="42" alt=""></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav justify-content-center ml-auto mr-auto">
      <li class="nav-item active">
        <a @click="currentPage()" class="nav-link" id="home" href="#">Home </a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Categories
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Grocery</a>
          <a class="dropdown-item" href="#">Vegetables</a>
          <a class="dropdown-item" href="#">Snacks</a>
        </div>
      </li>
      <li class="nav-item">
        <form  class="form-inline my-2 mr-5 my-lg-0">
          <input style="width: 500px" class="form-control mr-sm-2" type="search"  placeholder="Search for products and more.." aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </li>
    </ul>

    <a class="btn nav-item">
    <img data-toggle="tooltip" onclick="alert('Hello wrold')" data-placement="bottom" title="your cart" src="../assets/img/cart.png" height="42px" width="42px" alt="" >
      <span style=" top: -15px; left: -10px" class="badge sticky-top text-lg badge-danger">{{ ($store.state.cartItem < 10) ? $store.state.cartItem : '10+' }}</span>

      </a>
    <img data-toggle="tooltip" onclick="alert('Hello wrold')" data-placement="bottom" title="your profile" src="../assets/img/user.png" height="62px" width="72px" alt="" class="rounded-circle nav-item btn">
  </div>
</nav>
</template>

<script>
// import Logo from "../assets/Logo.png"
// document.getElementById("logo").src = Logo.src
export default {
  name: 'NabBar',
  props: {
    page: {
      type: String
    },
  },
  methods: {
    currentPage: function (){
        console.log("clicked")
        let element =  document.getElementById(this.page);
        let elementClass = element.class;
        document.getElementById(this.page).class = elementClass + " disabled"

    }
  }

}

</script>

<!--<style>-->
<!--//.nav-item {-->
<!--//  margin-left: 2rem;-->
<!--//  margin-right: 2rem;-->
<!--//}-->
<!--</style>-->
