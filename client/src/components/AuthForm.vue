<script setup>

    function handleSubmit() {

    }

    defineProps({
        submit_text: String
    });
</script>

<template>
    <v-container class="fill-height fill-width">
        <!-- <v-row align="center" justify="center">
            <v-column> -->
                <v-form ref="formRef" v-model="isValid" @submit.prevent="handleSubmit">

                    <v-text-field
                        v-model="username"
                        label="Username"
                    ></v-text-field>

                    <v-text-field
                        v-model="password"
                        label="Password"
                    ></v-text-field>
                    
                    <v-btn block>{{ submit_text }}</v-btn>
                    <br>
                    <slot name="footer"></slot>

                </v-form>
            <!-- </v-column>z
        </v-row> -->
    </v-container>
</template>
