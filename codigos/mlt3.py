def mlt3(bits):
    sinal = []
    nivel_atual = 0
    proximo_nivel = 1  # começa em +V

    for bit in bits:
      if bit == '1':
        if proximo_nivel == 0:
          proximo_nivel = nivel_atual * -1  # alterna entre +V e -V
          nivel_atual = 0
        else:
          nivel_atual = proximo_nivel
          proximo_nivel = 0
      sinal.append(nivel_atual)
    
    return sinal