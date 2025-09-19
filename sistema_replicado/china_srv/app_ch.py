import pandas as pd

#carregar o arquivo CSV
df = pd.read_csv('/data/dados.csv')

# Imprimir Dataframe para confirmar
print("---Dados lidos com sucesso na China!")
print(df)