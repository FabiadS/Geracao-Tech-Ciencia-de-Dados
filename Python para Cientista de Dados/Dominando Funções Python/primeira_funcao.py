def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2("Fabiola")
exibir_mensagem_3() #como foi adicionado na funcao o valor do parametro, n é necessário colocar aqui
exibir_mensagem_3(nome="Chappie")