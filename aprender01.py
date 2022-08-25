#Exibir na tela as quatros operações aritiméticas entre dois números
"""
print("*"*50)

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
print("*"*50)
soma = num1 + num2
subt = num1 - num2
mult = num1 * num2
divi = num1 / num2

print(f"A soma entre os dois números é: {soma}")
print(f"A subtração entre os dois números é: {subt}")
print(f"A multiplicação entre os dois números é: {mult}")
print(f"A divisão entre os dois números é: {divi}")

print("*"*50)

#Aumentar o salário em Porcentagem

salario = int(input("Digite o valor do salario: "))
aumento_porcent = int(input("Quantos % você quer aumentar? "))

novo_salario = salario*(1 + aumento_porcent/100)

print(f"O novo salario será de {novo_salario}")

print("*"*50)


#Calcular o desconto de um produto
print(f"Senhor cliente, nos estamos com uma super promoção de 15% de desconto")
tv = 950
desc = 15
novo_preco = tv * (1 - desc/100)
print(f"Nossa linda Smart TV com 15% OFF por apenas: R$:{novo_preco}")
"""

import time

print("*"*50)
print("*"*50)
print("*"*50)

#Fazer uma contagem regressiva para a virada do ano

for contagem in range(10, -1, -1):
    time.sleep(1)
    print(contagem)

print("Feliz ano novo!!🎆🎆🎆")

for par in range(0, 50, 2):
    print(par)

print(par)