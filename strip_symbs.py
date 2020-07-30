import constants as c


def strip_symbs(complex_data, pkt_startn, m):
    stf_len = c.stf_len
    ltf_len = c.ltf_len
    cyc_prefix_len = c.cyc_prefix_len
    symb_len = c.symb_len
    sig_len = c.sig_len

    v_start = pkt_startn + stf_len + ltf_len + sig_len + cyc_prefix_len + ((m - 1) * (cyc_prefix_len + symb_len))
    v_end = v_start + symb_len

    start_index = v_start
    end_index = v_end

    symbs = complex_data[int(start_index):int(end_index)]
    return symbs
