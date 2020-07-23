def bi2de(binary):
    x = 0
    for n in range(0,len(binary)):
        x = x + (binary[n]*(2**n))
    return x

# def binarytodecimal(binary):
#     binary1 = binary
#     decimal, i, n = 0, 0, 0
#     while binary != 0:
#         dec = binary % 10
#         decimal = decimal + dec * pow(2, i)
#         binary = binary // 10
#         i += 1
#     return decimal


# def bi2de(lengthn):
#     length = str(lengthn)
#     length = ''.join(length)
#     print(length)
#     length_dec = binarytodecimal(length)
#     return length_dec

