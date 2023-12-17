<template>
  <tr>
    <td>{{ username }}</td>
    <td>{{ email }}</td>
    <td>{{ role }}</td>
    <td>
      <div @click="deleteUser" class="btn btn-danger">
        Delete
      </div>
    </td>
  </tr>
</template>
<script>
// import axios from "axios";
export default {
  name: "TableRow",
  props: {
    userId: {
      type: String
    },
    username: {
      type: String
    },
    email: {
      type: String
    },
    role: {
      type: String
    }
  },
  methods: {
    deleteUser: function (){
      this.$emit("deleteUser", this.userId)
    }
  }
}
</script>


<style scoped>
.custom-popover {
  --bs-popover-max-width: 200px;
  --bs-popover-border-color: #712cf9;
  --bs-popover-header-bg: #712cf9;
  --bs-popover-header-color: #fff;
  --bs-popover-body-padding-x: 1rem;
  --bs-popover-body-padding-y: .5rem;
}
</style>