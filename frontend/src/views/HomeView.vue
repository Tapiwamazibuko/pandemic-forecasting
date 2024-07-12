<script setup>
import Table from '@/components/Table.vue'
import Chart from '@/components/Chart.vue'
</script>

<script>
import axios from 'axios'

export default {
    methods: {
        async getData()
        {
            return await axios.get('http://127.0.0.1:5000/forecast')
        }
    },
}
</script>



<template>
    <main class="container">
        <h1 className="heading">Pandemic Forecast</h1>
        <div class="diagram-container">
            <Table :getData="getData" />
            <Chart :getData="getData" />
        </div>
    </main>
</template>