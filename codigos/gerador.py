from codigos.manchester import manchester, manchester_diferencial
from codigos.nrz import nrz, nrz_l
from codigos.ami import ami
from codigos.pseudoternario import pseudoternario
from codigos._2b1q import codigo_2b1q
from codigos.cmi import cmi
from codigos.mlt3 import mlt3


def gerar_sinal(bits, codigo):
    if codigo == "Manchester":
        sinal = manchester(bits)
        titulo = "Codificacao Manchester"

    elif codigo == "Manchester Diferencial":
        sinal = manchester_diferencial(bits)
        titulo = "Codificacao Manchester Diferencial"

    elif codigo == "NRZ":
        sinal = nrz(bits)
        titulo = "Codificacao NRZ"

    elif codigo == "NRZ-L":
        sinal = nrz_l(bits)
        titulo = "Codificacao NRZ-L"

    elif codigo == "AMI":
        sinal = ami(bits)
        titulo = "Codificacao AMI"

    elif codigo == "Pseudoternario":
        sinal = pseudoternario(bits)
        titulo = "Codificacao Pseudoternario"

    elif codigo == "CMI":
        sinal = cmi(bits)
        titulo = "Codificacao CMI"

    elif codigo == "MLT-3":
        sinal = mlt3(bits)
        titulo = "Codificacao MLT-3"

    elif codigo == "2B1Q":
        sinal = codigo_2b1q(bits)
        titulo = "Codificacao 2B1Q"

    return sinal, titulo
