<template>
  <button type="button" class="btn btn-success" @click="editQuestion(question)" >Valider</button>
  <form class="needs-validation" novalidate>
  <div class="form-row">
    <div class="col-md-4 mb-3">
      <input type="text" class="form-control" id="validationCustom01" placeholder="First name" value="Mark" required>
      <div class="valid-feedback">
        Looks good!
      </div>
    </div>
    <div class="col-md-4 mb-3">
      <input type="text" class="form-control" id="validationCustom02" placeholder="Last name" value="Otto" required>
      <div class="valid-feedback">
        Looks good!
      </div>
    </div>
  </div>
  <div class="form-row">
    
  </div>
  
</form>
</template>

<script setup>

import quizApiService from "@/services/QuizApiService";
import { useRouter } from 'vue-router'



const router = useRouter()
const emit = defineEmits(['questionDeleted']);


function isActive(answer){
  if (answer.isCorrect){
    return "list-group-item active"
  } else {
    return "list-group-item"
  }
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