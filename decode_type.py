import numpy as np


def decode_type(sub_type_field):
    # Check if field is beacon:
    if np.array_equal(sub_type_field, [0,0,1,0,0,0]):
        packet_type = 'Beacon'
    else:
        packet_type = "N/A"

    return packet_type
