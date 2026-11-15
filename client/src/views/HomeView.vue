<script setup>

import { ref, onMounted, shallowRef } from 'vue';
import { socket, state } from '@/socket'
import Ajv from "ajv";

const ajv = new Ajv(); // TODO: may be unecessary
// const serverMessage = ref("Loading... ")
let players = shallowRef([{ id: 1, name: 'Item #1'}])
onMounted(async () => {

    socket.on("player_update", (data) => {
        players.value = data;
        console.log(data);
        console.log(players.value);
    });

// players = 
//   try {
//     const response = await fetch("/api/get-data");
//     const data = await response.json();
//     serverMessage.value = data;
    
//   } catch (error) {
//     serverMessage.value = "Could not connect to server"
//   }
});



</script>

<template>
    <h2>Home</h2>
    <v-row>
        <v-column class="ml-10">
            <v-list>
                <template v-for="(value, key) in players"
                    :key="key"
                >
                    <v-list-item>
                        <template v-slot:prepend>
                            <v-btn icon="mdi-gift"></v-btn>
                            <span class="mr-3">{{ value["Username"]}}</span>
                            <v-divider vertical class="mx-4"></v-divider>
                            <span>Health: {{  value["Health"] }}</span>
                        </template>
                    </v-list-item>
                    <v-divider></v-divider>
                </template>
            </v-list>
        </v-column>
    </v-row>
</template>