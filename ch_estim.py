import numpy as np
import constants as c


def ch_estim(s, pkt_locs):
    ltf_fft = c.ltf_fft

    pkt_count = len(pkt_locs)
    hinv = (1+(0*1j))*(np.ones((64, pkt_count)))
    v_1 = np.arange(-26, -1)
    v_1 = v_1.tolist()
    v_2 = np.arange(1, 26)
    v_2 = v_2.tolist()
    v = v_1 + v_2
    v = np.array(v)

    for n in range(0, pkt_count):
        start_index = pkt_locs[n, 0]

        window_1_start = start_index + 160 + 32
        window_1_end = start_index + 160 + 32 + 63 + 1
        s_fft1 = np.fft.fft(s[window_1_start:window_1_end])
        s_fft1 = np.fft.fftshift(s_fft1)
        
        window_2_start = start_index + 160 + 32 + 64
        window_2_end = start_index + 160 + 32 + 64 + 63 + 1
        s_fft2 = np.fft.fft(s[window_2_start:window_2_end])
        s_fft2 = np.fft.fftshift(s_fft2)

        s_fft = (s_fft1 + s_fft2) / 2

        hinv_row = (np.array(ltf_fft) / np.array(s_fft))
        hinv[:, n] = hinv_row
        # ltf_fft_temp = [ltf_fft[x] for x in 33+v]
        # s_fft_temp = [s_fft[x] for x in 33+v]
        # ltf_fft_temp = np.array(ltf_fft_temp)
        # s_fft_temp = np.array(s_fft_temp)
        # hinv_row = ltf_fft_temp / s_fft_temp

    return hinv
