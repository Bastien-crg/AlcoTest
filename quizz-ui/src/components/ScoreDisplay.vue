<template>
  <div v-if="props.score.score >= 8">Bien joué {{ participationStorageService.getPlayerName() }} tu as un score de {{ props.score.score }} points</div>
  <div v-else-if="props.score.score >= 5">Pas trop mal {{ participationStorageService.getPlayerName() }} tu as un score de {{ props.score.score }} points</div>
  <div v-else >Bof bof, {{ participationStorageService.getPlayerName() }} tu as un score de {{ props.score.score }} points</div>

  
  
</template>

<script setup>
import participationStorageService from "@/services/ParticipationStorageService";


const props = defineProps({
score: Object
});


</script>

<style>
</style>