"""

Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".
Entrada

Quatro números inteiros A, B, C e D.
Saída

Mostre a respectiva mensagem após a validação dos valores.

"""

a, b, c, d = [int(numero) for numero in input().split(" ")]

def eh_par(num):
    return True if num%2==0 else False

def eh_positivo(num):
    return True if num >=1 else False

def validated_values():
    return "Valores aceitos" if eh_par(a) and (
        b > c and d > a) and (c+d > a+b) and (
            eh_positivo(c) and eh_positivo(d)) else "Valores nao aceitos"

print(validated_values())
