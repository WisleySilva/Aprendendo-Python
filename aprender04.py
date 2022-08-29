#Desafio acertar o numero que a maquina sorteou de 1, 10

import random

numero_aleatorio = random.randint(1,10)

print(numero_aleatorio)
numero_usuario = 0
cont = 0
while numero_usuario != numero_aleatorio:
    numero_usuario = int(input('\033[34mTente acertar o número aleatório: \033[m'))
    if numero_usuario == numero_aleatorio:
        print('\033[34m*\033[m'*50)
        print(f"\033[32mVoce acertou, o número sorteado foi {numero_aleatorio} \033[m")
        cont = cont + 1
        print (f"\033[32mVocê fez o total de {cont} tentativas\033[m")
        print('*'*50)
        break
    else:
        print('\033[31m*\033[31m'*50)
        print(' Tente novamente!!')
        print('*'*50)
        cont = cont + 1

        