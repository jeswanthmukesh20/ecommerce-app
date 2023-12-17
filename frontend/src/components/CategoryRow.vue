<template>
  <tr>
    <th> {{ name }} </th>
    <td>{{ user }}</td>
    <td>

      <span v-if="status" class="badge text-bg-success">Approved</span>
      <span v-else class="badge text-bg-success">Pending</span>
    </td>
    <td>
      <div @click="setAction" class="btn btn-primary">
        Approve
      </div>
    </td>
  </tr>
</template>
<script>
export default {
  name: "CategoryRow",
  props: {
    name: {
      type: String
    },
    user: {
      type: String
    },
    status: {
      type: Boolean
    },
    categoryId: {
      type: Number
    }

  },
  methods: {
    setAction(){
      this.$emit("setAction", this.categoryId)
    }
  }
}
</script>
<style scoped>

</style>