
#dados de entrada
frase="This is an apple. Apple is red in collor."

#1.fase de mapeamento
pares_mapeados= []
for palavra in frase.lower().replace('.', '').split():
    pares_mapeados.append((palavra, 1))
print("--- resultado do mapeamento ---")
print(pares_mapeados)

#2.fase de agrupamento
grupos_embaralhados = {}
for chave, valor in pares_mapeados:
    if chave not in grupos_embaralhados:
        grupos_embaralhados[chave]= []
    grupos_embaralhados[chave].append(valor)
print("\n resultado do agrupamento:")
print(grupos_embaralhados)

#3.fase de reduce(reduzir)
frequencia_palavras ={}
for chave, lista_valores in grupos_embaralhados.items():
    frequencia_palavras[chave] = sum(lista_valores)
print("\n ---resultado da redução---")
print(frequencia_palavras)

#