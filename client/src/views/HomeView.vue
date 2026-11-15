<script setup lang="ts">

import { ref, onMounted, shallowRef, computed } from 'vue';
import { socket, state } from '@/socket'
import Ajv from "ajv";

// let players = shallowRef([{ id: 1, name: 'Item #1'}])
const players = ref({})
const hasData = ref(false); 

const history = ref({})

function update_players(data: any) {
    if (Object.keys(data).length === 0) {
        hasData.value = false;
    } else {
        // console.log(data)
        players.value = data;
        hasData.value = true;
    }

}

function update_history(data: any) {
    history.value = data
    console.log(history.value)
}

const selectedPlayerId = ref(null)

const playerList = computed(() => {
    return Object.entries(players.value || {}).map(([key, playerObj]) => {
        return {
            id: Number(key),  // Assigns the dictionary key as the ID
            ...playerObj      // Adds Username, Health, etc.
        }
    });
});
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

    socket.on("history_update", (data) => {
        update_history(data)
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
    <v-row size="3">
        <v-col cols="1">
            <v-card class="ml-10">
            <v-col cols="auto">
                <v-list v-if="hasData" class="pr-4">
                    <template v-for="(value, key) in players" :key="key">
                        <v-list-item>
                            <v-row align="center" no-gutters>
                                <v-col cols="auto" style="min-width: 145px;" class="d-flex align-center">
                                    <v-btn rounded="0" icon="mdi-gift" :to="`/sponsor/${key}`" class="mr-3"></v-btn>
                                    <span>{{ value["Username"] }}</span>
                                </v-col>

                                <v-divider vertical class="mx-4"></v-divider>

                                <v-col style="width: 350px;">
                                    <v-progress-linear 
                                        color="pink"
                                        height="25"
                                        rounded="sm" 
                                        :model-value="value['Health']"
                                    ></v-progress-linear>
                                </v-col>

                                <v-col cols="auto" class="d-flex align-center pl-4">
                                    <span>{{ value["Health"] }}/100</span>
                                </v-col>
                            </v-row>
                        </v-list-item>
                    </template>
                </v-list>
            </v-col>
            <p v-if="!hasData">The games have not begun!</p>
            </v-card>
        </v-col>
        <v-col>
            <v-card class="mr-10">
                <v-row>
                    <v-select
                        v-model="selectedPlayerId"
                        :items="playerList"
                        item-title="Username"
                        item-value="id"
                        label="Select a player"
                    ></v-select>
                </v-row>
                <v-row>
                    <v-sparkline
                        color="primary"
                    :model-value="history[selectedPlayerId] || []"
                    min="0"
                    max="100"
                    :gradient="['#f72047', '#ffd200', '#1feaea'].reverse()"
                    stroke-linecap="round"
                    ></v-sparkline>
                    
                </v-row>
            </v-card>
        </v-col>
    </v-row>
</template>