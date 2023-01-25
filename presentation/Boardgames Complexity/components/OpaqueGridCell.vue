<script setup lang="ts">
defineProps<{
    value: number
}>()
</script>

<template>
    <div class="opaque-cell">
        <div class="opaque-block"></div>
        <div class="nonopaque-text">{{ value }}</div>
    </div>
    <!-- <div style="opacity: {{ value / 10 }}">{{ this.value }}</div> -->
</template>

<style scoped>
.opaque-cell {
    position: relative;
    border: 1px solid grey;
    align-items: center;
    justify-content: center;
    display: flex;
}

.opaque-block {
    background-color: rgb(245, 70, 70);
    opacity: v-bind(value / 10);
    width: 100%;
    height: 100%;
}

.nonopaque-text {
    position: absolute;
}
</style>