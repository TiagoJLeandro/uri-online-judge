"""
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.

"""

numero = int(input())
numeros_impares = []

while len(numeros_impares) < 6:
    if numero % 2 != 0:
        numeros_impares.append(numero)
        print(numero)
    numero += 1
