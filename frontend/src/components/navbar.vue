<template>
    <div class="container">
        <ul>
            <router-link :to="{ name: 'create' }"><button class="botao">Adicionar Evento</button></router-link>
            <router-link :to="{ name: 'list' }"><button class="botao">Orçamentos Enviados</button></router-link>
        </ul>
    </div>
</template>

<style scoped>
.container{
    background-color: #F0E8DD;
    display: flex;
    justify-content: center;
}

.botao{
    background-color: #F0E8DD;
    border: none;
}

.botao:hover{
    cursor: pointer;
    font-weight: 800;
}

ul{
    display: flex;
    width: 100%;
    justify-content: space-around;
    padding: 5px;
}

li{
    list-style: none;
}

a{
    text-decoration: none;
}
</style>