import numpy as np
from bi2de import bi2de


def check_sig_field(rate, res, length, parity, tail):
    rate = np.array(rate)
    res = np.array(res)
    length = np.array(length)
    parity = np.array(parity)
    tail = np.array(tail)

    pkt_count = res.size
    MSC = -1*np.ones((pkt_count, 1))

    output_array = []

    for n in range(0, pkt_count):
        if res[n] != 0: # check reserved bit is set to zero
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
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 6 Mbps")
                print("# MODULATION BPSK")
                print("# CODE RATE 1/2")
                print("--------------------")
                MSC[n] = 0
                output_array.append([str(bi2de(length[n, :])) + " Bytes", "6 Mbps", "BPSK Modulation", "0.5"])
            elif sum(rate[n, :] == [1, 1, 1, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n, :])) + " BYTES")
                print("# BIT RATE 9 Mbps")
                print("# MODULATION BPSK")
                print("# CODE RATE 3/4")
                print("--------------------")
                MSC[n] = 1
                output_array.append([str(bi2de(length[n, :])) + " Bytes", "9 Mbps", "BPSK Modulation", "0.75"])

            elif sum(rate[n, :] == [0, 1, 0, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 12 Mbps")
                print("# MODULATION QPSK")
                print("# CODE RATE 1/2")
                print("--------------------")
                MSC[n] = 2
                output_array.append([str(bi2de(length[n, :])) + " Bytes", "12 Mbps", "QPSK Modulation", "0.5"])
            elif sum(rate[n, :] == [0, 1, 1, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 18 Mbps")
                print("# MODULATION QPSK")
                print("# CODE RATE 3/4")
                print("--------------------")
                MSC[n] = 3
                output_array.append([str(bi2de(length[n, :])) + " Bytes", "18 Mbps", "QPSK Modulation", "0.75"])
            elif sum(rate[n, :] == [1, 0, 0, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 24 Mbps")
                print("# MODULATION 16-QAM")
                print("# CODE RATE 1/2")
                print("--------------------")
                MSC[n] = 4
                output_array.append([str(bi2de(length[n, :])) + " Bytes", "24 Mbps", "16-QAM Modulation", "0.5"])
            elif sum(rate[n, :] == [1, 0, 1, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 36 Mbps")
                print("# MODULATION 16-QAM")
                print("# CODE RATE 3/4")
                print("--------------------")
                MSC[n] = 5
                output_array.append([str(bi2de(length[n, :])) + " Bytes", "36 Mbps", "16-QAM Modulation", "0.75"])
            elif sum(rate[n, :] == [0, 0, 0, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 48 Mbps")
                print("# MODULATION 64-QAM")
                print("# CODE RATE 2/3")
                print("--------------------")
                MSC[n] = 6
                output_array.append([str(bi2de(length[n, :])) + " Bytes", "48 Mbps", "64-QAM Modulation", "0.66"])
            elif sum(rate[n, :] == [0, 0, 1, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 54 Mbps")
                print("# MODULATION 64-QAM")
                print("# CODE RATE 3/4")
                print("--------------------")
                MSC[n] = 7
                output_array.append([str(bi2de(length[n, :])) + " Bytes", "54 Mbps", "64-QAM Modulation", "0.75"])
            else:
                print("PACKET " + str(n+1) + " rate is invalid")
    return MSC, np.array(output_array)
