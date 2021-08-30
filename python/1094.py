"""
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.
Entrada

A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).
Saída

Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

"""


class Cobaia:
    cobaias_usadas =  0
    especies = {}

    def __init__(self, quantidade=0, *, abrev, nome):
        self.nome = nome
        self.abrev = abrev
        self.usados = quantidade
        Cobaia.especies[abrev] = self
    
    @property
    def quantidade(self):
        return self.usados

    @quantidade.setter
    def add_quantidade(self, quantidade):
        self.usados += quantidade
        Cobaia.cobaias_usadas += quantidade

    @classmethod
    def numero_de_especies(cls):
        len_ = len(cls.especies)
        return len_
    
    @classmethod
    def mostrar_total_de_cobaias(cls):
        msg = f"Total: {cls.cobaias_usadas} cobaias"
        print(msg)
    
    @classmethod
    def mostrar_total_de_cobaias_por_especies(cls):
        for cobaia in cls.especies.values():
            msg = f"Total de {cobaia.nome}: {cobaia.quantidade}"
            print(msg) if cobaia.quantidade != 0 else None

    @classmethod
    def mostrar_porcentagem_de_cobaias_usadas_por_especies(cls):
        quant_total = cls.cobaias_usadas
        for cobaia in cls.especies.values():
            nome = cobaia.nome
            quant = cobaia.usados 
            porcent = ((quant - quant_total) / quant_total * 100) + 100
            msg = f"Percentual de {nome}: {round(porcent, 2):.2f} %"
            print(msg)


coelhos = Cobaia(abrev="C", nome="coelhos")
ratos = Cobaia(abrev="R", nome="ratos")
sapos = Cobaia(abrev='S', nome="sapos")

for e in range(numero_de_experimentos := int(input(""))):
    quantidade, abrev = input('').split()
    cobaia = Cobaia.especies[abrev]
    cobaia.add_quantidade = int(quantidade)

Cobaia.mostrar_total_de_cobaias()
Cobaia.mostrar_total_de_cobaias_por_especies()
Cobaia.mostrar_porcentagem_de_cobaias_usadas_por_especies()
