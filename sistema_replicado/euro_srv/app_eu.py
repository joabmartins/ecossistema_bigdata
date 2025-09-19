import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('/data/dados.csv')

# Imprime o Dataframe para confirmar
print("--- Dados lidos com sucesso na Europa!")
print(df)