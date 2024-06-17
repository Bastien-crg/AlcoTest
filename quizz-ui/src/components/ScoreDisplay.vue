<template>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-auto">
        <h1>Résultats</h1>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-auto">
        <div v-if="props.score.score >= 8">Bien joué {{ participationStorageService.getPlayerName() }} tu as un score de {{ props.score.score }} points</div>
        <div v-else-if="props.score.score >= 5">Pas trop mal {{ participationStorageService.getPlayerName() }} tu as un score de {{ props.score.score }} points</div>
        <div v-else >Bof bof, {{ participationStorageService.getPlayerName() }} tu as un score de {{ props.score.score }} points</div>
      </div>
    </div>
  </div>
  <br/>
  <br/>
  <br/>
  <br/>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-auto">
        <h1>Classement</h1>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-auto">
        <div v-for="scoreEntry in JSON.parse(participationStorageService.getParticipationScore()).scores" v-bind:key="scoreEntry.date">
          {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
        </div>
      </div>
    </div>
  </div>
  <br/>
  <br/>
  <br/>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-auto">
        <button @click="router.push('/')" type="button" class="btn btn-success">Retour</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import participationStorageService from "@/services/ParticipationStorageService";
import { useRouter } from 'vue-router'

const router = useRouter()



const props = defineProps({
score: Object
});


</script>

<style>
</style>