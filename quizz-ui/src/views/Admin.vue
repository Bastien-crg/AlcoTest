<script setup>
import AdminConnection from "../components/admin/AdminConnection.vue"
import QuestionAdminDisplay from "../components/admin/QuestionAdminDisplay.vue"
import QuestionEdition from "../components/admin/QuestionEdition.vue"
import QuestionList from "../components/admin/QuestionList.vue"
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";
import QuestionCreation from "../components/admin/QuestionCreation.vue"

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

function createQuestionPage(){
  adminMode.value = "QuestionCreation"
}

function backToList(){
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
    <button class="btn btn-outline-success my-2 my-sm-0" @click="unlog()">Déconnexion</button>
    <QuestionAdminDisplay v-if="adminMode == 'QuestionAdminDisplay'" :current-question="chosenQuest" @question-deleted="backToList" @back-to-list="backToList" @edit-question="editQuestion" ></QuestionAdminDisplay>
    <QuestionEdition v-else-if="adminMode == 'QuestionEdition'" :current-question="chosenQuest" @cancel-edit="backToList" @question-edited="backToList" ></QuestionEdition>
    <QuestionList v-else-if="adminMode == 'QuestionList'" @chosen-question="chosenQuestion" @create-question="createQuestionPage" ></QuestionList>
    <QuestionCreation v-else-if="adminMode == 'QuestionCreation'" @cancel-edit="backToList" @question-edited="backToList" />

  </div>
    
</template>

<style>



</style>