import numpy as np
import constants as c
from convdenc import convdenc


# The purpose of this function is to decode the SIG Field of the frame to determine packet parameters:
# Bit Rate and Code Rate (from rate field of PLCP), Payload length (from length field of PLCP)
# and checking packet validity.
def sig_field_decoder(complex_data, pkt_locs, hinv):
    k48 = np.array(c.k48)-1

    pkt_shape = pkt_locs.shape
    pkt_count = pkt_shape[0]

    rate = np.zeros((pkt_count, 4))
    res = np.zeros(pkt_count)
    length = np.zeros((pkt_count, 12))
    parity = np.zeros((pkt_count, 1))
    tail = np.zeros((pkt_count, 6))

    m_start = 160+160+16  # STF length + LTF length + cyclic prefix length
    m_end = 160+160+16 + 63 + 1  # STF length + LTF length + cyclic prefix length + symbol length
    v = [-26, -25, -24, -23, -22, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26]
    v = np.array(v)  # center frequencies of sub-carriers
    for n in range(0,pkt_count):
        start_index = pkt_locs[n, 0] + m_start
        end_index = pkt_locs[n, 0] + m_end

        sig_fft = np.fft.fftshift(np.fft.fft(complex_data[start_index:end_index]))*hinv[:, n]

        sig_48 = np.real(sig_fft[32+v])
        sig_48_bits = np.zeros((48, 1))

        for m in range(0, 48):  # Decode SIG field using BPSK (>1 gives 1, <1 gives 0)
            if sig_48[m] > 0:
                sig_48_bits[m] = 1
            else:
                sig_48_bits[m] = 0

        sig_48_deinter = sig_48_bits[k48]  # deinterleave bits
        decodedout = convdenc(sig_48_deinter, '1/2')  # decode bits
        # separate decoded bits into their respective fields
        rate[n, :] = (decodedout[0:4]).T
        res[n] = (decodedout[4])
        length[n, :] = (decodedout[5:17]).T
        parity[n, :] = (decodedout[17]).T
        tail[n, :] = (decodedout[18:24]).T
    return rate, res, length, parity, tail
