<script setup lang="ts">
import { onMounted, ref, shallowRef } from 'vue';
import { useRoute} from 'vue-router';

const route = useRoute();
const player = shallowRef({"username": "placeholder", "health": 0});

onMounted(async () => {
    try {
        const response = await fetch(`/api/player/${route.params.id}`);
        player.value = await response.json();
    } catch (error) { 
        // TODO: error handling
    }
});


</script>
<template>
    <p>You are sponsoring: {{ player["username"] }}, with ID: {{ route.params.id }}. They have {{ player["health"] }} / 100 health.</p>
</template>
