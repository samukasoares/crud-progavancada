<template>
    <div class="tudo">
        <header>
            <heading />
            <navbar />
        </header>
        <h3>Alterar Evento</h3>
        <form v-on:submit.prevent="updateEvento" autocomplete="off">
            <div class="form-group">
                <label name="usuario_id">ID</label>
                <input type="text" disabled v-model="evento.id" id="evento_id" />
            </div>

            <div class="form-group">
                <label>Nome:</label>
                <input v-model="evento.nome" type="text">
            </div>

            <div class="form-group">
                <label>Telefone:</label>
                <input v-model="evento.telefone" type="tel">
            </div>

            <div class="form-group">
                <label>Email:</label>
                <input v-model="evento.email" type="email">
            </div>

            <div class="form-group">
                <label>Convidados:</label>
                <input v-model="evento.convidados" type="number">
            </div>

            <div class="form-group">
                <label>Data:</label>
                <input v-model="evento.data" type="date">
            </div>

            <div class="form-group">
                <label for="tipoE">Evento:</label>
                <select v-model="evento.evento" name="tipoE" id="tipoE">
                    <option value="Casamento">Casamento</option>
                    <option value="Debutante">15 anos</option>
                    <option value="Bodas">Bodas</option>
                    <option value="Empresa">Empresa</option>
                    <option value="Aniversário">Aniversário</option>
                </select>
            </div>

            <div class="form-group">
                <label for="cardapio">Cardápio:</label>
                <select v-model="evento.cardapio" name="cardapio" id="cardapio">
                    <option value="Bronze">Bronze</option>
                    <option value="Prata">Prata</option>
                    <option value="Ouro">Ouro</option>
                    <option value="Mineiro">Mineiro</option>
                    <option value="Churrasco">Churrasco Fatiado</option>
                    <option value="Coquetel">Coquetel</option>
                    <option value="Boteco">Boteco</option>
                </select>
            </div>

            <div class="form-group">
                <label for="cerveja">Cerveja:</label>
                <select v-model="evento.cerveja" name="cerveja" id="cerveja">
                    <option value="Brahma">Brahma</option>
                    <option value="Original">Original</option>
                    <option value="Heineken">Heineken</option>
                    <option value="Sem Cerveja">Sem Cerveja</option>
                </select>
            </div>
            <button>Alterar</button>
        </form>
    </div>
</template>
  
<script>
import heading from './heading.vue';
import navbar from './navbar.vue';

export default {
    name: 'index',
    data() {
        return {
            evento: {}
        }
    },
    created: function () {
        this.getLivroData()
    },
    components: {
        heading,
        navbar
    }, methods: {
        getLivroData: function () {
            this.$http.get('http://localhost:5000/getid/' + this.$route.params.id).then(
                (response) => {
                    this.evento.id = this.$route.params.id
                    this.evento.nome = response.body['nome']
                    this.evento.telefone = response.body['telefone']
                    this.evento.email = response.body['email']
                    this.evento.convidados = response.body['convidados']
                    this.evento.data = response.body['data']
                    this.evento.evento = response.body['evento']
                    this.evento.cardapio = response.body['cardapio']
                    this.evento.cerveja = response.body['cerveja']
                    this.$forceUpdate()
                },
                (response) => { }
            )
        },
        updateEvento: function () {
            this.$http.post('http://localhost:5000/update', this.evento, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(
                    (response) => {
                        this.evento = {}
                        alert(response.body['mensagem'])
                        this.$router.push('list')
                    },
                    (response) => {
                        alert(respose.body['mensagem'])
                    }
                )
        }
    }
};
</script>
  
<style scoped>

.body {
    background-color: #F0E8DD;
    max-width: 50%;
    width: 50%;
    padding: 15px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    border-radius: 5px;
    box-shadow: 2px 2px 2px #49494988;
}

form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin: 10px;
}

.form-group {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

h3 {
    margin: 10px;
}

label {
    width: 120px;
}

input,
select {
    margin-bottom: 10px;
    width: 85%;
    height: 30px;
    border-radius: 5px;
    border: 1px solid #425c4d;
}

input:focus,
select:focus {
    outline-style: none;
    border: 1px solid #e1c59c;
}


button {
    background-color: #e1c59c;
    border-radius: 5px;
    border: none;
    height: 30px;
}

button:hover {
    background-color: #425c4d;
    color: white;
    cursor: pointer;
}
</style>