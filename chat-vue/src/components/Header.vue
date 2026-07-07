<script setup>
import {ref, onMounted, computed} from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth.js'
import { Users } from '@/api.js'

const authStore = useAuthStore()

const csrfToken = computed(() => {
	const cookie = document.cookie
		.split('; ')
		.find((row) => row.startsWith('csrftoken='))
	return cookie ? decodeURIComponent(cookie.split('=')[1]) : ''
})
onMounted(() => {
    if (!authStore.isLoaded) {
        authStore.loadCurrentUser();
    }
})
</script>
<template>
	<!--Header START-->
	<div class="container-fluid">
    	<div class="row">
            <div class="col-12 border border-primary">
                <p class="h1 text-center">
				    My_AWESOME_chat_header
					<a class="btn btn-primary btn-sm" href="/accounts/login/">Войти</a>
			    </p>
            </div>
		</div>
	</div>
	<!--Header END-->
</template>

<style scoped>
div {
	background-color: aqua;
}
</style>