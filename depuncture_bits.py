

def depuncture_bits(bits_deinter, MSCn):
    bits_depuncture = []
    if MSCn == 0 or MSCn == 2 or MSCn == 4:
        bits_depuncture = bits_deinter
    elif MSCn == 1 or MSCn == 3 or MSCn == 5 or MSCn == 7:
        bits_depuncture = bits_depuncture + [bits_deinter[0:3]]
        n = 3 - 1

        while n <= max(bits_deinter.shape):
            for m in range(0, 3):
                if n + m <= max(bits_deinter.shape):
                    bits_depuncture = bits_depuncture + [0, 0] + [bits_deinter[n + m]]
                else:
                    bits_depuncture = bits_depuncture + [bits_deinter[n + m]]
            n = n + 4 - 1

    else:
        bits_depuncture = bits_depuncture + [bits_deinter[0:3]]
        n = 3 - 1

        while n <= max(bits_deinter.shape):
            for m in range(0, 3):
                if n + m <= max(bits_deinter.shape):
                    bits_depuncture = bits_depuncture + [0] + [bits_deinter[n + m]]
                else:
                    bits_depuncture = bits_depuncture + [bits_deinter[n + m]]
            n = n + 3 - 1

    return bits_depuncture

