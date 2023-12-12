<template>
  <div id="footer" class="container">
    <footer class="py-3 my-4">
      <ul class="nav justify-content-center border-bottom pb-3 mb-3">
        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">Home</a></li>
        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">Features</a></li>
        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">Pricing</a></li>
        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">FAQs</a></li>
        <li class="nav-item"><a href="https://getbootstrap.com/docs/5.3/examples/footers/#" class="nav-link px-2 text-body-secondary">About</a></li>
      </ul>
      <p class="text-center text-body-secondary">© {{ year }} {{ companyName }}, Inc</p>
    </footer>
  </div>

</template>

<script>

export default {
  name: "FooterComponent",
  props: {
    companyName: {
      type: String,
      default: "Kirana Kart"
    }
  },
  data(){
    let date = new Date();
    let year = date.getFullYear();
    return {
      year: year
    }
  }
}

</script>

<style scoped>
#footer{
  background-color: white;
  margin-bottom: 0px;
}
</style>
