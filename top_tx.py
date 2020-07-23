import numpy as np
import cmath as cm
import matplotlib.pyplot as plt
from conv_enc import conv_enc
from interleave_symbs import interleave_symbs
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
# clear all;
# clc;
###########################################################################
# SHORT TRAINING FIELD
###########################################################################
sts_fft = np.zeros(64,dtype=complex) # short training sequence in FFT domain 64 subcarriers
sts_fft[32+np.array([-24,-16,-4,12,16,20,24])] = cm.sqrt(13/6)*(1+1j)*np.ones(7) # carriers -24, -16, -4, 12, 16, 20, 24 -> 1+1j
sts_fft[32+np.array([-20,-12,-8,4,8])] = -cm.sqrt(13/6)*(1+1j)*np.ones(5); # carriers -20, -12, -8, 4, 8 -> -1-1j

sts = np.fft.ifft((np.fft.fftshift(sts_fft))) # inverse FFT to get 64 samples in time domain

stf = np.zeros(160,dtype=complex)
stf[0:64] = sts
stf[64:128]=sts
stf[128:160] = sts[0:32] # repeat the short training sequence 2.5 times -> 64 64 32 = 160
# plt.plot(range(0,160),np.real(stf))

# ###########################################################################
# # LONG TRAINING FIELD
# ###########################################################################


lts_fft= np.array([0,0,0,0,0,0,1,1,-1,-1,1,1,-1,1,-1,1,1,1,1,1,1,-1,-1,1,1,-1,1,-1,1,1,1,1,0,1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,0,0,0,0,0],dtype=complex)
lts = np.fft.ifft(np.fft.fftshift(lts_fft)); # inverse FFT to get 64 samples in time domain
ltf = np.zeros(160,dtype=complex)
ltf[0:32] = lts[32:64]
ltf[32:96]=lts
ltf[96:160] = lts # repeat the short training sequence 2.5 times -> 32 64 64 = 160
# plt.plot(range(0,160),np.real(ltf))
# ###########################################################################
# # SIGNAL FIELD
# ###########################################################################
ppdu_length = 2000; # payload length in Bytes < 2^12
code_rate = '1/2';
MSC = 'BPSK';
RATE = np.zeros(4);





if MSC == 'BPSK':
    RATE[0:2] = [1,1]
    NDBPS = 24
    NCBPS = 48
    NBPSC = 1
elif MSC == 'QPSK':
    RATE[0:2] = [0,1]
    NDBPS = 48
    NCBPS = 96
    NBPSC = 2
elif MSC == '16-QAM':
    RATE[0:2] = [1,0]
    NDBPS = 96;
    NCBPS = 192;
    NBPSC = 4;
elif MSC == '64-QAM':
    RATE[0:2] = [0,0]
    NDBPS = 192
    NCBPS = 288
    NBPSC = 6

if code_rate == '1/2':
    NDBPS = NDBPS*2*(1/2)
    RATE[2:4] = [0,1]
elif code_rate == '3/4':
    NDBPS = NDBPS*2*(3/4)
    RATE[2:4] = [1,1]
elif code_rate == '2/3':
    NDBPS = NDBPS*2*(2/3)
    RATE[2:4] = [0,1]
    
RES = np.zeros(1) # reserved bit
LENGTH = np.flip((np.array(de2bi(min(ppdu_length,(2**12)-1),12))).T) # length bits in binary
x = np.concatenate((RATE,LENGTH))
PARITY = np.sum(x)%2*np.ones(1) # even parity
TAIL = np.zeros(6) # tail of 6 zeros
sig_bits = np.concatenate((RATE,RES,LENGTH,PARITY,TAIL)) # concatenate all 24 bits together

# convolutional encoder 
sig_bits_encoded = conv_enc(sig_bits,'1/2')
# interleaver
# sig_bits_interleave = wlanBCCInterleave(sig_bits_encoded,'Non-HT',48);

sig_bits_interleave = interleave_symbs(sig_bits_encoded,NCBPS)

sig_bits_modulated = 2*(np.array(sig_bits_interleave).reshape(len(sig_bits_interleave))-(1/2)) # BPSK modulation
p_21 = 1
p_7 = 1
p7 = 1
p21 = -1
sig_fft = np.zeros(64)
sig_fft[range(32-26,32-22+1)] = sig_bits_modulated[0:5]
sig_fft[32+-21] = p_21
sig_fft[range(32-20,32-8+1)] = sig_bits_modulated[5:18]
sig_fft[32+-7] = p_7
sig_fft[range(32+-6,32-1+1)] = sig_bits_modulated[18:24]
sig_fft[range(32+1,32+6+1)] = sig_bits_modulated[24:30]
sig_fft[32+7] = p7
sig_fft[range(32+8,32+20+1)] = sig_bits_modulated[30:43]
sig_fft[32+21] = p21
sig_fft[range(32+22,32+26+1)] = sig_bits_modulated[43:48]

sig_symb = np.fft.ifft(np.fft.fftshift(sig_fft));
sig = np.concatenate((sig_symb[48:64],sig_symb));

preamble = np.concatenate((stf,ltf,sig))

# ###########################################################################
# # PAYLAOD
# ###########################################################################
# service_field = zeros(16,1);
# preMAC = transpose(hexToBinaryVector('08013000',8*4));
# MAC1 = transpose(hexToBinaryVector('FFFFFFFFFFFF',12*4));
# MAC2 = transpose(hexToBinaryVector('EEEEEEEEEEEE',12*4));
# MAC3 = transpose(hexToBinaryVector('AAAAAAAAAAAA',12*4));
# # MAC1 = transpose(hexToBinaryVector('BEAC09BEAC09',12*4));
# # MAC2 = transpose(hexToBinaryVector('BEAC08BEAC08',12*4));
# # MAC3 = transpose(hexToBinaryVector('BEAC07BEAC07',12*4));
# ppdu = zeros((8*ppdu_length),1);
# ppdu_tail=zeros(6,1);

# Nsym = ceil((16+(8*4)+(3*4*12)+16+(8*ppdu_length)+6)/NDBPS);
# Ndata = Nsym*NDBPS;
# Npad = Ndata - (16+(8*4)+(3*4*12)+16+(8*ppdu_length)+6);

# bits_final=[service_field;preMAC;MAC1;MAC2;MAC3;zeros(16,1);ppdu;ppdu_tail;zeros(Npad,1)];


# seed=93;
# scrambled_bits = scrambler(bits_final,seed);
# bits_encoded = conv_enc(scrambled_bits,code_rate);
# ppdu_samples = zeros(80*Nsym,1);
# pilot_polarity = pilot_generator(Nsym+1);
# for n =1:Nsym
#     bits_inter = interleave_symbs(bits_encoded(((n-1)*NCBPS)+(1:NCBPS)),NCBPS);
#     iq_symb_fft = modulate_symbs(bits_inter,pilot_polarity(n+1),MSC);
#     iq_symb = ifft(fftshift(iq_symb_fft));
#     cyclic_prefix = iq_symb(49:64);
#     iq_symb_80 = [cyclic_prefix;iq_symb];
#     ppdu_samples(((n-1)*80)+(1:80)) = iq_symb_80;
#     # modulate and pilots -> 64 samples
#     # cyclic prefix -> take last 16 samples put them at the front and add
#     # to 64
#     # concatenate in time domain
# end

# s = [preamble;ppdu_samples];
