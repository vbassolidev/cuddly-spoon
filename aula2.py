import random

def inserir(lista):
    print(f"Lista atual: {lista}")    
    posicao = int(input("Escolha uma posição da lista que deseja inserir um número: "))
    numero = int(input("Digite um novo número a ser inserido: "))

    lista.append(0)
    ##for i in range(posicao, len(lista) - 1):
    for i in range(len(lista) - 1, posicao, -1):
        lista[i] = lista [i-1]
    lista[posicao] = numero
    print(f"Lista final: {lista}")
    return lista

lista = []
length = 15

for i in range(length):
        idx = random.randint(1, 200)
        lista.append(idx)

nova_lista = inserir(lista)