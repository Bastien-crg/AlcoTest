<script setup>
import QuestionDisplay from "../components/QuestionDisplay.vue"
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";
import { ref, onMounted } from 'vue';


const quiz_info = ref(null);

const current_question_pos = ref(0);
const current_question_data = ref(null);
const answers = ref([]);

const question = {
    text: "Quelle est la couleur du cheval blanc d'Henry IV ?",
    title: "Dummy Question",
    image: "falseb64imagecontent",
    position: 1,
    possibleAnswers: [
        {
            text: "Noir",
            isCorrect: false 
        },
        {
            text: "Gris",
            isCorrect: false
        },
        {
            text: "Blanc",
            isCorrect: true
        },
        {
            text: "La réponse D",
            isCorrect: false
        }
    ]
}

function callback(answer) {
  answers.value.push(answer);
  getNextQuestion();
}

function getNextQuestion(){
  current_question_pos.value++;
  let payload = quizApiService.getQuestionByPos(current_question_pos.value);
  payload.then(res => current_question_data.value = res.data);
}




onMounted(() => {
  let payload = quizApiService.getQuizInfo();
  payload.then(res => quiz_info.value = res)
  getNextQuestion()
  
});

</script>

<template>
  <div>
    <h1>Question Manager</h1>
  </div>
  <br/>
  <QuestionDisplay v-if="current_question_data != null" :currentQuestion="current_question_data" @answer-clicked="callback"></QuestionDisplay>
  
</template>



<style>
</style>
