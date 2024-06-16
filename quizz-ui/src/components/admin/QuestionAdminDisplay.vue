<template>
  <button type="button" class="btn btn-success" @click="editQuestion(question)" >Modifier</button>
  <button type="button" class="btn btn-danger" @click="deleteQuestion()" >Supprimer</button>
  <table class="table">
    <tbody>
      <tr>
        <th scope="row">Titre</th>
        <td>{{ props.currentQuestion.title }}</td>
      </tr>
      <tr>
        <th scope="row">Intitulé</th>
        <td>{{ props.currentQuestion.text }}</td>
      </tr>
      <tr>
        <th scope="row">Réponse</th>
        <td>
          <ul class="list-group">
            <li v-for="answer in props.currentQuestion.possibleAnswers" :class="isActive(answer)">{{ answer.text }}</li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>

import quizApiService from "@/services/QuizApiService";
import { useRouter } from 'vue-router'



const router = useRouter()
const emit = defineEmits(['questionDeleted','editQuestion']);


function isActive(answer){
  if (answer.isCorrect){
    return "list-group-item active"
  } else {
    return "list-group-item"
  }
}

function editQuestion(question){
  emit('editQuestion', question)
}

function deleteQuestion(){
  let payload = quizApiService.deleteQuestionById(props.currentQuestion.id)
  payload.then(res => {
    emit('questionDeleted', true)
    console.log(res)
  })
}

const props = defineProps({
  currentQuestion: Object
});

</script>