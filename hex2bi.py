def hex2bi(hex_str):
    bin_str=format(int(hex_str, 16), "4b")
    bin_int=[]         
    for i in range(len(bin_str)):
        if bin_str[i]=='1':
            bin_int.append(1)
        else:
            bin_int.append(0)    
    return bin_int
      

 