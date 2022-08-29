#criar um contador até 500, ver quais numeros sao divisiveis por 3 e somar todos eles

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f"a soma de todos os numeros é {soma}")
print(cont)

print("*"*50)
print("*"*50)

#Criando uma tabuada

num =  int(input("Digite um numero para ver a tabuada: "))
for x in range(1, 11):
    print(f"{num} X {x} = {num*x}")


print("*"*50)
print("*"*50)

