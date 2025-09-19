import pandas as pd
#carregar p arquivo csv
df = pd.read_csv('/data/dados.csv')
#imprime o dataframe para confirmar
print("---Dados lidos com sucesso!!")
print(df)