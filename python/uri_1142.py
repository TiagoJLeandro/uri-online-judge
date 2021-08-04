"""
Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.

"""

linhas = int(input()) * 4
pum = [
    "PUM\n" if num % 4 == 0 else f"{num} "
    for num in range(1, linhas + 1)
]
print("".join(pum).strip())
