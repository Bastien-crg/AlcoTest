<script setup>
import QuestionDisplay from "../components/QuestionDisplay.vue"

const question = {
    text: "Quelle est la couleur du cheval blanc d'Henry IV ?",
    title: "Dummy Question",
    image: "falseb64imagecontent",
    position: 1,
    possibleAnswers: [
        {
            text: "Noir",
            isCorrect: false 
        },
        {
            text: "Gris",
            isCorrect: false
        },
        {
            text: "Blanc",
            isCorrect: true
        },
        {
            text: "La réponse D",
            isCorrect: false
        }
    ]
}

function callback(event) {
  console.log(event)
}

</script>

<template>
  <div>
    <h1>Question Manager</h1>
  </div>
  <br/>
  <QuestionDisplay :currentQuestion="question" @answer-clicked="callback"></QuestionDisplay>
  

</template>



<style>
</style>
