# tenho uma lista principal irei adiconar números a esta lista.

lista = [1, 3, 5, 7, -2, -8]
print(lista)
print()

s = 0

newlista = list()

# irei fazer com que os números que eu digitar apareça em uma lista separada

while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        newlista.append(num)
    else:
        print('ERRO! Número já existe, adicione outro número.')

# faz com que a pergunta ao usuario se deseja continuar ou não

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

# o resultado da lista adicionada separada da principal

print(f'Os números {newlista} foram adicionados com Sucesso a lista!')

# faz com que a lista principal mais a lista adicionada sejam juntadas em uma só lista em ordem crescente.

s = newlista + lista
ordem = sorted(s)
print(f'A nova lista é composta por esses números {ordem}')
