


''' dosrok '''
# def R(n):
#     n = f'{n:b}'
#     if n.count('1') % 2 == 0:
#         n += '0'
#         n = '10' + n[2:]
#     else:
#         n += '1'
#         n = '11' + n[2:]
#     return int(n, 2)
# for n in range(1000):
#     if R(n) > 480:
#         print(n)
#         break

' var15 '
def R(n):
    proizved = 1
    for c in str(n):
        proizved *= int(c)
    summ = sum(map(int, str(n)))
    if summ > proizved:
        return int(str(summ) + str(proizved))
    return int(str(proizved) + str(summ))
for n in range(1000,1,-1): # т.к. трёхзначное число
    if R(n) == 33621:
        print(n)
        break

''' var14 '''
# for n in range(999,99,-1):
#     s = str(n)
#     s1 = int(s[0]) ** 2 + int(s[1]) ** 2
#     s2 = int(s[1]) ** 2 + int(s[2]) ** 2
#     if s1 > s2:
#         result = str(s1) + str(s2)
#     else:
#         result = str(s2) + str(s1)
#     if result == '7434':
#         print(n)
#         break

''' demo '''
# def R(n):
#     b = bin(n)[2:]
#     if n % 2 == 0:
#         b = '10' + b
#     else:
#         b = '1' + b + '01'
#     return int(b,2)
# res = []
# for N in range(1, 12+1):
#     res.append(R(N))
# print(max(res))
# print(res)

'''ДЗ 6'''
# def R(n):
#     b = f'{n:b}'
#     if n % 3 == 0:
#         b += '010'
#     else:
#         b += bin(5 * (n % 3))[2:]
#     return int(b,2)
# minR = (10000,0)
# for n in range(1,1000):
#     if 300 < R(n) < minR[0] and R(n) % 2 == 0:
#         minR = (R(n), n)
# print(minR)

''' ДЗ 4 '''
# def convert_to_trinary(n):
#     res = ''
#     while n > 0:
#         res += str(n%3)
#         n //= 3
#     return res[::-1]
# def R(n):
#     n = convert_to_trinary(n)
#     if sum(map(int,n)) % 3 == 0:
#         n = '20' + n
#     else:
#         n = '10' + n
#     return int(n,3)
# for n in range(1000, 1, -1):
#     if R(n) < 100:
#         print(n)
#         break

"""8BD535"""
# def R(n):
#     b = bin(n)[2:]
#     if b.count('1') % 2 == 0:
#         b += '0'
#         b = '10' + b[2:]
#     elif b.count('1') % 2 != 0:
#         b += '1'
#         b = '11' + b[2:]
#     return int(b,2)
# print(R(6), R(4))
# for n in range(1, 1000):
#     if R(n) > 19:
#         print(n)
#         break



"""0D73A6"""
# def convert_to_trinary(n):
#     res = ''
#     while n > 0:
#         res += str(n%3)
#         n //= 3
#     return res[::-1]
#
# def R(n):
#     n = convert_to_trinary(n)
#     if n[-1]  == '0':
#         n += n[-2:]
#     else:
#         n += convert_to_trinary(int(n, 3) % 3 * 5)
#     return int(n,3)
#
# print(R(11) ==  307, R(12) == 111)
# for n in range(10000, 1, -1):
#     if R(n) < 159:
#         print(n)
#         break

'''2.7'''
# def isPrime(n):
#     for i in range(2, int(n ** 0.5)):
#         if n % i == 0:
#             return False
#     return True
# print(isPrime(7))
# def R(n):
#     b = bin(n)[2:]
#     if isPrime(sum(map(int, b))):
#         b += b[-3:]
#     else:
#         b = b[::-1] + bin(n % 4 * 4)[2:]
#     return b
# for n in range(1, 100000):
#     if len(set(str(n))) > 3:
#         res = R(n)
#         if int(res,2) > 100000 and isPrime(int(res,2)):
#             print(n)
#             break

