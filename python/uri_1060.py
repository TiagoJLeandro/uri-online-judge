"""
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.
Entrada

Seis valores, negativos e/ou positivos.
Saída

Imprima uma mensagem dizendo quantos valores positivos foram lidos.

"""

numeros_de_positivos = 0

for loop in range(6):
    numero = float(input())
    numeros_de_positivos += 1 if numero > 0 else 0

print(f"{numeros_de_positivos} valores positivos")
