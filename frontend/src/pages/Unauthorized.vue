<template>
<div class="container">
  <h1><img src="../assets/img/warning.png" alt="">You are not authorized for this request...</h1>
</div>
</template>

<script>
export default {
  name: "UnAuthorized",
}
</script>
<style scoped>
.container {
  margin-top: 10rem;
  //background-color: white;
  color: orangered;
  text-align: center;
}
img {
  height: 42px;
  width: 42px;
}
</style>