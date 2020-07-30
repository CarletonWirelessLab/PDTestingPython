import constants as c
import numpy as np


# The purpose of this function is to perform coarse correction to mitigate carrier frequency offset
def coarse_cfo_correct(complex_data, pkt_locs):
    sts_len = c.sts_len
    stf_len = c.stf_len

    s_corrected = complex_data
    pkt_count = len(pkt_locs)

    length = stf_len - sts_len
    v = np.arange(1, length)

    for n in range(0, pkt_count):
        start_index = pkt_locs[n, 0]
        end_index = pkt_locs[n, 1] + 1

        # Calculate frequency offset, df:
        df_0 = (1/sts_len)
        v_1 = np.array(v)
        v_1 += start_index
        v_2 = v_1 + sts_len
        df_1 = [complex_data[i] for i in v_1]
        df_2 = [complex_data[i] for i in v_2]
        df_2 = np.conj(df_2)
        df = df_0 * np.angle(np.sum(df_1 * df_2))  # df is the Coarse frequency offset
        nv = np.arange(start_index, end_index)
        nv = np.array(nv)
        ev = 1j * nv * df
        ev = np.exp(ev)
        temp = [complex_data[x] for x in nv]
        temp = temp * ev  # apply complex offset to each sample index
        s_corrected[start_index:end_index] = temp  # save the corrected list

    return s_corrected
