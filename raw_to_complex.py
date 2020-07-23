import numpy as np
import math


def raw_to_complex(file_name, fraction):
    global data_length
    file = open(file_name, "rb")
    data = np.fromfile(file,'<f4')
    file.close()
    inphase_data = data[0:len(data):2]
    quadrature_data = data[1:len(data):2]
    data_length = math.floor(fraction*min(len(inphase_data), len(quadrature_data)))
    complex_data = inphase_data[0:data_length - 1] - 1j*quadrature_data[0:data_length-1]
    complex_data = complex_data/max(abs(complex_data))
    return complex_data

# bin_file = "E:\School\Graduate Studies\Packet Detector\Bins\Receive25%.bin"
#
# fraction = 1
#
# raw_to_complex(bin_file, fraction)
