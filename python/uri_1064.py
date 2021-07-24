"""

Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.
Entrada

A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.
Saída

O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.

"""

numeros_positivos = []
for index in range(1, 7):
    num = float(input())
    numeros_positivos.append(num) if num > 0 else None

media = sum(numeros_positivos)/len(numeros_positivos)
print(f"{len(numeros_positivos)} valores positivos")
print(f"{media:.1f}")
