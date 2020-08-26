import numpy as np
from bi2de import bi2de


# The purpose of this function is to check that the SIG field values determined from sig_field_decoder() are valid
# such that they follow the correct format of the plcp described in the 802.11a - 1999 standard

def check_sig_field(rate, res, length, parity, tail):
    # convert each field to a numpy array:
    rate = np.array(rate)
    res = np.array(res)
    length = np.array(length)
    parity = np.array(parity)
    tail = np.array(tail)

    # Determine number of packets:
    pkt_count = res.size

    # initialize output variables:
    MSC = -1*np.ones((pkt_count, 1))
    output_array = []

    for n in range(0, pkt_count):
        if res[n] != 0:  # check reserved bit is set to zero
            print("PACKET " + str(n+1) + " reserved bit is not valid")
            continue
        elif sum(tail[n,:]) > 0:  # check tail is 6 zeros
            print("PACKET " + str(n+1) + " tail bits are not valid")
            continue
        elif (sum(rate[n,:]) + sum(length[n,:]) + sum(parity[n])) % 2 != 0:  # even parity check
            print("PACKET " + str(n+1) + " even parity check failed")
            continue
        else:  # otherwise SIG field is valid and can be decoded according to the 8 possible options of 802.11a - 1999
            if sum(rate[n, :] == [1, 1, 0, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("--------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 6 Mbps")
                print("# MODULATION BPSK")
                print("# CODE RATE 1/2")
                print("--------------------")
                MSC[n] = 0
                output_array.append([str(bi2de(length[n, :])), 6, "BPSK Modulation", "0.5"])
            elif sum(rate[n, :] == [1, 1, 1, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n, :])) + " BYTES")
                print("# BIT RATE 9 Mbps")
                print("# MODULATION BPSK")
                print("# CODE RATE 3/4")
                print("--------------------")
                MSC[n] = 1
                output_array.append([str(bi2de(length[n, :])), 9, "BPSK Modulation", "0.75"])

            elif sum(rate[n, :] == [0, 1, 0, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 12 Mbps")
                print("# MODULATION QPSK")
                print("# CODE RATE 1/2")
                print("--------------------")
                MSC[n] = 2
                output_array.append([str(bi2de(length[n, :])), 12, "QPSK Modulation", "0.5"])
            elif sum(rate[n, :] == [0, 1, 1, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 18 Mbps")
                print("# MODULATION QPSK")
                print("# CODE RATE 3/4")
                print("--------------------")
                MSC[n] = 3
                output_array.append([str(bi2de(length[n, :])), 18, "QPSK Modulation", "0.75"])
            elif sum(rate[n, :] == [1, 0, 0, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 24 Mbps")
                print("# MODULATION 16-QAM")
                print("# CODE RATE 1/2")
                print("--------------------")
                MSC[n] = 4
                output_array.append([str(bi2de(length[n, :])), 24, "16-QAM Modulation", "0.5"])
            elif sum(rate[n, :] == [1, 0, 1, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 36 Mbps")
                print("# MODULATION 16-QAM")
                print("# CODE RATE 3/4")
                print("--------------------")
                MSC[n] = 5
                output_array.append([str(bi2de(length[n, :])), 36, "16-QAM Modulation", "0.75"])
            elif sum(rate[n, :] == [0, 0, 0, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 48 Mbps")
                print("# MODULATION 64-QAM")
                print("# CODE RATE 2/3")
                print("--------------------")
                MSC[n] = 6
                output_array.append([str(bi2de(length[n, :])), 48, "64-QAM Modulation", "0.66"])
            elif sum(rate[n, :] == [0, 0, 1, 1]) == 4:
                print("PACKET" + str(n+1) + " is valid")
                print("------------------")
                print("# PAYLOAD LENGTH = " + str(bi2de(length[n,:])) + " BYTES")
                print("# BIT RATE 54 Mbps")
                print("# MODULATION 64-QAM")
                print("# CODE RATE 3/4")
                print("--------------------")
                MSC[n] = 7
                output_array.append([str(bi2de(length[n, :])), 54, "64-QAM Modulation", "0.75"])
            else:  # If the rate field is invalid and doesn't match any allowable rate parameter the packet is invalid
                print("PACKET " + str(n+1) + " rate is invalid")
    return MSC, np.array(output_array)
