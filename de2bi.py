import numpy as np
import cmath as cm

def de2bi(n,N):
    bseed= bin(n).replace("0b", "")
    fix = N-len(bseed)
    pad = np.zeros(fix)
    pad=pad.tolist()
    y=[]         
    for i in range(len(pad)):
        y.append(int(pad[i]))  
    for i in range(len(bseed)):
        y.append(int(bseed[i]))
    return y


