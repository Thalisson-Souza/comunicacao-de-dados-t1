def codigo_2b1q(bits):
    sinal = []
    
    if len(bits) % 2 != 0:
        bits += '0'

    for i in range(0, len(bits), 2):
        dibit = bits[i:i+2] 
        
        if dibit == '10':
            sinal.append(3)
        elif dibit == '11':
            sinal.append(1)
        elif dibit == '01':
            sinal.append(-1)
        elif dibit == '00':
            sinal.append(-3)

    return sinal
