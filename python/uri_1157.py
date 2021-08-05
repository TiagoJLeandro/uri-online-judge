"""
Ler um número inteiro N e calcular todos os seus divisores.
Entrada

O arquivo de entrada contém um valor inteiro.
Saída

Escreva todos os divisores positivos de N, um valor por linha.

"""

def mostrar_divisores():
    numero = int(input())
    for n in range(1, numero + 1):
        print(n) if not numero % n else None

mostrar_divisores()
