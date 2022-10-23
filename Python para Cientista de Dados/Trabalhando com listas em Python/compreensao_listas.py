numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

# Filtro versão 1
for num in numeros:
  if(num % 2 == 0):
    pares.append(num)

print(f'Numeros: {numeros}')
print(f'Pares: {pares}')

# Filtro versão 2
pares = [num for num in numeros if num % 2 == 0] # retorno for iteração na lista numeros
print(pares)

# Modificando valor versão 1
quadrado = []

for num in numeros:
  quadrado.append(num ** 2)

print(quadrado)

# Modificando valor versão 2
quadrado = [num ** 2 for num in numeros]
print(quadrado)