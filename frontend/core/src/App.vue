<script setup lang="ts">
import { ref } from 'vue';
import Navbar from '@/components/Navbar.vue'
</script>

<template>
  <header>
    <Navbar />
  </header>
  <main>
    <RouterView />
  </main>
</template>

<style scoped>
</style>
