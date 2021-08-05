"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
Entrada

A entrada contem três números inteiros.
Saída

Imprima a saída conforme foi especificado.

"""

entrada = [int(num) for num in input().split()]

def ordenar(lista, _decrescente=False):
    lista = [*lista]
    if _decrescente:
        return decrescente(lista)
    return crescente(lista)

def crescente(lista):
    rodada_inicial = 0
    rodada_final = 1
    while rodada_inicial <= rodada_final:
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                maior = lista[i]
                menor = lista[i+1]
                lista[i+1] = maior
                lista[i] = menor
                rodada_final += 1

        rodada_inicial += 1

    return lista

def decrescente(lista):
    rodada_inicial = 0
    rodada_final = 1
    while rodada_inicial <= rodada_final:
        for i in range(len(lista)-1):
            if lista[i] < lista[i+1]:
                maior = lista[i+1]
                menor = lista[i]
                lista[i+1] = menor
                lista[i] = maior
                rodada_final += 1

        rodada_inicial += 1

    return lista

def mostrar_lista(lista):
    for i in range(len(lista)):
        print(lista[i])


mostrar_lista(ordenar(entrada))
print("")
mostrar_lista(entrada)
