<script setup>

import AuthForm from '@/components/AuthForm.vue';

</script>

<template>
    <h2>Signup</h2>
    <v-container class="d-flex justify-center align-center">
        <v-card class="w-25">
            <AuthForm submit_text="Sign up!">
                <template #footer>
                    <RouterLink class="d-flex justify-center align-center" to="/login">Login Instead</RouterLink>
                </template>
            </AuthForm>
        </v-card>
    </v-container>
</template>