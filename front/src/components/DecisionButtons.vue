<template>
<div>
    <div class="columns">
        <div class="column">
            <a class="button is-danger is-large"  v-on:click="privateState.chooseDate = 1; sharedState.hideMap = true">
            <strong><a class="title is-3">Idę po piwo</a></strong>
            </a>
        </div>
        <div class="column">
            <a class="button is-success is-large" v-on:click="sharedState.isDone=true">
            <strong><a class="title is-3">Wróciłem z piwem</a></strong>
            </a>
        </div>
    </div>

    <div class="modal" v-bind:class="{'is-active': privateState.chooseDate}">
    <div class="modal-background" v-on:click="privateState.chooseDate = 0; sharedState.hideMap = 0;"></div>
    <div class="modal-content">
            <div class="box">
            <div class="field">
                <input type="time"/>
            </div>
            <div class="container">
                <a class="button is-success" v-on:click="sharedState.showPredictions = 1; sharedState.hideMap = 0;">
                Ok
                </a>
            </div>
            </div>
    </div>
    <button class="modal-close is-large" aria-label="close"></button>
    </div>
</div>
</template>

<script>
import store from "../store"
export default {
    data: function()  { 
        return {
            sharedState: store.state,
            privateState: { chooseDate: false }
        }
    }
}
</script>