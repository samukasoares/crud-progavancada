<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
@font-face {
  font-family: 'montserrat';
  src: local("Montserrat"),
  url(./assets/fonts/Montserrat-Regular.ttf)format("truetype");
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}


*{
  font-family: montserrat;
  margin:0px;
  padding:0px;
}
</style>
