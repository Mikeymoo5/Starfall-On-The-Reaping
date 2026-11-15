<script setup lang="ts">
import { useErrorStore } from '@/stores/errorStore';
import { onMounted, ref, shallowRef } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const errorStore = useErrorStore()

const player = shallowRef({"username": null, "health": 0});

onMounted(async () => {
    console.log(player.value["username"])
    if (player.value["username"] == null) {
        errorStore.triggerError("That tribute does not exist!")
    }
    try {
        const response = await fetch(`/api/player/${route.params.id}`);
        player.value = await response.json();
    } catch (error) { 
        // TODO: error handling
    }
});

const formRef = ref()
const selectedValue = ref(null)

const submitForm = async () => {
    const { valid } = await formRef.value.validate()
    if (valid) {
        try {
            const payload = {
                player_id: route.params.id,
                item: selectedValue.value,
                sent: false,
            };

            const response = await fetch("/api/send-gift", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload)
            });
            console.log("success");
        } catch (error) {
            // TODO: handle errors
            console.log(error)
        }
    }
    };

const rules = [
    (value: any) => {
        if (value) return true
        return "You must choose something to donate "
    }
]

</script>
<template>
    <v-row class="d-flex align-center justify-center">
        <v-column class="w-25">
            <p>You are sponsoring: {{ player["username"] }}, with ID: {{ route.params.id }}. They have {{ player["health"] }} / 100 health.</p>
            <v-card class="pa-4">
                <v-form ref="formRef" @submit.prevent="submitForm">
                    <v-combobox 
                        label="Donation"
                        v-model="selectedValue"
                        :items="['Sword', 'Bow', 'Potion']"
                        :rules="rules"
                        variant="outlined"
                    ></v-combobox>
                    <v-btn block type="submit" color="primary">Donate</v-btn>
                </v-form>
            </v-card>
        </v-column>
    </v-row>
</template>
