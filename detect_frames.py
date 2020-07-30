import constants as c
import numpy as np
import cross_cor


# The purpose of this function is to determine the start and end samples of each frame by scanning the complex data
# for the STF of each frame and recording the index of each starting and ending sample
def detect_frames(complex_data):
    print("FINDING FRAMES")
    print("--------------")

    # CONSTANTS:
    # short training sequence length
    sts_len = c.sts_len
    # short training field length
    stf_len = c.stf_len
    # minimum packet length
    pkt_min_len = c.pkt_min_len
    stf_fft = c.stf_fft

    # INITIALIZATIONS:
    # Length of the signal
    s_len = len(complex_data)
    pkt_start = []
    pkt_end = []
    # Number of Found Packets
    pkt_count = 0
    # Max index for loop
    n_max = s_len - (stf_len - 1)
    # Iterate through entire signal
    n = 0

    # FIND PACKET START:
    while n < n_max:
        # For the first 16 samples of STF, skip the first sample then take first 15 samples of STF
        start_window = n + 1
        end_window = n + sts_len-1 + 1
        x1 = complex_data[start_window:end_window]

        # For the last 16 samples of STF, skip the first sample then take first 15 samples of STF
        start_window_2 = n + (stf_len - sts_len) + 1
        end_window_2 = n + (stf_len - sts_len) + sts_len-1 + 1
        x2 = complex_data[start_window_2:end_window_2]

        # Perform correlation:
        correlation = cross_cor.cross_cor(x1, x2)
        # print(correlation)

        if correlation > 0.90:
            c_max = correlation
            while 1:
                n = n + 1
                # For the first 16 samples of STF, skip the first sample then take first 15 samples of STF
                start_window = n + 1
                end_window = n + sts_len-1 + 1
                x1 = complex_data[start_window:end_window]

                # For the last 16 samples of STF, skip the first sample then take first 15 samples of STF
                start_window_2 = n + (stf_len - sts_len) + 1
                end_window_2 = n + (stf_len - sts_len) + sts_len-1 + 1
                x2 = complex_data[start_window_2:end_window_2]

                # perform secondary correlation:
                second_corr = cross_cor.cross_cor(x1, x2)

                if second_corr < c_max:
                    # new packet
                    pkt_count = pkt_count + 1
                    # record previous index
                    pkt_start.append(n-1)
                    n = n + 160
                    break
                else:
                    # correlation is increasing
                    c_max = second_corr
        else:
            n = n + 1
    print(pkt_count)

    # ALIGN PACKET:
    # Determine with accuracy the start and end of each frame by checking 2 samples on either side of previously
    # detected start sample for higher correlation
    good_index = []
    for m in range(pkt_count):
        pkt_startn = pkt_start[m]
        good_location = 0
        # Check if correlation improves when moving 2 samples to either side of the previously determined start sample
        for n in range(-2, 2):
            start_sample_range = pkt_startn+n
            end_sample_range = pkt_startn+n+63 + 1

            complex_data_array = complex_data[start_sample_range:end_sample_range]
            x = np.fft.fft(complex_data_array)
            x = np.fft.fftshift(x)
            comp_cor = cross_cor.cross_cor(x, c.stf_fft)
            if comp_cor > 0.7:  # Check if correlation has improved, if so record index as starting sample of a frame
                pkt_start[m] = pkt_startn + n
                good_location = 1
        if good_location == 1:
            good_index.append(m)
    pkt_start = [pkt_start[x] for x in good_index]
    pkt_count = len(pkt_start)

    # FIND PACKET END:
    for m in range(0, pkt_count):
        # check if this is the last packet, then go to the end of the signal
        # and move left until you hit the start of the packet or detect some energy
        if m == pkt_count-1:
            end_index = s_len-1
        else:
            end_index = pkt_start[m+1] - sts_len
        # Get the start of the packet
        start_index = pkt_start[m]
        # Look left from the start of the packet and find the average value of the absolute values to find
        # the mean of the noise (32 samples)
        start_noise_window = -33+start_index
        end_noise_window = -1+start_index
        complex_data_array = complex_data[start_noise_window:end_noise_window]
        complex_data_array = np.array(complex_data_array)
        threshold = np.mean(abs(complex_data_array))
        # Move left through frame
        for n in range(end_index, start_index, -1):
            if abs(complex_data[n]) > 2 * threshold:
                pkt_end.append(n)
                break

    pkt_start_array = np.array(pkt_start)
    pkt_end_array = np.array(pkt_end)
    pkt_count = len(pkt_start)

    # PRINT RESULTS:
    print('TOTAL PACKETS FOUND: ' + str(pkt_count))
    print('--------------------------------------')
    for n in range(0, pkt_count):
        print('PACKET ' + str(n + 1))
        print('Starts at sample: ' + str(pkt_start[n]))
        print('Ends at sample: ' + str(pkt_end_array[n]))
        print('----------------------')

    # RETURN:
    pkt_locs = np.vstack((pkt_start_array, pkt_end_array)).T
    return pkt_locs
