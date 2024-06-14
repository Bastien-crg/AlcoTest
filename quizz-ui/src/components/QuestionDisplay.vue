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
    
    <div v-for="choice in props.currentQuestion.possibleAnswers">
        <a @click="emit('answer-clicked', choice.text)">{{choice.text}}</a>
    </div>
</template>

<script setup>



const props = defineProps({
  currentQuestion: Object
});


const emit = defineEmits(['answer-clicked']);

</script>

<style>
</style>