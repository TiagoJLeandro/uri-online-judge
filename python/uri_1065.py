"""

Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.
Entrada

O arquivo de entrada contém 5 valores inteiros quaisquer.
Saída

Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

"""

numeros_pares = []
for num in range(5):
    numero = int(input())
    numeros_pares.append(numero) if numero % 2 == 0 else None
print(f"{len(numeros_pares)} valores pares")