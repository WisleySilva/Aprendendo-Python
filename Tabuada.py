while True:
    num =  int(input("Digite um numero para ver a tabuada: "))
    print('-'*30)
    for x in range(1, 11):
        print(f"{num} X {x} = {num*x}")
    print('-'*30)
    if num == "sair":
        break

    
#print(f'A soma dos {cont} numeros é {soma}')