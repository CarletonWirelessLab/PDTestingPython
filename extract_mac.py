import numpy as np
import math
from strip_symbs import strip_symbs
from demodulate_symbs import demodulate_symbs
from deinterleave_symbs import deinterleave_symbs
from convdenc import convdenc
from descrambler import descrambler
from decode_mac import decode_mac


def extract_mac(complex_data, pkt_start, MSC, hinv):
    pkt_count = len(pkt_start)

    mac1 = []
    mac2 = []
    mac3 = []
    good = []
    subtype_duration_bits = []

    for n in range(0, pkt_count):
        MSCn = MSC[n]
        pkt_startn = pkt_start[n]
        bitstream = []
        bits_deinter = []
        if MSCn == 0:
            numDBPS = 24
        elif MSCn == 1:
            numDBPS = 36
        elif MSCn == 2:
            numDBPS = 48
        elif MSCn == 3:
            numDBPS = 72
        elif MSCn == 4:
            numDBPS = 96
        elif MSCn == 5:
            numDBPS = 144
        elif MSCn == 6:
            numDBPS = 192
        else:
            numDBPS = 216

        for m in range(1, math.ceil(192/numDBPS)):
            symbs = strip_symbs(complex_data, pkt_startn, m)
            bits_demod = demodulate_symbs(symbs, MSCn, hinv[:, n])
            print(bits_demod)
            exit()
            bits_deinter = deinterleave_symbs(bits_demod, MSCn)

        # bits_decode = decode_symbs(bits_deinter, MSCn  # needs to be decode_symbs() not convdenc
        # print(len(bits_decode))
        # exit()
        # bits_descram = descrambler(bits_decode)
        # bitstream = bits_descram
        #
        # [mac1, mac2, mac3] = decode_mac(bitstream)
        # subtype_duration_bits = [subtype_duration_bits, bitstream[16+np.arange(0, 32)]]
        # MAC1 = MAC1 + [mac1]
        # MAC2 = MAC2 + [mac2]
        # MAC3 = MAC3 + [mac3]
        # print(MAC1)

    return

