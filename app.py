from flask import Flask, jsonify, render_template, request, redirect

app = Flask(__name__)

# Lista de tarefas (temporária, na memória)
tarefas = []


@app.route('/')
def index():
    # Mostra a página HTML e envia a lista de tarefas para ela
    return render_template('index.html', lista_de_tarefas=tarefas)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    # Pega o que foi digitado no formulário
    nova_tarefa = request.form.get('tarefa')

    if nova_tarefa:
        tarefas.append(nova_tarefa)

    # Volta para a página inicial
    return redirect('/')

@app.route('/deletar/<int:indice>')
def deletar(indice):
    # Verifica se o índice existe para não dar erro
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)  # Remove o item naquela posição
        
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
