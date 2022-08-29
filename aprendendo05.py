#Criar um programa que leia dois valores e mostre um menu na tela

print("Digite 2 números")
numero1 = int(input('1: '))
numero2 = int(input('2: '))

opcoes = 1
while opcoes != 0:
    print("*"*50)
    #print('O que você quer fazer com esses números?')
    print("[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa")
    print("*"*50)
    opcoes = input("O que você quer fazer com esses números? ")

    if  opcoes == "1": #OPÇÃO 1
        soma = numero1 + numero2
        print(soma)
    
    elif opcoes == "2": #OPÇÃO 2
        multiplica = numero1 * numero2
        print(multiplica)

    elif opcoes == "3": #OPÇÃO 3
        if numero1 > numero2:
            print(numero1)
        else: print(numero2)

    elif opcoes == "4": #OPÇÃO 4
        print("Digite os novos números")
        numero1 = int(input('1: '))
        numero2 = int(input('2: '))

    elif opcoes == "5": #OPÇÃO 5
        print("Até mais!!")
        break
    else:
        print("Selecione uma opção valida!")


