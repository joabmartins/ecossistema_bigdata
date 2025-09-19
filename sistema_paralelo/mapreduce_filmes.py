# import as bibliotecas
# import install pandas collections matplotlib
import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt

# lê os dados do csv em um dataframe do pandas 
AVALIACOES_CSV_PATH = 'filmes.csv'
df_avaliacoes = pd.read_csv(AVALIACOES_CSV_PATH)
print(df_avaliacoes.head())

# 1. Fase Map (mapear)
def mapear(dataframe):
    return[(nota, 1) for nota in dataframe['Avaliacao']]

# 2.Fase Shuffle (agrupar)
def agrupar(dados_mapeados):
    agrupado = defaultdict(list)
    for chave, valor in dados_mapeados:
        agrupado[chave].append(valor)
    return agrupado

# 3.Fase de reduce (reduzir)
def reduzir(dados_agrupados):
    reduzido = {}
    for chave, valores in dados_agrupados.items():
        reduzido[chave] = sum(valores)
    return reduzido

# 4. visualizar os resultados
def exibir_grafico(dados_reduzidos):
    notas = list(dados_reduzidos.keys())
    totais = list(dados_reduzidos.values())

    plt.figure(figsize=(10, 6))
    plt.bar(notas, totais, color='#3b36a3')

    plt.title('Distribuição de Notas dos Filmes', fontsize=16)
    plt.xlabel('Nota')
    plt.ylabel('Total de Filmes')

    plt.show()

# 4.Fase de mapeamento
dados_mapeados = mapear(df_avaliacoes)
print(dados_mapeados[0:5])
# Fase de agrupamento
dados_agrupados = agrupar(dados_mapeados)
print(dados_agrupados)
# Fase de redução
dados_reduzidos = reduzir( dados_agrupados)
print(dados_reduzidos)
#Exibe o gráfico de barras
exibir_grafico(dados_reduzidos)

  