import numpy as np
import constants as c


def strip_symbs(complex_data, pkt_startn, m):
    stf_len = c.stf_len
    ltf_len = c.ltf_len
    cyc_prefix_len = c.cyc_prefix_len
    symb_len = c.symb_len
    sig_len = c.sig_len


    v = np.arange(0, symb_len)
    v = pkt_startn + stf_len + ltf_len + sig_len + cyc_prefix_len + ((m - 1) * (cyc_prefix_len + symb_len)) + v

    start_index = min(v)
    end_index = max(v) + 1

    symbs = complex_data[int(start_index):int(end_index)]

    return symbs
