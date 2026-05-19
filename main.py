import random

from codigos.gerador import gerar_sinal
from comparacao import executar_comparacao
from grafico import exibir_grafico


def validar_bits(bits):
    if bits == "":
        return False

    for bit in bits:
        if bit not in "01":
            return False

    return True


def gerar_sequencia_aleatoria(tamanho=16):
    bits = ""

    for _ in range(tamanho):
        bits += random.choice("01")

    return bits


def mostrar_menu_sequencias():
    print()
    print("Escolha a sequencia de bits")
    print("1 - 10101010   -> Alternancia constante")
    print("2 - 00000000   -> Longa sequencia de zeros")
    print("3 - 111111111  -> Longa sequencia de uns")
    print("4 - 11001100   -> Padrao misto")
    print("5 - Aleatoria  -> Aleatório com 16 bits")
    print("6 - Digitar manualmente")
    print("0 - Sair")
    print()


def escolher_sequencia():
    while True:
        mostrar_menu_sequencias()

        opcao = input("Escolha uma opcao: ")

        if opcao == "0":
            return None

        if opcao == "1":
            return "10101010"

        if opcao == "2":
            return "00000000"

        if opcao == "3":
            return "11111111"

        if opcao == "4":
            return "11001100"

        if opcao == "5":
            bits = gerar_sequencia_aleatoria(16)
            print("Sequencia aleatoria gerada:", bits)
            return bits

        if opcao == "6":
            bits = input("Informe a sequencia de bits: ")

            if validar_bits(bits):
                return bits

            print("Sequencia invalida. Use apenas 0 e 1.")
            continue

        print("Opcao invalida.")


def mostrar_menu_codigos():
    print()
    print("Escolha o codigo de linha")
    print("1 - Manchester")
    print("2 - Manchester Diferencial")
    print("3 - NRZ")
    print("4 - NRZ-L")
    print("5 - AMI")
    print("6 - Pseudoternário")
    print("7 - CMI")
    print("8 - MLT-3")
    print("9 - 2B1Q")
    print("10 - Modo comparação")
    print("0 - Voltar")
    print()


def escolher_codigo():
    while True:
        mostrar_menu_codigos()

        opcao = input("Escolha uma opcao: ")

        if opcao == "0":
            return None

        if opcao == "1":
            return "Manchester"

        if opcao == "2":
            return "Manchester Diferencial"
        
        if opcao == "3":
            return "NRZ"
        
        if opcao == "4":
            return "NRZ-L"
        
        if opcao == "5":
            return "AMI"
    
        if opcao == "6":
            return "Pseudoternario"

        if opcao == "7":
            return "CMI"

        if opcao == "8":
            return "MLT-3"

        if opcao == "9":
            return "2B1Q"

        if opcao == "10":
            return "Comparacao"

        print("Opcao invalida.")

def executar():
    while True:
        bits = escolher_sequencia()

        if bits is None:
            print("Encerrando...")
            break

        codigo = escolher_codigo()

        if codigo is None:
            continue

        if codigo == "Comparacao":
            executar_comparacao(bits, escolher_codigo)
            continue

        sinal, titulo = gerar_sinal(bits, codigo)

        print()
        print("Sequencia escolhida:", bits)
        print("Codigo escolhido:", codigo)

        exibir_grafico(bits, sinal, titulo)


if __name__ == "__main__":
    executar()
