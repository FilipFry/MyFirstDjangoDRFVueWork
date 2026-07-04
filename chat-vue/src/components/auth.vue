<script setup>
import { ref, onMounted, computed } from 'vue';
import {useAuthStore} from '@/stores/auth.js'

const authStore = useAuthStore();
const csrfToken = computed(() => {
  const cookie = document.cookie
    .split('; ')
    .find((row) => row.startsWith('csrftoken='))
  return cookie ? decodeURIComponent(cookie.split('=')[1]) : ''
})

onMounted(()=>{
    if (!authStore.isLoaded) {
        authStore.loadCurrentUser();
    }
});
</script>

<template></template>