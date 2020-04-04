<template>
        <div class="has-text-centered" v-bind:class="{'is-hidden': !sharedState.isDone}">
            <strong><a class="title">K thx bai</a></strong>
        </div>

</template>

<script>
import store from  "../store"
export default {
    data: function() {
        return {
        sharedState: store.state,
        privateState: {}
        }
    }
}
</script>