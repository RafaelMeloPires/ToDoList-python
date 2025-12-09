import os
import json
from flask import Flask, jsonify, render_template, request, redirect

app = Flask(__name__)

# Nome do arquivo onde vamos salvar os dados
ARQUIVO_DB = 'tarefas.json'

# --- Funções Ajudantes (Para lidar com o arquivo) ---


def carregar_tarefas():
    """Lê o arquivo JSON e devolve a lista. Se não existir, devolve lista vazia."""
    if not os.path.exists(ARQUIVO_DB):
        return []
    try:
        with open(ARQUIVO_DB, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except:
        return []


def salvar_tarefas(lista):
    """Pega a lista atual e grava no arquivo JSON."""
    with open(ARQUIVO_DB, 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, indent=4)


# Lista de tarefas (temporária, na memória)
tarefas = []


@app.route('/')
def index():
    tarefas = carregar_tarefas()
    # Mostra a página HTML e envia a lista de tarefas para ela
    return render_template('index.html', lista_de_tarefas=tarefas)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    # Pega o que foi digitado no formulário
    nova_tarefa = request.form.get('tarefa')

    if nova_tarefa:
        # 1. Carrega a lista atual
        tarefas = carregar_tarefas()
        # 2. Adiciona o novo item
        tarefas.append(nova_tarefa)
        # 3. Salva no arquivo imediatamente
        salvar_tarefas(tarefas)

    # Volta para a página inicial
    return redirect('/')


@app.route('/deletar/<int:indice>')
def deletar(indice):
    # Verifica se o índice existe para não dar erro
    # 1. Carrega a lista atual
    tarefas = carregar_tarefas()

    # 2. Remove se o índice for válido
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        # 3. Salva a lista atualizada no arquivo
        salvar_tarefas(tarefas)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
