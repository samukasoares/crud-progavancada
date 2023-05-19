from flask import json, request, jsonify
import flask
from bson import json_util
from app import app
from app import db
from bson.objectid import ObjectId


@app.route('/')
@app.route('/index')
def index():
    return flask.jsonify(json.loads(json_util.dumps(db.evento.find({}).sort("_id", 1))))

@app.route('/create', methods=['POST'])
def create():
    json_data = request.json
    if json_data is not None:
        db.evento.insert_one(json_data)
        return jsonify(mensagem='Evento adicionado com sucesso')
    else:
        return jsonify(mensagem='Erro ao adicionar  evento')

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    result = db.evento.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify(mensagem='Evento excluído com sucesso')
    else:
        return jsonify(mensagem='Erro ao excluir evento')
    
@app.route('/update', methods=['POST'])
def update():
    json_data = request.json
    if json_data is not None and db.evento.find_one({"_id": ObjectId(json_data.get("id"))}) is not None:
        db.evento.update_one({'_id': ObjectId(json_data.get("id"))}, {"$set": {'nome': json_data["nome"], 'telefone': json_data["telefone"], 'email':json_data["email"],'convidados':json_data["convidados"],'data':json_data["data"], "evento":json_data["evento"], "cardapio":json_data["cardapio"], "cerveja":json_data['cerveja']}})
        return jsonify(mensagem='evento atualizado')
    else:
        return jsonify(mensagem="evento nao atualizado")
    
@app.route("/getid/<string:id>")
def getid(id):
    evento = db.evento.find_one({"_id": ObjectId(id)})
    return flask.jsonify(json.loads(json_util.dumps(evento)))

    
