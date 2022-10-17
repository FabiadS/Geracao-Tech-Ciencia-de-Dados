# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True)
print(True and False)
print(True or True)
print(True or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp1)

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite) 
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

exp3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp3)