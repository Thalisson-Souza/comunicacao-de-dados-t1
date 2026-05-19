def nrz_i(bits):
    NRZI = []
    current_voltage = -1

    for bit in bits:
        if bit == "1":
            current_voltage = current_voltage * -1

        NRZI.append(current_voltage)

    return NRZI


def nrz_l(bits):
    NRZL = []
    current_voltage = -1

    for bit in bits:
        if bit == "1":
            current_voltage = -1
        else:
            current_voltage = 1

        NRZL.append(current_voltage)
    
    return NRZL




