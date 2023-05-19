<template>
    <div>
        <img :src="image">
        <h1>Badulaque Enterprise</h1>
    </div>
</template>

<script>
import image from "../assets/Logo.png"

export default {
    name: 'heading',
    data: function () {
        return {
            image: image
        }
    }
}
</script>

<style scoped>
@font-face {
  font-family: 'montserrat';
  src: local("Montserrat"),
  url(../assets/fonts/Montserrat-Regular.ttf)format("truetype");
}

*{
    margin:0px;
    padding: 0px;
    font-family: montserrat;
    color: #2F4036;
}

div {
    padding: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #F0E8DD;
}

img {
    width: 70px;
    height:70px;
    margin-right: 20px;
}
</style>