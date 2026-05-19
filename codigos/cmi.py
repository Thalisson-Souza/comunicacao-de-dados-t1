def cmi(bits):
    sinal = []
    nivel_atual = 1

    for bit in bits:
        if bit == "0":
            sinal.extend([-1, 1])
        else:
            sinal.extend([nivel_atual, nivel_atual])
            nivel_atual *= -1

    return sinal