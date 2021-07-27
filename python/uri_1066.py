"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

"""

numeros_impares = []
numeros_pares = []
numeros_positivos = []
numeros_negativos = []

for i in range(5):
    numero = int(input())
    numeros_pares.append(numero) if numero % 2 == 0 else None
    numeros_impares.append(numero) if numero % 2 != 0 else None
    numeros_positivos.append(numero) if numero > 0 else None
    numeros_negativos.append(numero) if numero < 0 else None

print(f"{len(numeros_pares)} valor(es) par(es)")
print(f"{len(numeros_impares)} valor(es) impar(es)")
print(f"{len(numeros_positivos)} valor(es) positivo(s)")
print(f"{len(numeros_negativos)} valor(es) negativo(s)")
