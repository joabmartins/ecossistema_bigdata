#importar as bibliotecas
#pip install para as bibliotecas
import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt

#le os dados do csv em dataframe pandas
AVALIACOES_CSV_PATH = 'filmes.csv'
df_avaliacoes = pd.read_csv(AVALIACOES_CSV_PATH)
print(df_avaliacoes.head())

#1. fase map(mapear
def mapear(dataframe):
    return[(nota, 1)for nota in dataframe['Avaliacao']]

#2. fase shuf(agrupar)
def agrupar(dados_mapeados):
    agrupado = defaultdict(list) 
    for chave, valor in dados_mapeados:
        agrupado[chave].append(valor)
    return agrupado

#3. fase reduce(reduzir)
def reduzir(dados_agrupado):
    reduzido = {}
    for chave, valores in dados_agrupado.items():
        reduzido[chave ] =sum(valores)
    return reduzido

#vizualizar os resultados
def exibir_grafico(dados_reduzidos):
    notas = list(dados_reduzidos.keys())
    totais = list(dados_reduzidos.values())

    plt.figure(figsize=(10, 6))
    plt.bar(notas, totais, color= '#eb5ba8')

    plt.title('distribuição de notas dos filmes', fontsize=16)
    plt.xlabel('Nota')
    plt.ylabel('total de filmes')

    plt.show()

#fase de mapeamento
dados_mapeados = mapear(df_avaliacoes)
print(dados_mapeados[0:5])
#fase de agrupamento
dados_agrupado = agrupar(dados_mapeados)
print(dados_agrupado)
#fase de redução
dados_reduzidos = reduzir(dados_agrupado)
print(dados_reduzidos)
#exibe o grafico
exibir_grafico(dados_reduzidos)