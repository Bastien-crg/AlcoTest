<template>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-auto">
        <h1>{{ props.currentQuestion.title }}</h1>
      </div>
    </div>
  </div>
  <br/>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-auto">
        {{ props.currentQuestion.text }}
      </div>
    </div>
  </div>
  <br/>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-auto">
        <img v-if="props.currentQuestion.image" :src="props.currentQuestion.image" />
      </div>
    </div>
  </div>
  <br/>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-auto" v-for="choice,i in props.currentQuestion.possibleAnswers">
        <button @click="emit('answer-clicked', i+1)" type="button" class="btn btn-success">{{choice.text}}</button>
      </div>
    </div>
  </div>
</template>

<script setup>

function getAnswerIndex(answer){
  for (let i = 0; i < props.currentQuestion.possibleAnswers.length; i++) {
    if (props.currentQuestion.possibleAnswers[i].text == answer){
      return i+1;
    }
  }
  return -1;
}



const props = defineProps({
  currentQuestion: Object
});


const emit = defineEmits(['answer-clicked']);



</script>

<style>
</style>