<template>
  <nav class="navbar navbar-light bg-light justify-content-between">
  <router-link class="navbar-brand" to="/">Home page</router-link>
  <button class="btn btn-outline-success my-2 my-sm-0" @click="router.push('admin')">Connexion</button>
</nav>
</template>

<script setup>
import { useRouter } from 'vue-router'
import participationStorageService from "@/services/ParticipationStorageService";



const router = useRouter()





</script>
