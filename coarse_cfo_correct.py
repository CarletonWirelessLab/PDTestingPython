import constants as c
import numpy as np
import cmath as cm


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

        df_0 = (1/sts_len)
        v_1 = np.array(v)
        v_1 += start_index
        v_2 = v_1 + sts_len
        # x1 = complex_data[v_1]
        # x2 = np.conj(complex_data[v_2])
        df_1 = [complex_data[i] for i in v_1]
        df_2 = [complex_data[i] for i in v_2]
        df_2 = np.conj(df_2)
        df = df_0 * np.angle(np.sum(df_1 * df_2))
        df = np.round(df, 4)
        nv = np.arange(start_index, end_index)
        # print(nv[0:10])
        # print(start_index)
        nv = np.array(nv)
        nv = nv + 1
        ev = 1j * nv * df
        ev = np.exp(ev)
        nv = nv - 1
        temp = [complex_data[x] for x in nv]
        temp = temp * ev
        # temp = complex_data[nv]*ev
        s_corrected[start_index:end_index] = temp
        # print(temp)

    return s_corrected
