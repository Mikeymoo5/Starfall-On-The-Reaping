# TODO: If there is no session cookie, redirect to LoginView
<script setup lang="ts">
import { useRouter } from 'vue-router';
const router = useRouter();

router.push("/login")

</script>

<template>
    <h1>Account</h1>
</template>