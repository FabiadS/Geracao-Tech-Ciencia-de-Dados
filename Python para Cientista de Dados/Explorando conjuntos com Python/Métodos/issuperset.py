conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # todos os alementos de 'b' estão no subconjunto de 'a' ?
print(resultado) # False

resultado = conjunto_b.issubset(conjunto_a)  # todos os elementos de 'a' estão no subconjunto de 'b' 
print(resultado) # True