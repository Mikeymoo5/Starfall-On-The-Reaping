import { reactive } from "vue";
import { io } from "socket.io-client";

export const state = reactive({
    connected: false,
    all_player_data: []
})

const URL = "http://localhost:5000";

export const socket = io(URL, {
    autoConnect: true
})

socket.on("connect", () => {
    state.connected = true;
});

socket.on("disconnect", () => {
    state.connected = false;
});

// socket.on("receive_message", (msg) => {
//     state.messages.push(msg);
// })
