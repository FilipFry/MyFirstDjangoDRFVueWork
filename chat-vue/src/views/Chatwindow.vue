<script setup>
import { ref, onMounted,onUpdated, computed, onBeforeMount, onUnmounted } from 'vue';
import { Message, Users } from '@/api.js'
import { useAuthStore } from '@/stores/auth.js'
import moment from 'moment'

const MessageDisplay = ref([])
const UsersDisplay = ref([])
const authStore = useAuthStore()
let timer;

const form = ref({
            textmessage: '',
			is_private: false
        })

const csrfToken = computed(() => {
	const cookie = document.cookie
		.split('; ')
		.find((row) => row.startsWith('csrftoken='))
	return cookie ? decodeURIComponent(cookie.split('=')[1]) : ''
})


const getMessagesList = async () => {
	let res = await Message.getList()
	console.log("messages", res)
	MessageDisplay.value = res.results
}
const getUsersList = async () => {
	let res = await Users.getList()
	console.log("users", res)
	UsersDisplay.value = res.results
}

const getFormatDate = (date) => {
	return moment(date).format('HH:mm')
}
const sent = async () => {
	const response = await Message.save(form.value)
}
onMounted(() => {
	getMessagesList()
	getUsersList()
	timer = setInterval(getMessagesList, 1000)
})
onUnmounted(() => {
	clearInterval(timer)
})
</script>

<template>
	<div class="container-fluid my-block">
		<div class="row">
			<!--USER BLOCK START-->
			<div class="col-2">
				<div class="d-flex flex-column border border-primary mt-2">
					<div class="d-block p-2 text-bg-primary">
						User Pannel {{ authStore.isAuthenticated }}
					
					</div>
					<div v-if="authStore.isAuthenticated">
						<div class="border border-secondary m-1">
							<RouterLink v-if="authStore.id" :to="{
								name: 'profile',
								params: { id: authStore.id },
							}">
								{{ authStore.displayName }}
							</RouterLink>
						</div>
						<div class="border border-secondary m-1">

							<div class="d-flex align-items-center justify-content-center text-body-secondary">
								Нет фото
							</div>
						</div>
						<div v-if="authStore.is_active">
							<div class="border border-secondary text-bg-success m-1">
								{{ authStore.is_active ? 'Online' : 'Offline' }}
							</div>
						</div>
						<div v-else>
							<div class="border border-secondary text-bg-danger m-1">
								{{ authStore.is_active ? 'Online' : 'offline' }}
							</div>
						</div>
						<div class="border border-secondary m-1">
							<form v-if="authStore.isAuthenticated" method="post" action="/accounts/logout/" class="mb-0">
            					<input type="hidden" name="csrfmiddlewaretoken" :value="csrfToken">
            					<button type="submit" class="btn btn-outline-secondary btn-sm">Выйти</button>
							</form>
						</div>
					</div>
					<div v-else>
						<p class="text-break">User is not autentificated, please <a href="/accounts/login/">LOGIN</a> or register</p>						
					</div>
				</div>
				<!--USER BLOCK END-->
				<!--ONLINE BLOCK START-->
				<div class="border border-primary mt-2">
					<div class="d-block p-2 text-bg-primary">
						Online
					</div>
					<div v-if="UsersDisplay.length > 0">
						<div v-for="user in UsersDisplay">
							<div v-if="user.is_active">
								<div class="border border-secondary m-1">
									<RouterLink :to="{
										name: 'profile',
										params: { id: user.id },
									}">
										{{ user.username }}
									</RouterLink>
								</div>
							</div>
						</div>
					</div>
				</div>
				<!--ONLINE BLOCK END-->
			</div>
			<div class="col-8">
				<div class="border border-primary p-1">
					<!--MESSAGES BLOCK START-->
					<div class="align-items-end" v-if="authStore.isAuthenticated">
					<div class="height overflow-y-auto" v-if="MessageDisplay.length > 0">
						<div v-for="message in MessageDisplay">
							<div v-if="!message.is_private">
								<span class="text-bg-info">{{ message.usermessage_display }}</span>
								<span class="text-bg-warning">&nbsp;:&nbsp;{{ getFormatDate(message.datemessage)}}&nbsp;:&nbsp;</span>
								<span class="text-break">{{ message.textmessage }}</span>
							</div>
						</div>
					</div>
					</div>
					<div v-else>
						<div>
						<span class="text-bg-info">ADMIN</span>
						<span class="text-bg-warning">&nbsp;:&nbsp;00:00&nbsp;:&nbsp;</span>
						<span class="text-break">Неавторизированному пользователю</span>
						</div>
						<div>
						<span class="text-bg-info">ADMIN</span>
						<span class="text-bg-warning">&nbsp;:&nbsp;00:01&nbsp;:&nbsp;</span>
						<span class="text-break">Нельзя читать</span>
						</div>
						<div>
						<span class="text-bg-info">ADMIN</span>
						<span class="text-bg-warning">&nbsp;:&nbsp;00:02&nbsp;:&nbsp;</span>
						<span class="text-break">А то нос сотвалится</span>
						</div>
					</div>
					<!--MESSAGES BLOCK END-->
					<!--MESSAGE SENT BLOCK START-->
					<div class="align-items-end" v-if="authStore.isAuthenticated">
						<form @submit="sent" class="d-flex">
							<input class="form-control" id="message" v-model="form.textmessage" required autofocus />
							<input class="btn btn-primary" type="submit" />
						</form>
					</div>
					<div v-else>
						
						<span>Aaaa. Сначала адо авторизироваться. <button type="button" class="btn btn-outline-primary btn-sm btn-block">Отправить</button></span>
					</div>
					<!--MESSAGE SENT BLOCK END-->
				</div>
			</div>
			<div class="col-2">
				<!--NEWS BLOCK START-->
				<div class="visually-hidden">
					<div>
						News
					</div>
					<div>
						News1
					</div>
					<div>
						News2
					</div>
					<div>
						News3
					</div>
					<div>
						News4
					</div>
				</div>
				<!--NEWS BLOCK END-->
				<!--ADWARE BLOCK START-->
				<div class="visually-hidden">
					Adware
				</div>
				<!--ADWARE BLOCK END-->
			</div>
		</div>
	</div>
</template>

<style scoped>
div.height {
	height: 80vh;
}
</style>