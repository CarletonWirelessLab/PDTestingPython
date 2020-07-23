from raw_to_complex import raw_to_complex
from detect_frames import detect_frames
from coarse_cfo_correct import coarse_cfo_correct
from ch_estim import ch_estim
from sig_field_decoder import sig_field_decoder
from check_sig_field import check_sig_field
from extract_mac import extract_mac
import numpy as np

bin_file = "../Bins/Receive25%.bin"
fraction = 1/60
complex_data = raw_to_complex(bin_file, fraction)

complex_data = np.concatenate((np.zeros(1000,dtype=complex), complex_data, np.zeros(1000,dtype=complex)))
pkt_locs = detect_frames(complex_data)

s_corrected = coarse_cfo_correct(complex_data, pkt_locs)

hinv = ch_estim(s_corrected, pkt_locs)  # Matches Matlab code up to here.

# print(s_corrected[(6301+160+160+80+16):(6301+160+160+80+16+64)])
# exit()
rate, res, length, parity, tail = sig_field_decoder(s_corrected, pkt_locs, hinv)

MSC = check_sig_field(rate, res, length, parity, tail)

extract_mac(s_corrected, pkt_locs[:, 0], MSC, hinv)

