<template>
    <div class="list" v-bind:class="{'is-hidden': sharedState.isDone | !sharedState.showPredictions}">
        <div class="list-item">
            <div class="columns has-text-centered">
                <div class="column">
                    Data
                </div>
                <div class="column">
                    Predykcja
                </div>
            </div>
        </div>
        <div class="list-item" v-for="timedPrediction of sharedState.predictions" :key="timedPrediction">
            <div class="columns has-text-centered">
                <div class="column" >
                    {{ timedPrediction[0] }}
                </div>
                <div class="column">
                    {{ timedPrediction[1] }}
                </div>
            </div>
        </div>
        <div class="list-item">
            <div class="columns has-text-centered">
                <div class="column">
                <a class="button is-danger" v-on:click="sharedState.showPredictions = false;">
                    Inny termin
                </a>
                </div>
                <div class="column">
                <a class="button is-success" v-on:click="sharedState.isDone = true;">
                    Potwierdź wyjście 
                </a>  
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import store from "../store"

export default {
    data: function() {
        return {
            sharedState: store.state,
            privateState: {}
        }
    }
}
</script>