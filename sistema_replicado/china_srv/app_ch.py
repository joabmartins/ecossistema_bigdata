import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv( '/data/dados.csv' )

# Imprime o DataFrame para confirmar
print( "---Dados lidos com sucesso na China!" )
print( df )