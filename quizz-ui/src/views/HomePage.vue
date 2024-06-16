<script setup>
import { ref, onMounted } from 'vue';
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";



onMounted(async () => {
  let payload = quizApiService.getQuizInfo();
  payload.then(res => {
    participationStorageService.saveParticipationScore(JSON.stringify(res.data));
  })
});
</script>

<template>
  <h1>Home page</h1>
  <br/>
  <router-link to="/new-quiz">Démarrer le quiz !</router-link>
  <br/>
  <div v-for="scoreEntry in JSON.parse(participationStorageService.getParticipationScore()).scores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  
</template>