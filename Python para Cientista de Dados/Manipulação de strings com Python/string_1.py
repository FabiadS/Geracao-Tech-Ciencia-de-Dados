nome = "guilHerme"

print(nome.upper()) # coloca toda a string em maiúsculo
print(nome.lower()) # coloca toda a string em minúsculo
print(nome.title()) # coloca o primeiro caractere em maiúsculo e o resto em minúsculo

texto = "     Olá, Mundo!     "

print(texto)
print(texto.strip() + ".") # tira os espaços da direita e da esquerda
print(texto.lstrip() + ".") # tira os espaços da esquerda
print(texto.rstrip() + ".") # tira os espaços da direita

menu = "Python"

print(menu.center(14, "#"))
print("-".join(menu))