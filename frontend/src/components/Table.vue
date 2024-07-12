<script>
export default {
  props: ['getData'],
  data()
  {
    return {
      dates: [],
      cases: []
    }
  },
  async mounted()
  {
    const values = await this.getData()
    this.dates = values.data.date
    this.cases = values.data.new_cases
  }
}
</script>

<template>
  <div class="container">
    <table>
      <tr>
        <th class="header-item">Date</th>
        <th class="header-item">Cases</th>
      </tr>
      <tr v-for="(date, i) in dates" :key="i" class="table-rows">
        <td>{{ date }}</td>
        <td>{{ cases[i] }}</td>
      </tr>
    </table>
  </div>
</template>

<style scoped>
table {
  border-collapse: collapse;
  width: 100%;
  table-layout: auto !important;
  word-wrap: break-word;
}

td {
  padding: 5px;
  text-align: center;
  border-bottom: 2px solid #1869F4;
}

.header-item {
  padding: 30px 20px;
  font-size: 12px;
  background-color: #1869F4;
  text-transform: uppercase;
}

.table-rows:nth-child(odd) {
  background-color: rgb(250, 250, 250);
}
</style>
