def pseudoternario(bits):
    sinal = []
    nivel = 1 

    for bit in bits:
        #0 alterna entre +V e -V
        if bit == '0':
            sinal.append(nivel)
            nivel *= -1

        #1 permanece em 0
        else:
            sinal.append(0)

    return sinal