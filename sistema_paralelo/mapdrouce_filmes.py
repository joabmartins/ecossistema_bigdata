import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt

AVALIACOES_CSV_PATH = 'filmes.csv'
df_avaliacoes = pd.read_csv(AVALIACOES_CSV_PATH)
print(df_avaliacoes.head())
#1. fase map (mapear)
def mapear(dataframe):
    return[(rating, 1) for rating in dataframe['Avaliacao']]
#2. fase shuffle (agrupar)
def agrupar(dados_mapeados):
    agrupado = defaultdict(list)
    for chave, valor in dados_mapeados:
        agrupado[chave].append(valor)
    return agrupado
#3. fase reduce (resduzir)
def reduzir(dados_agrupados):
    reduzido = {}
    for chave, valores in dados_agrupados.items():
        reduzido[chave] = sum(valores)
    return reduzido

def exibir_graficos(dados_reduzidos):
    notas = list(dados_reduzidos.keys())
    totais = list(dados_reduzidos.values())

    plt.figure(figsize=(10,6))
    plt.bar(notas, totais, color='#3E99CC')
    plt.title('dsitribuição de notas dos filmes', fontsize=16)

    plt.xlabel('nota')
    plt.ylabel('total de filmes')
    plt.show()

#Fase de mapeamento
dados_mapeados = mapear(df_avaliacoes)
print(dados_mapeados[0:5])
#fase agroup
dados_agrupados = agrupar(dados_mapeados)
print(dados_agrupados)
#fase de redução
dados_reduzidos = reduzir(dados_agrupados)
print(dados_reduzidos)
#exibe o grafico de barras
exibir_graficos(dados_reduzidos)