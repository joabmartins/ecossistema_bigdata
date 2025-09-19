import pandas as pd

#Carrega o arquivo CSV
df = pd.read_csv('/data/dados.csv')

#Imprime o Dataframe para confirmar
print("---Dados lidos com sucesso na China!")
print(df)