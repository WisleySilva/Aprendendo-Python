from math import factorial

valor_usuario = int(input('Digite um número para ver o fatorial: '))

fatorial = factorial(valor_usuario)

print(f'Calculando {valor_usuario}!: ', end='')

c = valor_usuario

while c > 0:
    print(f'{c} ', end='')
    print(' x ' if  c > 1 else ' = ' f'{fatorial}', end='')
    c -= 1
