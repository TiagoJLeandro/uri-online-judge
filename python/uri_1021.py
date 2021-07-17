"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
Entrada

O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
Saída

Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

"""

from decimal import Decimal


def troco():
    valor = float(input())
    cedulas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    print("NOTAS:")
    for c in cedulas:
        quantidade = int(valor//c)
        valor -= c * quantidade
        print(f"{quantidade} nota(s) de R$ {c:.2f}")

    
    valor = round(valor, 2)
    print("MOEDAS:")
    for m in moedas:
        quantidade = int(Decimal(f'{valor}')//Decimal(f'{m}'))
        valor = round(valor - m * quantidade, 2)
        print(f"{quantidade} moeda(s) de R$ {m:.2f}")
    return

troco()
