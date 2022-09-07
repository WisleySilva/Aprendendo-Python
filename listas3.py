num = [[],[]]
temp = 0

for c in range(1, 8):
    temp = int(input(f'Digite o {c}º valor: '))

    if temp % 2 == 0:
        num[0].append(temp)
    if temp % 2 == 1:
        num[1].append(temp)
num[0].sort()
num[1].sort()
print(f'Os numeros pares são: {num[0]}')
print(f'Os numeros impares são: {num[1]}')
