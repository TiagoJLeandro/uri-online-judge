"""
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

"""

def converter_segundos_para_horas_minutos_segundos():
    segundos = int(input())
    tempo = {
        "horas": segundos // 60 // 60,
        "minutos": segundos // 60 % 60,
        "segundos": segundos % 60
    }
    print(f"{tempo['horas']}:{tempo['minutos']}:{tempo['segundos']}")
    return

converter_segundos_para_horas_minutos_segundos()
