from detect_frames import detect_frames
from coarse_cfo_correct import coarse_cfo_correct
from ch_estim import ch_estim
from sig_field_decoder import sig_field_decoder
from check_sig_field import check_sig_field
from extract_mac import extract_mac
import numpy as np


# This program is a post-processing receiver which takes raw data in the form of a sampled waveform and extracts frame
# information for the purpose of capturing wifi packets.
# Based off of the 802.11a - 1999 standards

def wifi_rx(s):
    complex_data = np.concatenate((np.zeros(1000, dtype=complex), s, np.zeros(1000, dtype=complex),s,np.zeros(1000,dtype=complex)))
    pkt_locs = detect_frames(complex_data)  # Determine start and end sample locations of each frame in the raw data

    s_corrected = coarse_cfo_correct(complex_data, pkt_locs)  # Coarse Carrier Frequency Offset correction (STF)
    hinv = ch_estim(s_corrected, pkt_locs)  # Channel estimation (LTF)
    rate, res, length, parity, tail = sig_field_decoder(s_corrected, pkt_locs, hinv)  # Channel estimation (LTF)
    MSC, output_array = check_sig_field(rate, res, length, parity, tail)  # Check that packet information is valid
    packet_type, MAC1, MAC2, MAC3 = extract_mac(s_corrected, pkt_locs[:, 0], MSC, hinv)  # Extract MAC addresses from packet payload

    # Output Data to .CSV:
    mac_data = []
    mac_data.append([MAC1, MAC2, MAC3, packet_type])
    mac_data = np.array(mac_data)
    mac_data = mac_data[0, :, :]
    mac_data = mac_data.T
    pkt_indices = np.arange(0, len(pkt_locs)).T
    packet_data = np.concatenate((pkt_locs, output_array, mac_data), axis=1)
    top_row = ["Start Sample", "End Sample", "Payload length", "Bit Rate", "Modulation", "Code Rate", "MAC1", "MAC2", "MAC3", "Packet Type"]
    top_row = np.array(top_row)
    packet_data = np.vstack((top_row, packet_data))
    np.savetxt("Packet_Data.csv", packet_data, delimiter=",", fmt="%s")
    print(packet_data)
    mac1_array = MAC1
    length_array = output_array[:,0]
    type_array = packet_type
    rate_array = output_array[:, 1]
    start_array = pkt_locs[:, 0]
    end_array = pkt_locs[:, 1]
    return mac1_array, length_array, type_array, rate_array, start_array, end_array
