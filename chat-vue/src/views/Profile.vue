<script setup>
import { ref, onMounted, onBeforeMount, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth.js'
import { Users } from '@/api.js'
import moment from 'moment'


const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const userfromaddress = ref([])


const getUser = async () => {
    userfromaddress.value = await Users.getById(route.params.id)
}

const goBack = () => {
    router.push({ name: 'chat-main' })
}

const getFormatDate = (date) => {
    return moment(date).format('DD.MM.YYYY')
}

onMounted(() => {
    getUser()
})

const gooduser = computed(() => {
    return userfromaddress.value?.id != null && userfromaddress.value?.id === authStore.id
})
</script>

<template>
    
      <button class="btn btn-outline-secondary d-flex align-items-center gap-2" @click="goBack"><= Назад</button>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-3">
                        <div>
                            avatar
                        </div>
                        <div>
                            Online | Offline
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="d-block p-2 text-bg-primary text-center">Характеристики пользователя</div>
                        <div>
                            Никнейм: {{ userfromaddress.username }}
                        </div>
                        <div>
                            Имя: {{ userfromaddress.first_name }}
                        </div>
                        <div>
                            Фамилия: {{ userfromaddress.last_name }}
                        </div>
                        <div>
                            Пол: {{ userfromaddress.gender_display }}
                        </div>
                        <div>
                            Дата регистрации: {{ getFormatDate(userfromaddress.date_joined) }}
                        </div>
                    </div>
                    
                    <div class="col-3" v-if="gooduser">
                        <div>
                            Edit profile
                        </div>
                        <div>
                            delete profile
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-12">
                            <div class="d-block p-2 text-bg-primary text-center">Кратенько о себе</div>
                            <div>
                                {{ userfromaddress.about }}
                            </div>
                        </div>
                    </div>

                    <div class="row" v-if="gooduser">
                        <div class="col-4">

                            <div class="height overflow-auto">
                                <div class="d-block p-2 text-bg-primary">
                                    Online Users
                                </div>

                            </div>
                        </div>
                        <div class="col-8">
                            <div class="height overflow-auto">

                            </div>
                            <!-- MESSAGE SENT BLOCK START -->
                            <div class="align-items-end">
                                <form class="d-flex" method="POST">
                                    <input type="text" name="name" id="name" class="form-control" required />
                                    <input class="btn btn-primary" type="submit" />
                                </form>
                            </div>
                            <!-- MESSAGE SENT BLOCK END -->
                        </div>
                    </div>
                </div>
            </div>

</template>

<style scoped>
div.height {
    height: 55vh;
    border: 1px dashed coral;
}

.visota {
    height: 85vh;
}
</style>