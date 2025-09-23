# importar as bibliotecas
import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt


# lê os dados do csv em um dataframe Pandas
AVALIACOES_CSV_PATH = 'filmes.csv'
df_avaliacoes = pd.read_csv(AVALIACOES_CSV_PATH)
print(df_avaliacoes.head())

# 1. Fase Map (mapear)
def mapear(dataframe):
    return [(nota, 1) for nota in dataframe['Avaliacao']]

# 2. Fase Shuffle (agrupar)
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

# Fase de mapeamento
dados_mapeados = mapear(df_avaliacoes)
print(dados_mapeados[0:5])
# Fase de agrupamento 
dados_agrupados = agrupar(dados_mapeados)
print(dados_agrupados[0:5])
# Fase de redução

dados_reduzidos = reduzir(dados_agrupados)
print(dados_reduzidos[0:5])

