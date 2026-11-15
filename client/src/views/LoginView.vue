<script setup lang="ts">

import AuthForm from '@/components/AuthForm.vue';

</script>

<template>
  <h2>Login</h2>

  <v-container class="d-flex align-center justify-center">
    <v-card class="w-25">
      <AuthForm submit_text="Sign in!">
        <template #footer>
          <RouterLink class="d-flex align-center justify-center" to="signup">Signup instead</RouterLink>
        </template>
      </AuthForm>
    </v-card>
  </v-container>
</template>

<style scoped></style>
