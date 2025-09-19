import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt

AVALIACOES_CSV_PATH =  'filmes.csv'
df_avaliacoes = pd.read_csv(AVALIACOES_CSV_PATH)
print(df_avaliacoes.head())

# 1. Fase Map (mapear)
def mapear(dataframe):
    return [(rating, 1) for rating in dataframe['Avaliacao']]

# 2. Fase shuffle (agrupar)
def agrupar(dados_mapeados):
    agrupado = defaultdict(list)
    for chave, valor in dados_mapeados:
        agrupado[chave].append(valor)
    return agrupado

# 3. Fase Reduce (reduzir)
def reduzir(dados_agrupados):
    reduzido = {}
    for chave, valores in dados_agrupados.items():
        reduzido[chave] = sum(valores)
    return reduzido

def exibir_grafico(dados_reduzidos):
    notas = list(dados_grupados.keys())
    totais = list(dados_reduzidos.values())

    plt.figure(figsize=(10, 6))
    plt.bar(notas, totais, color='#3E99CC')

    plt.title('Distribuição de Notas dos Fimes', fontsize=16)
    plt.xlabel('Nota')
    plt.ylabel('Total de filmes')

    plt.show()

# Fase de mapeamento 
dados_mapeados = mapear(df_avaliacoes)
print(dados_mapeados[0:5])
#Fase de agrupamento
dados_grupados = agrupar(dados_mapeados)
print(dados_grupados)
#Fase de redução
dados_reduzidos = reduzir(dados_grupados)
print(dados_reduzidos)
#Exibe o gráfico de barras
exibir_grafico(dados_reduzidos)
