# short training sequence length
sts_len = 16
# short training sequence cycles
sts_cyc = 10
# total short training field length
stf_len = sts_len*sts_cyc
# long training sequence length
lts_len = 64
# long training sequence cycles
lts_cyc = 2.5
# total long training field length
ltf_len = lts_len*lts_cyc
# cyclic prefix length
cyc_prefix_len = 16
# symbol length
symb_len = 64
sig_len = cyc_prefix_len + symb_len
# minimum packet length
pkt_min_len = stf_len + ltf_len + sig_len
# short training field fft
stf_fft = [0, 0, 0, 0, 0, 0, 0, 0, 1+1j, 0, 0, 0, -1-1j, 0, 0, 0, 1+1j, 0, 0, 0, -1-1j, 0, 0, 0, -1-1j, 0, 0, 0, 1+1j, 0, 0, 0, 0, 0, 0, 0, -1-1j, 0, 0, 0, -1-1j, 0, 0, 0, 1+1j, 0, 0, 0, 1+1j, 0, 0, 0, 1+1j, 0, 0, 0, 1+1j, 0, 0, 0, 0, 0, 0, 0]
# ltf_fft = (1+(0*1j))*[0,0,0,0,0,0,1,1,-1,-1,1,1,-1,1,-1,1,1,1,1,1,1,-1,-1,1,1,-1,1,-1,1,1,1,1,0,1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,1,0,0,0,0,0,]
ltf_fft = [0 + (0*1j),0 + (0*1j),0 + (0*1j),0 + (0*1j),0 + (0*1j),0 + (0*1j),1 + (0*1j),1 + (0*1j),-1 + (0*1j) + (0*1j),-1 + (0*1j) + (0*1j),1 + (0*1j),1 + (0*1j),-1 + (0*1j) + (0*1j),1 + (0*1j),-1 + (0*1j) + (0*1j),1 + (0*1j),1 + (0*1j),1 + (0*1j),1 + (0*1j),1 + (0*1j),1 + (0*1j),-1 + (0*1j) + (0*1j),-1 + (0*1j) + (0*1j),1 + (0*1j),1 + (0*1j),-1 + (0*1j) + (0*1j),1 + (0*1j),-1 + (0*1j) + (0*1j),1 + (0*1j),1 + (0*1j),1 + (0*1j),1 + (0*1j),0 + (0*1j),1 + (0*1j),-1 + (0*1j) + (0*1j),-1 + (0*1j) + (0*1j),1 + (0*1j),1 + (0*1j),-1 + (0*1j) + (0*1j),1 + (0*1j),-1 + (0*1j) + (0*1j),1 + (0*1j),-1 + (0*1j) + (0*1j),-1 + (0*1j) + (0*1j),-1 + (0*1j) + (0*1j),-1 + (0*1j) + (0*1j),-1 + (0*1j) + (0*1j),1 + (0*1j),1 + (0*1j),-1 + (0*1j) + (0*1j),-1 + (0*1j) + (0*1j),1 + (0*1j),-1 + (0*1j) + (0*1j),1 + (0*1j),-1 + (0*1j) + (0*1j),1 + (0*1j),1 + (0*1j),1 + (0*1j),1 + (0*1j),0 + (0*1j),0 + (0*1j),0 + (0*1j),0 + (0*1j),0 + (0*1j)]

k48 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
