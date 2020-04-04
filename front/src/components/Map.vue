<template>
    <div class="container">
    <div class="columns is-centered  is-vcentered">
        <div class="column" v-bind:class="{'is-hidden': sharedState.showLogin | sharedState.showSignup | sharedState.hideMap } ">
            <div id="map">
            </div>
        </div>
        <div class="column">
            <p v-if="privateState.step == 0" class="title is-3">Znajdź swoją ulubioną biedronkem</p>
            <div v-else>
            <DecisionButtons/>
            </div>
        </div>
    </div>
    </div>
</template>

<script>
import L from "leaflet"
import store from "../store"
import DecisionButtons from "./DecisionButtons"

export default {
    components: {
        DecisionButtons
    },
    data: function() {
        return {
            sharedState: store.state,
            privateState: {}
        }
    },
    beforeMount: function() {
        this.privateState.step = 0;
    }, 

    mounted: function() {
            var map = L.map('map').setView([51.505, -0.09], 13);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);



            L.marker([51.5, -0.09]).addTo(map)
                .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
                .on('click', (e) => {this.privateState.step=1; this.sharedState.shop=e.latlng, this.$forceUpdate();});
    
    },

}
</script>

<style scoped>
.container {
    margin: 100px;
}
#map {
    padding-left: 100px;
    width: 600px;
    height: 600px;
    border-radius: 12px;
}
</style>