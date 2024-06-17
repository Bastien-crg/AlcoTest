<template>
  <button type="button" class="btn btn-success" @click="createQuestion()" >Créer un question</button>
  <br/>
  <table id="example" class="table table-striped" style="width:100%">
    <thead>
        <tr>
          <th>Position</th>
          <th>Title</th>
          <th>Question</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="question in question_list">
          <td>{{ question.position }}</td>
          <td>{{ question.title }}</td>
          <td>{{ question.text }}</td>
          <td><button type="button" class="btn btn-primary" @click="editQuestion(question)" >Détails</button></td>
        </tr>
    </tbody>
  </table>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

const question_list = ref([])
const emit = defineEmits(['chosenQuestion','createQuestion']);

function editQuestion(question){
  emit('chosenQuestion', question)
}

function createQuestion(){
  emit('createQuestion', true)

}

onMounted(() => {
  let payload = quizApiService.getQuizInfo();
  payload.then(res => {
    participationStorageService.saveParticipationScore(JSON.stringify(res.data));
  }).then(()=>{
    for (let i = 0; i < JSON.parse(participationStorageService.getParticipationScore()).size; i++) {
    let payload = quizApiService.getQuestionByPos(i+1);
    payload.then(res => question_list.value.push(res.data));
    
  }
  })

});
</script>