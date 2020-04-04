<template>
<nav class="navbar" role="navigation" aria-label="main navigation">

  <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
          Ostatnie Biedronki
        </a>

        <div class="navbar-dropdown">
          <a href="" class="navbar-item">1</a>
          <a href="" class="navbar-item">2</a>
          <a href="" class="navbar-item">3</a>
          <a href="" class="navbar-item">4</a>
        </div>
      </div>
 

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <a class="button is-danger" v-on:click="sharedState.showSignup = 1;">
            <strong>Rejestracja</strong>
          </a>
          <a class="button is-light" v-on:click="sharedState.showLogin = 1;">
            Logowanie
          </a>
        </div>
      </div>
    </div>
  </div>
</nav>
</template>

<script>
import store from "../store.js"
export default {
    name: 'navbar',
    data: function () {
        return {
            sharedState: store.state,
            privateState: {}
        }
    }
}
</script>