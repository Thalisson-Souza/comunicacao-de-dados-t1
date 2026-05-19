def manchester_diferencial(bits):
    sinal = []
    nivel_atual = 1     
    for bit in bits:
        if bit == "0":   
            nivel_atual = -nivel_atual
            
        sinal.extend([nivel_atual, -nivel_atual])
        nivel_atual = -nivel_atual
    return sinal


def manchester(bits):
    sinal = []
    nivel_atual = -1
    for bit in bits:
        if bit == "1":
            sinal.extend([nivel_atual, -nivel_atual])
        else:
            sinal.extend([-nivel_atual, nivel_atual])
    return sinal

