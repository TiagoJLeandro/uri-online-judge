"""
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.

"""

def verificar_se_sao_multiplos():
    numero_1, numero_2 = [int(num) for num in input().split()]
    resultado = "Sao Multiplos" if (
        not numero_1 % numero_2 or 
        not numero_2 % numero_1) else "Nao sao Multiplos"
    return resultado

print(verificar_se_sao_multiplos())
