cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez')

while True:
    num = int(input("Digite um valor entre 0 e 10: "))
    if 0 <= num <= 10:
        break
    print('Tente novamente. ', end='')

print(f'Você digitou o numero {cont[num]}')