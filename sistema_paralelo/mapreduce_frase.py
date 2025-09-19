frase = "This is an Apple. Apple is red in color."

# 1. Fase de Mapeamento
pares_mapeados = []
for palavra in frase.lower().replace('.', '').split():
    pares_mapeados.append((palavra, 1))
print("--- Resultado do mapeamento ---")
print(pares_mapeados)

# 2. Fase Agrupamento
grupos_embaralhados = {}
for chave, valor in pares_mapeados:
    if chave not in grupos_embaralhados:
        grupos_embaralhados[chave] = []
    grupos_embaralhados[chave].append(valor)
print("\n --- Resultado do agrupamento: ---")
print(grupos_embaralhados)

# 3. Fase de Redução
frequencia_palavras = {}
for chave, lista_valores in grupos_embaralhados.items():
    frequencia_palavras[chave] = sum(lista_valores)
print("\n --- Resultado da redução ---")
print(frequencia_palavras)