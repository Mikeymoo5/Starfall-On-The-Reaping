import { defineStore } from 'pinia';
import router from '@/router';

export const useErrorStore = defineStore('error', {
    state: () => ({
        showPopup: false,
        message: '',
    }),
    actions: {
        triggerError(errorMessage: string, redirectPath = "/") {
            this.message = errorMessage;
            this.showPopup = true;

            if (redirectPath) {
                router.push(redirectPath)
            }
        },
        closePopup() {
            this.showPopup = false;
            this.message = '';
        }
    }
})