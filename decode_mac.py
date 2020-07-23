import numpy as np


def decode_mac(bitstream):
    bitstream = bitstream.tolist()
    print(len(bitstream))

    m = 12 * 4
    m1 = 16 + 32 + np.arange(0, m)
    m2 = max(m1) + np.arange(0, m)
    m3 = max(m2) + np.arange(0, m)
    mac1_bin = bitstream[min(m1):max(m1)]
    mac1 = hex(bitstream[min(m1):max(m1)])
    mac2 = hex(bitstream[min(m2):max(m2)].T)
    mac3 = hex(bitstream[min(m3):max(m3)].T)

    return mac1, mac2, mac3
