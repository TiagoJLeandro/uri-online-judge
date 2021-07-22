"""
Faça um programa que mostre os números pares entre 1 e 100, inclusive.

Entrada
Neste problema extremamente simples de repetição não há entrada.

Saída
Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.

"""

for numero in range(0, 101):
    print(f"{numero}") if numero % 2 == 0 and numero > 0  else None