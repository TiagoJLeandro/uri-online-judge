"""
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

"""

numeros = []

for i in range(100):
    num = int(input())
    numeros.append(num)

maior = max(numeros)
posicao = numeros.index(maior) + 1

print(maior)
print(posicao)
