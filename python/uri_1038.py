"""
Entrada

O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.
Saída

O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal

"""

produtos = {
     1: {"desc": "Cachorro Quente", "valor": 4.00},
     2: {"desc": "X-Salada", "valor": 4.50},
     3: {"desc": "X-Bacon", "valor": 5.00},
     4: {"desc": "Torrada simples", "valor": 2.00},
     5: {"desc": "Refrigerante", "valor": 1.50}
}

codigo, quantidade = [int(numero) for numero in input().split()]
resultado = produtos[codigo]["valor"] * quantidade

print(f"Total: R$ {resultado:.2f}")
