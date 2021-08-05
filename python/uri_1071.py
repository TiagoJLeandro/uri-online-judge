"""
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

"""

maior = int(input())
menor = int(input())

soma_dos_impares = 0
for numero in range(menor + 1, maior):
    soma_dos_impares += numero if numero % 2 else 0

print(soma_dos_impares)
