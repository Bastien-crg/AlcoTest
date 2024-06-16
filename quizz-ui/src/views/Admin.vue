<script setup>
import AdminConnection from "../components/admin/AdminConnection.vue"
import QuestionAdminDisplay from "../components/admin/QuestionAdminDisplay.vue"
import QuestionEdition from "../components/admin/QuestionEdition.vue"
import QuestionList from "../components/admin/QuestionList.vue"
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router'



const router = useRouter()

const chosenQuest = ref(null)

const adminMode = ref("QuestionList")
const isToken = ref(false);

function changeLog(val){
  console.log(val)
  isToken.value = val
}

function changeMode(mode){
  adminMode.value = mode
}

function unlog(){
  isToken.value = false
  participationStorageService.saveToken(null)
  router.push('/')
}

function chosenQuestion(question){
  chosenQuest.value = question
  adminMode.value = "QuestionAdminDisplay"
}

function questionDeleted(){
  adminMode.value = "QuestionList"
}

function editQuestion(question){
  chosenQuest.value = question
  adminMode.value = "QuestionEdition"
}

onMounted(() => {
  if (participationStorageService.getToken() == 'null'){
    isToken.value == false
  } else {
    isToken.value = true
  }
  
});


</script>


<template>
  <AdminConnection v-if="!isToken" @is-token="changeLog"></AdminConnection>
  <div v-else>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <button class="nav-link"  @click="changeMode('QuestionAdminDisplay')">Question admin display</button>
          </li>
          <li class="nav-item">
            <button class="nav-link" @click="changeMode('QuestionEdition')">Question edition</button>
          </li>
          <li class="nav-item">
            <button class="nav-link" @click="changeMode('QuestionList')">Question list</button>
          </li>
        </ul>
      </div>
      <button class="btn btn-outline-success my-2 my-sm-0" @click="unlog()">Déconnexion</button>
    </nav>
    <QuestionAdminDisplay v-if="adminMode == 'QuestionAdminDisplay'" :current-question="chosenQuest" @question-deleted="questionDeleted" @edit-question="editQuestion" ></QuestionAdminDisplay>
    <QuestionEdition v-else-if="adminMode == 'QuestionEdition'" :current-question="chosenQuest" ></QuestionEdition>
    <QuestionList v-else-if="adminMode == 'QuestionList'" @chosen-question="chosenQuestion" ></QuestionList>

  </div>
    
</template>

<style>



</style>