import numpy as np
import math
from strip_symbs import strip_symbs
from demodulate_symbs import demodulate_symbs
from deinterleave_symbs import deinterleave_symbs
from decode_symbs import decode_symbs
from descrambler import descrambler
from decode_mac import decode_mac


def extract_mac(complex_data, pkt_start, MSC, hinv):
    pkt_count = len(pkt_start)

    MAC1 = []
    MAC2 = []
    MAC3 = []
    subtype_duration_bits = []

    for n in range(0, pkt_count):
        MSCn = MSC[n]
        pkt_startn = pkt_start[n]
        bitstream = []
        bits_deinter = []
        if MSCn == 0:
            NCBPS = 48
            numDBPS = 24
        elif MSCn == 1:
            NCBPS = 48
            numDBPS = 36
        elif MSCn == 2:
            NCBPS = 96
            numDBPS = 48
        elif MSCn == 3:
            NCBPS = 96
            numDBPS = 72
        elif MSCn == 4:
            NCBPS = 192
            numDBPS = 96
        elif MSCn == 5:
            NCBPS = 192
            numDBPS = 144
        elif MSCn == 6:
            NCBPS = 288
            numDBPS = 192
        else:
            NCBPS = 288
            numDBPS = 216
            
        for m in range(1, math.ceil(192/numDBPS)+1):
            symbs = strip_symbs(complex_data, pkt_startn, m)
            bits_demod = demodulate_symbs(symbs, MSCn, hinv[:, n])
            bits_deinter = bits_deinter + deinterleave_symbs(bits_demod, NCBPS)

        bits_decode = decode_symbs(bits_deinter, MSCn)
        bits_descram = descrambler(bits_decode)  # correlation between python and matlab is 1 up to here
        bitstream = bits_descram
        [mac1, mac2, mac3] = decode_mac(bitstream)
        MAC1 = MAC1 + [mac1]
        MAC2 = MAC2 + [mac2]
        MAC3 = MAC3 + [mac3]

        subtype_duration_bits = [subtype_duration_bits, bitstream[16+np.arange(0, 32)]]

    return subtype_duration_bits, np.array(MAC1), np.array(MAC2), np.array(MAC3)

