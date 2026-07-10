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
    print("Choose a bit sequence")
    print("1 - 10101010   -> Constant alternation")
    print("2 - 00000000   -> Long sequence of zeros")
    print("3 - 111111111  -> Long sequence of ones")
    print("4 - 11001100   -> Mixed pattern")
    print("5 - Random     -> Random 16-bit sequence")
    print("6 - Enter manually")
    print("0 - Exit")
    print()


def escolher_sequencia():
    while True:
        mostrar_menu_sequencias()

        opcao = input("Choose an option: ")

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
            print("Random sequence generated:", bits)
            return bits

        if opcao == "6":
            bits = input("Enter the bit sequence: ")

            if validar_bits(bits):
                return bits

            print("Invalid sequence. Use only 0 and 1.")
            continue

        print("Invalid option.")


def mostrar_menu_codigos():
    print()
    print("Choose a line code")
    print("1 - Manchester")
    print("2 - Differential Manchester")
    print("3 - NRZ-I")
    print("4 - NRZ-L")
    print("5 - AMI")
    print("6 - Pseudoternary")
    print("7 - CMI")
    print("8 - MLT-3")
    print("9 - 2B1Q")
    print("10 - Comparison mode")
    print("0 - Back")
    print()


def escolher_codigo():
    while True:
        mostrar_menu_codigos()

        opcao = input("Choose an option: ")

        if opcao == "0":
            return None

        if opcao == "1":
            return "Manchester"

        if opcao == "2":
            return "Differential Manchester"
        
        if opcao == "3":
            return "NRZ"
        
        if opcao == "4":
            return "NRZ-L"
        
        if opcao == "5":
            return "AMI"
    
        if opcao == "6":
            return "Pseudoternary"

        if opcao == "7":
            return "CMI"

        if opcao == "8":
            return "MLT-3"

        if opcao == "9":
            return "2B1Q"

        if opcao == "10":
            return "Comparison"

        print("Invalid option.")

def executar():
    while True:
        bits = escolher_sequencia()

        if bits is None:
            print("Exiting...")
            break

        codigo = escolher_codigo()

        if codigo is None:
            continue

        if codigo == "Comparison":
            executar_comparacao(bits, escolher_codigo)
            continue

        sinal, titulo = gerar_sinal(bits, codigo)

        print()
        print("Selected sequence:", bits)
        print("Selected code:", codigo)

        exibir_grafico(bits, sinal, titulo)


if __name__ == "__main__":
    executar()
