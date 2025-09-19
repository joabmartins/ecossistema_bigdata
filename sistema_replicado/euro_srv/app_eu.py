import pandas as pd

# Carrega o arquivo csv
df = pd.read_csv('/data/dados.csv')

# Imprime o DataFrame para confirmar
print("---Dados lidos com sucesso na Europa!")
print(df)