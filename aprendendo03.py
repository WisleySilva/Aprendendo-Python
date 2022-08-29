#Criar um programa que leia o sexo da pessoa, mas so aceite os valores M e F.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

r = 'M'

while r == 'M' or 'F':
    r = str(input("Qual o seu sexo? [M/F]")).upper()
    if r == 'M':
        print("voce é do sexo masculino")
        break
    elif r == 'F':
        print("voce é do sexo feminino")
        break
    else:
        print("digite o valor correto")
    