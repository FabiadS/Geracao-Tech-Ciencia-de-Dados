#cria chaves em duas situações: criar chaves no dicicionário e só colocar ela lá, sem nennhum valor; 
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

#criar um conjunto de chaves e quer colocar um valor padrão nela
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)