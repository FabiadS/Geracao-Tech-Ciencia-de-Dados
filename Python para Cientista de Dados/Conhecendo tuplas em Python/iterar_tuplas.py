carros = ("gol","celta","palio",)

for carro in carros:
    print(carro)

#para saber o índice
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")