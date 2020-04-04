<template>
  <div id="bg" style="height=100vh">
      <NavBar class="has-background-warning"/>
      <MainBody/>
      <Login/>
      <SignUp/>
      <Predictions/>
      <ThxBai/>
  </div>
</template>

<script>

import MainBody from "./components/MainBody.vue"
import NavBar from "./components/NavBar.vue"
import ThxBai from "./components/ThxBai.vue"
import Predictions from "./components/Predictions.vue"
import Login from "./components/Login.vue"
import SignUp from "./components/SignUp.vue"

import store from "./store"


store.xd = true;

export default {
  name: 'App',
  data: function() {
    return {
      sharedState: store.state,
      privateState: {}
    }
  },
  components: {
    MainBody, NavBar, ThxBai, Predictions, Login, SignUp
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
};

  #bg { 
        background-color: red ;
        background-position: center center;
        background-repeat:  no-repeat;
        background-attachment: fixed;
        background-size:  cover;

 }


</style>
