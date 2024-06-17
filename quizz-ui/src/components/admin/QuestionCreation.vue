<template>
  <button type="button" class="btn btn-success" @click="validateEdit(question)" >Valider</button>
  <button type="button" class="btn btn-danger" @click="cancelEdit(question)" >Annuler</button>
  <form>
    <div class="form-row">
      <div class="col-md-4 mb-3">
        <label for="validationCustom01">Titre</label>
        <input type="text" class="form-control" id="validationCustom01" placeholder="Titre" v-model="title" required>
        
      </div>
      <div class="col-md-4 mb-3">
        <label for="validationCustom02">Intitulé</label>
        <input type="text" class="form-control" id="validationCustom02" placeholder="Intitulé" v-model="text" required>
      </div>
      <div class="col-md-4 mb-3">
        <label for="validationCustom02">Position</label>
        <input type="text" class="form-control" id="validationCustom02" placeholder="Position" v-model="position" required>
      </div>
    </div>
    <label for="validationCustom02">Réponses</label>
    <div class="form-check">
      <input class="form-check-input position-static" type="radio" name="blankRadio" id="blankRadio1" @click="checkBox(1)" aria-label="...">
      <input type="text" class="form-control"  placeholder="Réponse 1" v-model="rep1" required>
    </div>
    <div class="form-check">
      <input class="form-check-input position-static" type="radio" name="blankRadio" id="blankRadio1" @click="checkBox(2)" aria-label="...">
      <input type="text" class="form-control" placeholder="Réponse 2" v-model="rep2" required>
    </div>
    <div class="form-check">
      <input class="form-check-input position-static" type="radio" name="blankRadio" id="blankRadio1" @click="checkBox(3)" aria-label="...">
      <input type="text" class="form-control" placeholder="Réponse 3" v-model="rep3" required>
    </div>
    <div class="form-check">
      <input class="form-check-input position-static" type="radio" name="blankRadio" id="blankRadio1" @click="checkBox(4)" aria-label="...">
      <input type="text" class="form-control" placeholder="Réponse 4" v-model="rep4" required>
    </div>
  </form>
  
  <ImageUpload @file-change="getImage"></ImageUpload>
  
  <img v-if="imagedata != null" :src="imagedata" alt="uploaded image">

</template>

<script setup>
import ImageUpload from "./ImageUpload.vue";
import quizApiService from "@/services/QuizApiService";
import { useRouter } from 'vue-router'
import { ref, onMounted, watch } from 'vue';
import QuizApiService from "@/services/QuizApiService";

const imagedata = ref(null)
const title = ref("")
const text = ref("")
const position = ref("")
const rep1 = ref("")
const rep2 = ref("")
const rep3 = ref("")
const rep4 = ref("")
const isCorrect1 = ref(false)
const isCorrect2 = ref(false)
const isCorrect3 = ref(false)
const isCorrect4 = ref(false)




const router = useRouter()
const emit = defineEmits(['questionEdited','cancelEdit']);

function getImage(event){
  if (event == ''){
    imagedata.value = null
  } else {
    imagedata.value = event
  }
}

function checkBox(index){
  if (index == 1){
    isCorrect1.value = true
    isCorrect2.value = false
    isCorrect3.value = false
    isCorrect4.value = false
  }
  if (index == 2){
    isCorrect1.value = false
    isCorrect2.value = true
    isCorrect3.value = false
    isCorrect4.value = false
  }
  if (index == 3){
    isCorrect1.value = false
    isCorrect2.value = false
    isCorrect3.value = true
    isCorrect4.value = false
  }
  if (index == 4){
    isCorrect1.value = false
    isCorrect2.value = false
    isCorrect3.value = false
    isCorrect4.value = true
  }
}

function validateEdit(){
  let body = {
    "title":title.value,
    "text":text.value,
    "image":imagedata.value,
    "position":parseInt(position.value),
    "possibleAnswers":[
      {
        "text":rep1.value,
        "isCorrect":isCorrect1.value
      },
      {
        "text":rep2.value,
        "isCorrect":isCorrect2.value
      },
      {
        "text":rep3.value,
        "isCorrect":isCorrect3.value
      },
      {
        "text":rep4.value,
        "isCorrect":isCorrect4.value
      }
    ]
  }
  
  let payload = QuizApiService.addQuestion(body);
  payload.then(() => {
    emit('questionEdited', true)
  })
}

function cancelEdit(){
  emit("cancelEdit",true)
}

const props = defineProps({
  currentQuestion: Object
});






</script>