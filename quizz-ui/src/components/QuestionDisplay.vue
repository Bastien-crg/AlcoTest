<template>
    <div>
      <h1>{{ props.currentQuestion.title }}</h1>
    </div>
    <br/>
    <div>
        {{ props.currentQuestion.text }}
    </div>
    <br/>
    <div>
        <img v-if="props.currentQuestion.image" :src="props.currentQuestion.image" />
    </div>
    <br/>
    
    <div v-for="choice,i in props.currentQuestion.possibleAnswers">
        <a @click="emit('answer-clicked', i+1)">{{choice.text}}</a>
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