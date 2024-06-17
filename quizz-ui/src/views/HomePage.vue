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

  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-auto">
        <h1>AlcoTest</h1>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-auto">
        <router-link to="/new-quiz">Démarrer le quiz !</router-link>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-auto">
        <div v-for="scoreEntry in JSON.parse(participationStorageService.getParticipationScore()).scores" v-bind:key="scoreEntry.date">
          {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
        </div>
      </div>
    </div>
  </div>

  
  
</template>

<style>
#container {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>