<script setup>

import { ref } from 'vue'
import participationStorageService from "@/services/ParticipationStorageService";
import { useRouter } from 'vue-router';

const router = useRouter();
const username = ref("")

function launchNewQuiz() {
    participationStorageService.savePlayerName(username.value);
    router.push("/questions")
}





</script>


<template>

    <div class="container">
    <div class="row">
        <div class="col">
        </div>
        <div class="col-6">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" v-model="username" class="form-control" id="username" placeholder="Enter username">
            </div>
        </div>
        <div class="col">
        </div>
    </div>
    <div class="row">
        <div class="col">
        </div>
        <div class="col-6">
            <div class="form-group">
                <br>
                <button @click="launchNewQuiz" class="btn btn-primary">Go!</button>
            </div>
        </div>
        <div class="col">
        </div>
    </div>
    </div>


    
    
</template>

<style>



</style>