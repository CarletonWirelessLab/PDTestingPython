import numpy as np
import constants as c


# This function provides channel estimation based off the LTF
def ch_estim(s, pkt_locs):
    ltf_fft = c.ltf_fft

    pkt_count = len(pkt_locs)
    hinv = (1+(0*1j))*(np.ones((64, pkt_count)))  # initialize hinv as complex array of ones

    for n in range(0, pkt_count):
        start_index = pkt_locs[n, 0]  # get start index from first column of pkt_locs

        window_1_start = start_index + 160 + 32  # start sample index offset by STF length plus 32
        window_1_end = start_index + 160 + 32 + 63 + 1  # start sample index offset by STF length plus LTF length plus SIG field length
        s_fft1 = np.fft.fft(s[window_1_start:window_1_end])
        s_fft1 = np.fft.fftshift(s_fft1)
        
        window_2_start = start_index + 160 + 32 + 64  # start sample index offset by STF length plus 32 plus SIG field length
        window_2_end = start_index + 160 + 32 + 64 + 63 + 1  # start sample index offset by STF length plus 32 plus SIG field length plus 64
        s_fft2 = np.fft.fft(s[window_2_start:window_2_end])
        s_fft2 = np.fft.fftshift(s_fft2)

        s_fft = (s_fft1 + s_fft2) / 2

        hinv_row = (np.array(ltf_fft) / np.array(s_fft))
        hinv[:, n] = hinv_row

    return hinv
