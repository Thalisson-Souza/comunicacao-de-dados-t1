from codigos.manchester import manchester, manchester_diferencial
from codigos.nrz import nrz_i, nrz_l
from codigos.ami import ami
from codigos.pseudoternario import pseudoternario
from codigos._2b1q import codigo_2b1q
from codigos.cmi import cmi
from codigos.mlt3 import mlt3


def gerar_sinal(bits, codigo):
    if codigo == "Manchester":
        sinal = manchester(bits)
        titulo = "Manchester Encoding"

    elif codigo == "Differential Manchester":
        sinal = manchester_diferencial(bits)
        titulo = "Differential Manchester Encoding"

    elif codigo == "NRZ":
        sinal = nrz_i(bits)
        titulo = "NRZ-I Encoding"

    elif codigo == "NRZ-L":
        sinal = nrz_l(bits)
        titulo = "NRZ-L Encoding"

    elif codigo == "AMI":
        sinal = ami(bits)
        titulo = "AMI Encoding"

    elif codigo == "Pseudoternary":
        sinal = pseudoternario(bits)
        titulo = "Pseudoternary Encoding"

    elif codigo == "CMI":
        sinal = cmi(bits)
        titulo = "CMI Encoding"

    elif codigo == "MLT-3":
        sinal = mlt3(bits)
        titulo = "MLT-3 Encoding"

    elif codigo == "2B1Q":
        sinal = codigo_2b1q(bits)
        titulo = "2B1Q Encoding"

    return sinal, titulo
