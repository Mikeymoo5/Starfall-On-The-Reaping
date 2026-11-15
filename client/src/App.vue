<script setup lang="ts">
import { useErrorStore } from './stores/errorStore';

const errorStore = useErrorStore()
</script>

<template>
  <v-app>
      <!-- <h1>You did it!</h1>
      <p>
        <strong>Current route path:</strong> {{ $route.fullPath }}
      </p>
      <div>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/signup">Signup</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
      </div> -->
      <v-main>
        <v-app-bar>
          <template v-slot:prepend>
            <v-btn to="/" icon="mdi-home"></v-btn>
          </template>
          
          <!-- <v-btn to="/sponsor">Sponsor</v-btn> -->

          <!-- <template v-slot:append>
            <v-btn to="/account" icon="mdi-account"></v-btn>
          </template> -->
        </v-app-bar>
        <RouterView />
      </v-main>

      <v-snackbar 
        :timeout="2000" 
        prepend-icon="mdi-alert-circle" 
        color="error" 
        v-model="errorStore.showPopup" 
        class="pb-3"
        location="top end"
        >
          <v-text>{{ errorStore.message }}</v-text>
          <template v-slot:actions>
            <v-btn icon="mdi-close" @click="errorStore.closePopup()"></v-btn>
          </template>
      </v-snackbar>

    </v-app>
</template>

<style scoped></style>
