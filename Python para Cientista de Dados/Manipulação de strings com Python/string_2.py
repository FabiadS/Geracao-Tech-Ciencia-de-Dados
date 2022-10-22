nome = "Fabiola"
idade = 21
profissao = "Estudante"
linguagem = "Python"

dados = {"nome": "Fabiola", "idade": 21}

# Old styel %
print("Nome: %s Idade: %d" %(nome, idade))

# Método format
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

# Método f-string
print(f'Meu nome é {nome} e tenho {idade} anos')