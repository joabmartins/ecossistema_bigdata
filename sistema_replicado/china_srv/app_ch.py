import pandas as pd

#Carregar o arquivo csv
df = pd.read_csv('/data/dados.csv')

#imprimi o data frame para confirmar
print("---Dados lidos com sucesso na China! ")
print(df)