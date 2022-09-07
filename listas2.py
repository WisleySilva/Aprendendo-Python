galera = []
dado = []
sair = ''
mai = men = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    
    if len(galera) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
            
    galera.append(dado[:])       
    dado.clear()

   
    
    sair = str(input('Você deseja continuar? [S/N] ')).upper()
    while sair not in 'SN':  
        sair = str(input(('Digite um valor valido: [S/N]'))).upper()
    
    if sair == 'N':
        break
print('='*50)
print(f'Você cadastrou o total de {len(galera)} Pessoas')


print(f'O maior peso foi o de {mai}kg. Peso de ', end='')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print('\n')
print(f'O menor foi o de {men}kg. Peso de ',end='')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print('\n')
print('='*50)
print('\n')
print(galera)