'''2.6'''
# for n in range(1,100):
#    b= bin(n)[2:]
#    if n%5==0:
#         b = b + b[-3] +b[-2]+ b[-1]
#    else:
#        a= n%5 *4
#        b= b+ bin(a)[2:]
#    r= int(b,2)
#    if r >150:
#        print(n)
#        break

'''2.1'''
# def R(n):
#     b = bin(n)[2:]
#     if len(b) % 2 == 0:
#         b = b[:len(b) // 2] + '1' + b[len(b) // 2:]
#     return b
# res = []
# for n in range(1,1000):
#     if int(R(n),2) <= 68:
#         res.append(n)
# print(max(res))

'''4'''
# import string
#
# def convert_to(n, base):
#     digits = '0123456789' + string.ascii_uppercase
#     res = ''
#     while n > 0:
#         res += digits[ n % base ]
#         n //= base
#     return res[::-1]
# def R(n):
#     s = convert_to(n, 17)
#     s = s.replace('5', 'F')
#     summ = 0
#     for c in s:
#         summ += int(c, 17)
#     if summ % 2 == 0:
#         s += '11'
#     else:
#         s = '42' + s
#     return int(s[::-1], 17)
# for N in range(3,1000):
#     res = R(N)
#     if  res % 7 == 0 and res > 290:
#         print(N)
#         break

'''3'''
# count = 0
# def alg(n):
#     bin_n = bin(n)[2:]
#     while len(bin_n) < 8:
#         bin_n = '0' + bin_n
#     if (int(bin_n[1]) + int(bin_n[4])) % 2 == 0:
#         bin_n = '1' + bin((int(bin_n[1]) + int(bin_n[4])))[2:] + bin_n
#     elif int(bin_n[1]) % 2 != 0:
#         bin_n += '1'
#     return int(bin_n,2)
# for n in range(2, 257):
#     res = alg(n)
#     if str(res).count('5') > 0 and res % 2 != 0:
#         print(res)
#         count += 1
# print(alg(204))
# print(count)
# ИЛИ
# def R(n):
#     b = bin(n)[2:]
#     while len(b) < 8:
#          b = '0' + b
#     b = list(map(int, b))
#     if (b[1] + b[4]) % 2 == 0:
#         b = [1] + list(bin(b[1] + b[4])[2:]) + b
#     elif b[1] % 2 != 0:
#         b += [1]
#     k = list(map(str, b))
#     res = ''
#     for i in k:
#         res += i
#     return int(res,2)
# cnt = 0
# for N in range(3,256):
#     res = R(N)
#     if res % 2 != 0 and '5' in str(res):
#         cnt += 1
# print(cnt)

''' 2 '''
# def R(n):
#     bin_n = bin(n)[2:]
#     numbers = list(int(c) for c in bin_n)
#     if sum(numbers) % 2 == 0:
#         bin_n += "10"
#         bin_n = "10" + bin_n[2:]
#     if sum(numbers) % 2 != 0:
#         bin_n += "01"
#         bin_n = "11" + bin_n[2:]
#     return int(bin_n, 2)
# for N in range(1000):
#     if R(N) > 102:
#         print(N)
#         break

''' 1 '''
# def R(n):
#     s = bin(n)[2:]
#     if n % 2 == 0:
#         s = s + s[-2] + s[-1]
#     else:
#         s = '1' + s + '0'
#     return int(s,2)
# for n in range(1,1000):
#     if R(n) > 1038:
#         print(n)
#         break
# # Или
# for i in range(1,1000):
#     i_bin = bin(i)[2:]
#     if i_bin[-1] == '0':
#         i_bin = i_bin + i_bin[-2] + i_bin[-1]
#     if i_bin[-1] == '1':
#         i_bin = '1' + i_bin + '0'
#     if int(i_bin,2) > 1038:
#         print(i)
#         break



