<template>
<div class="modal" v-bind:class="{'is-active': sharedState.showLogin}">
  <div class="modal-background" v-on:click="sharedState.showLogin = 0"></div>
  <div class="modal-content">
        <div class="box">
        <div class="field">
        <label class="label">Psuedonim</label>
            <div class="control">
                <input v-model="privateState.username" class="input" type="text" placeholder="np. Piotr">
            </div>
        </div>

        <div class="field">
        <label class="label">Hasło</label>
            <div class="control">
                <input v-model="privateState.password" class="input" type="password" placeholder="np. masło">
            </div>
        </div>
        <div class="container">
            <a class="button is-success" v-on:click="sharedState.showLogin = 1;">
            Zaloguj się
            </a>
        </div>
        </div>
  </div>
  <button class="modal-close is-large" aria-label="close"></button>
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