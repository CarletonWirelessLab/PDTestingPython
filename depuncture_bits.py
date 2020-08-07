import numpy as np

def depuncture_bits(bits_deinter, MSCn):
    bits_depuncture = [] 
    if MSCn == 0 or MSCn == 2 or MSCn == 4:
        bits_depuncture = bits_deinter
    elif MSCn == 1 or MSCn == 3 or MSCn == 5 or MSCn == 7:
        bits_depuncture=bits_deinter[0:3]
        n = 3 - 1

        while n < max(np.array(bits_deinter).shape):
            for m in range(1, 5):
                if n + m < max(np.array(bits_deinter).shape):
                    if m==1:
                        bits_depuncture.append(0)
                        bits_depuncture.append(0)
                        bits_depuncture.append(bits_deinter[n + m])         
                    else:
                        bits_depuncture.append(bits_deinter[n + m])    
            n = n + 4 

    else:
        bits_depuncture=bits_deinter[0:3]
        n = 3 - 1

        while n < max(np.array(bits_deinter).shape):
            for m in range(1, 4):
                if n + m < max(np.array(bits_deinter).shape):
                    if m==1:
                        bits_depuncture.append( 0)
                        bits_depuncture.append(bits_deinter[n + m])
                    else:
                        #print(max(np.array(bits_deinter).shape))
                       # print(n+m)
                        bits_depuncture.append(bits_deinter[n + m])                  
            n = n + 3 
    return bits_depuncture

