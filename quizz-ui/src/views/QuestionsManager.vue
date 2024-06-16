<script setup>
import QuestionDisplay from "../components/QuestionDisplay.vue"
import ScoreDisplay from "../components/ScoreDisplay.vue"
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";
import { ref, onMounted } from 'vue';


const current_question_pos = ref(0);
const current_question_data = ref(null);
const answers = ref([]);
const score = ref(null);
const is_form_over = ref(false);



function callback(answer) {
  console.log(answer);
  answers.value.push(answer);
  getNextQuestion();
}

function getNextQuestion(){
  current_question_pos.value++;
  if (current_question_pos.value <= JSON.parse(participationStorageService.getParticipationScore()).size){
    let payload = quizApiService.getQuestionByPos(current_question_pos.value);
    payload.then(res => current_question_data.value = res.data);
  } else {
    let payload = quizApiService.sendAnswer(participationStorageService.getPlayerName(), answers.value);
    payload.then(res =>{
      score.value = res.data
      is_form_over.value = true;
    });
    
  }
  
}


onMounted(() => {
  getNextQuestion()
});

</script>

<template>
  <div>
    <h1>Question Manager</h1>
  </div>
  <br/>
  <QuestionDisplay v-if="current_question_data != null && !is_form_over" :currentQuestion="current_question_data" @answer-clicked="callback"></QuestionDisplay>
  <ScoreDisplay v-if="score != null" :score="score" @answer-clicked="callback"></ScoreDisplay>

  
  
</template>



<style>
</style>
