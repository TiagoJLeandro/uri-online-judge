"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
Entrada

O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
Saída

Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

"""


def calcular_troco():
    valor = int(input())
    print(valor)
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    for cedula in cedulas:
        numero_de_cedulas = valor//cedula
        valor -= numero_de_cedulas * cedula
        print(f"{numero_de_cedulas} nota(s) de R$ {cedula},00")

calcular_troco()
