from random import randint


v = 0
m = 0
while True:
    print("=-"*30)
    print("Vamos jogar Par ou Impar")
    print("=-"*30)
    num = int(input('Digite um valor: '))
    x = randint(0, 10)
    soma = x + num
    par_impar = ' '
    
    while par_impar not in 'PI':
        par_impar = input('Par ou impar[P/I]: ').strip().upper()[0]
    print("-"*30)
    print(f'Você jogou {num} e a máquina jogou {x}. Total de {soma}')
    print("-"*30)
        

    if par_impar == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU')
            v += 1
        else:
            print("A maquina venceu")
            break
    elif par_impar == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENCEU')
            v += 1
        else:
            print("A maquina venceu")
            break
    print("Vamos jogar novamente...")

print(f'GAME OVER você venceu {v} vezes')


