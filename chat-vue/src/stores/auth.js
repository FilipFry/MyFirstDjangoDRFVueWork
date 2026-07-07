import { computed, ref } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore('auth', () => {
    const currentUser = ref(null);
    const isLoaded = ref(false);

    const isAuthenticated = computed(() => currentUser.value?.is_authenticated ?? false)
    const displayName = computed(() => currentUser.value?.user.full_name || currentUser.value?.username)
    const id = computed(() => currentUser.value?.user?.id)
    const last_login = computed(() => currentUser.value?.user.last_login)
    const username = computed(() => currentUser.value?.user.username)
    const full_name = computed(() => currentUser.value?.user.full_name)
    const first_name = computed(() => currentUser.value?.user.first_name)
    const last_name = computed(() => currentUser.value?.user.last_name)
    const email = computed(() => currentUser.value?.user.email)
    const is_active = computed(() => currentUser.value?.user?.is_active)
    const date_joined = computed(() => currentUser.value?.user.date_joined)
    const gender_display = computed(() => currentUser.value?.user.gender_display)
    const avatar = computed(() => currentUser.value?.user.avatar)
    const about = computed(() => currentUser.value?.user.about)
    const is_banned = computed(() => currentUser.value?.user.is_banned)

    async function loadCurrentUser() {
        try {
            const response = await axios.get('/api/user/')
            currentUser.value = response.data
        }catch {
            currentUser.value = null
        }finally {
            isLoaded.value = true
            }
    }
     return {
        currentUser,
        isLoaded,
        isAuthenticated,
        displayName,
        id,
        last_login,
        username,
        full_name,
        first_name,
        last_name,
        email,
        is_active,
        date_joined,
        gender_display,
        avatar,
        about,
        is_banned,
        loadCurrentUser,
    };
})