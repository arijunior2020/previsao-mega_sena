from flask import Flask, render_template, request
import pandas as pd
import random
from itertools import combinations

app = Flask(__name__)

# Carregar dados
dados = pd.read_csv('dadosmega.csv')
todos_numeros = dados[['B1', 'B2', 'B3', 'B4', 'B5', 'B6']].values.flatten()
frequencia = pd.Series(todos_numeros).value_counts()

# Valores das apostas
valores_aposta = {
    6: 5.00,
    7: 35.00,
    8: 140.00,
    9: 420.00,
    10: 1050.00,
    11: 2310.00,
    12: 4620.00,
    13: 8580.00,
    14: 15015.00,
    15: 25025.00,
    16: 40040.00,
    17: 61880.00,
    18: 92820.00,
    19: 135660.00,
    20: 193800.00,
}

# Probabilidades
probabilidades = {
    6: {"Sena": 50063860, "Quina": 154518, "Quadra": 2332},
    7: {"Sena": 7151980, "Quina": 44981, "Quadra": 1038},
    8: {"Sena": 1787995, "Quina": 17192, "Quadra": 539},
    9: {"Sena": 595998, "Quina": 7791, "Quadra": 312},
    10: {"Sena": 238399, "Quina": 3973, "Quadra": 195},
    11: {"Sena": 108363, "Quina": 2211, "Quadra": 129},
    12: {"Sena": 54182, "Quina": 1317, "Quadra": 90},
    13: {"Sena": 29175, "Quina": 828, "Quadra": 65},
    14: {"Sena": 16671, "Quina": 544, "Quadra": 48},
    15: {"Sena": 10003, "Quina": 370, "Quadra": 37},
    16: {"Sena": 6252, "Quina": 260, "Quadra": 29},
    17: {"Sena": 4045, "Quina": 188, "Quadra": 23},
    18: {"Sena": 2697, "Quina": 139, "Quadra": 19},
    19: {"Sena": 1845, "Quina": 105, "Quadra": 16},
    20: {"Sena": 1292, "Quina": 81, "Quadra": 13},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar', methods=['POST'])
def gerar():
    quantidade = int(request.form['quantidade'])
    numeros_por_jogo = int(request.form['numeros_por_jogo'])
    
    # Verificar se o número de jogos é válido
    if numeros_por_jogo not in valores_aposta:
        mensagem = f"Quantidade de números inválida. Escolha entre: {', '.join(map(str, valores_aposta.keys()))}."
        return render_template('index.html', mensagem=mensagem)

    # Selecionar os números mais sorteados
    numeros_top = frequencia.head(20).index.tolist()
    todas_combinacoes = list(combinations(numeros_top, numeros_por_jogo))
    total_combinacoes = len(todas_combinacoes)

    # Validar se é possível gerar a quantidade de jogos solicitada
    if quantidade > total_combinacoes:
        mensagem = f"Não é possível gerar {quantidade} jogos. Máximo permitido: {total_combinacoes}."
        return render_template('index.html', mensagem=mensagem)

    # Gerar as combinações
    combinacoes = random.sample(todas_combinacoes, quantidade)

    # Calcular o custo total
    valor_total = valores_aposta[numeros_por_jogo] * quantidade

    # Obter as probabilidades
    probabilidade = probabilidades[numeros_por_jogo]

    # Renderizar a página de resultados com os dados gerados
    return render_template(
        'resultados.html',
        combinacoes=combinacoes,
        valor_total=valor_total,
        probabilidade=probabilidade,
        numeros_por_jogo=numeros_por_jogo
    )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
