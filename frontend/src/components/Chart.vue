<script>
export default {
    props: ['getData'],
    data()
    {
        return {
            chart: null
        }
    },
    async mounted()
    {
        const values = await this.getData()

        const myChart = new Chart("myChart", {
            type: "line",
            options: {
                legend: { display: false }
            },
            data: {
                labels: Object.values(values.data.date),
                datasets: [{
                    pointBackgroundColor: "rgba(0,0,255,1)",
                    data: Object.values(values.data.new_cases)
                }]
            }
        });
    }
}
</script>

<template>
    <div class="container">
        <canvas id="myChart" style="height: 100%;"></canvas>
    </div>
</template>