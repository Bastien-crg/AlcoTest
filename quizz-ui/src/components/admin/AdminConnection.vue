<script setup>
import { ref, onMounted } from 'vue';
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";


const password = ref("")
const wrong_password_flag = ref(false);
const emit = defineEmits(['isToken']);


function login(){
  let payload = quizApiService.login(password.value)
  payload.then(payload => {
    if (payload != undefined){
      participationStorageService.saveToken(payload.data.token)
      emit('isToken', true)
    } else {
      wrong_password_flag.value = true
    }
    
  })
  
}

</script>


<template>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <div v-if="wrong_password_flag">Mauvais mot de passe</div>
    <input type="password" class="form-control" v-model="password" placeholder="Password">
  </div>
  <button class="btn btn-primary" @click="login()" >Submit</button>
    
</template>

<style>



</style>