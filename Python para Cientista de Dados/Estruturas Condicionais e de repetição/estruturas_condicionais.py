MAIOR_IDADE = 18
IDADE_ESPECIAL = 171

idade = int(input("Informe a sua idade: "))

#IF
if idade >= 18:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


# IF ELSE
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")

# IF ELIF ELSE
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas mas não pode fazer aulas práticas")
else:
    print("Ainda não pode tirar a CNH.")