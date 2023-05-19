<template>
    <div>
        <heading />
        <navbar />
        <table>
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>Telefone</th>
                    <th>Email</th>
                    <th>Convidados</th>
                    <th>Data</th>
                    <th>Evento</th>
                    <th>Cardápio</th>
                    <th>Cerveja</th>
                    <th>Ação</th>
                </tr>
            </thead>

            <tbody>
                <tr v-for='evento in eventos' :key="evento">
                    <td>{{ evento.nome }}</td>
                    <td>{{ evento.telefone }}</td>
                    <td>{{ evento.email }}</td>
                    <td>{{ evento.convidados }}</td>
                    <td>{{ evento.data }}</td>
                    <td>{{ evento.evento }}</td>
                    <td>{{ evento.cardapio }}</td>
                    <td>{{ evento.cerveja }}</td>
                    <td>
                        <button @click="removerEvento(evento._id.$oid)">Remover</button>
                        <label>|</label>
                        <router-link :to="{name:'alterar', params: { id: evento._id['$oid']}}"><button>Alterar</button></router-link>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import navbar from './navbar.vue';
import heading from './heading.vue';
export default {
    components: {
        heading,
        navbar,
    },
    data() {
        return{
            eventos: [],
        }
    },
    created: function () {
        this.fetchEventoData()
    },
    methods: {
        fetchEventoData: function () {
            this.$http.get('http://localhost:5000/index').then(
                (response) => {
                    this.eventos = response.body
                },
                (response) => { }
            )
        },
        removerEvento(id) {
            this.$http.delete(`http://localhost:5000/delete/${id}`).then(
                response => {
                    console.log(response.body.mensagem);
                    this.fetchEventoData()
                },
                error => {
                    console.error(error);
                }
            );
        }
    }
}
</script>

<style scoped>

tr:nth-child(odd) {
  background-color: #f0e8dd; /* Cor da linha ímpar */
}

tr:nth-child(even) {
  background-color: transparent; /* Cor da linha par (transparente) */
}

table {
    border-collapse: collapse;
    width: 100%;
    padding:5px;
}

tr {
    text-align: center;
}

th {
    color: #f0e8dd;
    background-color: #425c4d;
    height: 40px;
    width: auto;

}

.selected {
    background-color: rgb(153, 153, 153);
}

button{
    background-color: transparent;
    border: none;
    font-size: 16px;
}

button:hover{
    color: red;
    cursor: pointer;
}

.container {
    width: 100%;
}
</style>