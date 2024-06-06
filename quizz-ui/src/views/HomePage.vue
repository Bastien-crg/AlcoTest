<script setup>
import { ref, onMounted } from 'vue';
import quizApiService from "@/services/QuizApiService";




const registeredScores = ref([]);

onMounted(async () => {
		console.log("Home page mounted");
    //registeredScores.push(quizApiService.getQuizInfo())
    registeredScores.value.push({playerName : "Bastien",score:"8000"})
    registeredScores.value.push({playerName : "Célian",score:"2"})
});
</script>

<template>
  <h1>Home page</h1>
  <br/>
  <router-link to="/new-quiz">Démarrer le quiz !</router-link>
  <br/>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  {{ playerName }}
</template>