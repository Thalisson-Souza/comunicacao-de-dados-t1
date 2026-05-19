def ami(bits):
    sinal = []
    nivel = 1  # começa em +1

    for bit in bits:
        if bit == '1':
            sinal.append(nivel)
            nivel *= -1  # alterna entre +1 e -1s
        else:
            sinal.append(0)

    return sinal