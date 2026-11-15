<script setup lang="ts">

import { ref, onMounted, shallowRef } from 'vue';
import { socket, state } from '@/socket'
import Ajv from "ajv";

const ajv = new Ajv(); // TODO: may be unecessary
// const serverMessage = ref("Loading... ")
let players = shallowRef([{ id: 1, name: 'Item #1'}])
const hasData = ref(false); 

function update_players(data: any) {
    if (Object.keys(data).length === 0) {
        hasData.value = false;
    } else {
        players.value = data;
        hasData.value = true;
    }

}

onMounted(async () => {
    try {
        const response = await fetch("/api/players")
        const data = await response.json();
        update_players(data)
        // players.value = data;
        // hasData.value = true;
    } catch (error) {
        // TODO: handle errors
    }
    socket.on("player_update", (data) => {
        update_players(data)
        // players.value = data;
        // console.log(data);
        // console.log(players.value);
        // hasData.value = true;
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
            <v-list v-if="hasData">
                <template v-for="(value, key) in players"
                    :key="key"
                >
                    <v-list-item>
                        <v-row align="center">
                            <v-col cols="5" class="d-flex">
                                <v-btn icon="mdi-gift" :to="`/sponsor/${key}`"></v-btn>
                                <span class="mr-3">{{ value["Username"]}}</span>
                            </v-col>

                            <v-divider vertical class="mx-4"></v-divider>

                            <v-col>
                                <v-progress-linear 
                                    color="pink"
                                    height=25
                                    rounded=sm 
                                    :model-value="value['Health']"
                                ></v-progress-linear>
                            </v-col>

                            <v-col>
                                <span>{{value["Health"]}}/100</span>
                            </v-col>
                        </v-row>
                    </v-list-item>
                </template>
            </v-list>
        </v-column>
        <p v-if="!hasData">The games have not begun!</p>
    </v-row>
</template>