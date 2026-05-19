from codigos.gerador import gerar_sinal
from grafico import exibir_grafico_comparacao

def calcular_metricas(sinal):
    transicoes = 0

    for i in range(1, len(sinal)):
        if sinal[i] != sinal[i - 1]:
            transicoes += 1

    valor_medio = sum(sinal) / len(sinal)

    return transicoes, valor_medio


def exibir_metricas(codigo, sinal):
    transicoes, valor_medio = calcular_metricas(sinal)

    print()
    print("Codigo:", codigo)
    print("Transicoes:", transicoes)
    print("Valor medio aproximado:", round(valor_medio, 2))


def executar_comparacao(bits, escolher_codigo):
    print()
    print("Escolha o primeiro codigo")
    codigo_1 = escolher_codigo()

    if codigo_1 is None or codigo_1 == "Comparacao":
        return

    print()
    print("Escolha o segundo codigo")
    codigo_2 = escolher_codigo()

    if codigo_2 is None or codigo_2 == "Comparacao":
        return

    sinal_1, titulo_1 = gerar_sinal(bits, codigo_1)
    sinal_2, titulo_2 = gerar_sinal(bits, codigo_2)

    print()
    print("Sequencia comparada:", bits)

    metricas_1 = calcular_metricas(sinal_1)
    metricas_2 = calcular_metricas(sinal_2)

    exibir_grafico_comparacao(bits, sinal_1, titulo_1, sinal_2, titulo_2, metricas_1, metricas_2)