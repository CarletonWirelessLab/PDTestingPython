import numpy as np


def check_sig_field(rate, res, length, parity, tail):
    rate = np.array(rate)
    res = np.array(res)
    length = np.array(length)
    parity = np.array(parity)
    tail = np.array(tail)

    pkt_count = res.size
    # pkt_count = pkt_count_row_col[2]
    MSC = -1*np.ones((pkt_count,1))
    # print(pkt_count)
    for n in range(0, pkt_count):
        if res[n, :] != 0: # check reserved bit is set to zero
            print("PACKET " + str(n+1) + " reserved bit is not valid")
            continue
        elif sum(tail[n,:]) > 0: # check tail is 6 zeros
            print("PACKET " + str(n+1) + " tail bits are not valid")
            continue
        elif (sum(rate[n,:]) + sum(length[n,:]) + sum(parity[n])) % 2 != 0: # even parity check
            print("PACKET " + str(n+1) + " even parity check failed")
            continue
        else:
            if sum(rate[n, :] == [1, 1, 0, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("--------------------")
                # print("# PAYLOAD LENGTH = %d BYTES",bi2de(length[n,:]))
                print("# BIT RATE 6 Mbps")
                print("# MODULATION BPSK")
                print("# CODE RATE 1/2")
                print("--------------------")
                MSC[n] = 0
            elif sum(rate[n, :] == [1, 1, 1, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                # print("# PAYLOAD LENGTH = %d BYTES",bi2de(length[n,:]))
                print("# BIT RATE 9 Mbps")
                print("# MODULATION BPSK")
                print("# CODE RATE 3/4")
                print("--------------------")
                MSC[n] = 1
            elif sum(rate[n, :] == [0, 1, 0, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                # print("# PAYLOAD LENGTH = %d BYTES",bi2de(length[n,:]))
                print("# BIT RATE 12 Mbps")
                print("# MODULATION QPSK")
                print("# CODE RATE 1/2")
                print("--------------------")
                MSC[n] = 2
            elif sum(rate[n, :] == [0, 1, 1, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                # print("# PAYLOAD LENGTH = %d BYTES",bi2de(length[n,:]))
                print("# BIT RATE 18 Mbps")
                print("# MODULATION QPSK")
                print("# CODE RATE 3/4")
                print("--------------------")
                MSC[n] = 3
            elif sum(rate[n, :] == [1, 0, 0, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                # print("# PAYLOAD LENGTH = %d BYTES",bi2de(length[n,:]))
                print("# BIT RATE 24 Mbps")
                print("# MODULATION 16-QAM")
                print("# CODE RATE 1/2")
                print("--------------------")
                MSC[n] = 4
            elif sum(rate[n, :] == [1, 0, 1, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                # print("# PAYLOAD LENGTH = %d BYTES",bi2de(length[n,:]))
                print("# BIT RATE 36 Mbps")
                print("# MODULATION 16-QAM")
                print("# CODE RATE 3/4")
                print("--------------------")
                MSC[n] = 5
            elif sum(rate[n, :] == [0, 0, 0, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                # print("# PAYLOAD LENGTH = %d BYTES",bi2de(length[n,:]))
                print("# BIT RATE 48 Mbps")
                print("# MODULATION 64-QAM")
                print("# CODE RATE 2/3")
                print("--------------------")
                MSC[n] = 6
            elif sum(rate[n, :] == [0, 0, 1, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                # print("# PAYLOAD LENGTH = %d BYTES",bi2de(length[n,:]))
                print("# BIT RATE 54 Mbps")
                print("# MODULATION 64-QAM")
                print("# CODE RATE 3/4")
                print("--------------------")
                MSC[n] = 7
            else:
                print("PACKET " + str(n+1) + " rate is invalid")
    return MSC
