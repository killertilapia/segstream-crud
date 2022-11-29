<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="row">
    <div class="col-2">
      <ul>
        <li><RouterLink to="/">Home</RouterLink></li>
        <li><RouterLink to="/logs">Logs</RouterLink></li>
      </ul>
    </div>
    <div class="col-10">
      <RouterView />
    </div>
  </div>
</template>


