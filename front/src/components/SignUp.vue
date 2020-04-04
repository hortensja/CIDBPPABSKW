<template>
<div class="modal" v-bind:class="{'is-active': sharedState.showSignup}">
  <div class="modal-background" v-on:click="sharedState.showSignup = 0"></div>
  <div class="modal-content">
        <div class="box">
        <div class="field">
        <label class="label">Psuedonim</label>
            <div class="control">
                <input v-model="privateState.username" class="input" type="text" placeholder="np. Piotr" v-bind:class="{'is-danger': privateState.clicked ? privateState.username.length == 0 : false}">
            </div>
        </div>

        <div class="field">
        <label class="label">Hasło</label>
            <div class="control">
                <input v-model="privateState.password" class="input" type="password" placeholder="np. masło">
            </div>
        </div>

        <div class="field">
        <label class="label"> Powtórz hasło</label>
            <div class="control">
                <input v-model="privateState.repeatedPassword" class="input" type="password" placeholder="np. masło" v-bind:class="{
                'is-danger': privateState.password != privateState.repeatedPassword, 
                'is-success': privateState.password.length > 0 ? privateState.password == privateState.repeatedPassword : false}
                ">
            </div>
        </div>
        <div class="container">
            <a class="button is-success" v-on:click="privateState.clicked = true">
            Zarejestruj się!
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
            privateState: { username: "",
                            password: "",
                            repeatedPassword: "",
                            clicked: false
                            }
        }
    }
}
</script>