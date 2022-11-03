# se o atributo n existir, ele cria com o valor mandado, caso exista, retorna o valor que ja existe e n altera nada
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # vai adicionar a chave idade com o valor 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}