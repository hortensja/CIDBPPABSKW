<template>
   <div v-bind:class="{'is-hidden': sharedState.isDone | sharedState.showPredictions}">
    <Map/>

   </div> 
</template>

<script>
import Map from "./Map"

import store from "../store.js"


export default {
    components: {
        Map
    },
    data: function() {
        return {
            sharedState: store.state,
            privateState: {}
        }
    }
}
</script>

<style scoped>

</style>