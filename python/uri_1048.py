"""
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário 	Percentual de Reajuste

0 - 400.00
400.01 - 800.00
800.01 - 1200.00
1200.01 - 2000.00
Acima de 2000.00

15%
12%
10%
7%
4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.
Entrada

A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
Saída

Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.

"""

salario = float(input())
reajustes = {
    15: {"min": 0, "max": 400.00},
    12: {"min": 400.01, "max": 800.00},
    10: {"min": 800.01, "max": 1200.00},
    7: {"min": 1200.01, "max": 2000.00},
    4: {"min": 2000.01, "max": "unlimited"}
}
for percent, min_max in reajustes.items():
    maximo = salario if min_max["max"] == "unlimited" else min_max["max"]
    if salario >= min_max["min"] and salario <= maximo:
        print(f"Novo salario: {(salario*(percent/100)+salario):.2f}")
        print(f"Reajuste ganho: {(salario*(percent/100)):.2f}")
        print(f"Em percentual: {percent} %")
        break
