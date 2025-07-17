'''DV2'''
# def conv_to_3(n):
#     res = ''
#     while n > 0:
#         res = str(n%3) + res
#         n //= 3
#     return res
# def R(n):
#     r = conv_to_3(n)
#     if n % 3 == 0:
#         r = '1' + r + '02'
#     else:
#         r += conv_to_3((n % 3) * 4)
#     return int(r,3)
# for n in range(1, 1000):
#     if R(n) > 135:
#         print(n)
#         break
'''DV1'''
# def conv_to_3(n):
#     res = ''
#     while n > 0:
#         res = str(n%3) + res
#         n //= 3
#     return res
# def R(n):
#     r = conv_to_3(n)
#     if n % 3 == 0:
#         r += r[-2:]
#     if n % 3 != 0:
#         r += conv_to_3((n % 3) * 5)
#     return int(r,3)
# for n in range(1,1000):
#     if R(n) >= 290:
#         print(n)
#         break

'''21473'''
# def convert_to_3(n):
#     res = ''
#     while n > 0:
#         res = str(n%3) + res
#         n //= 3
#     return res
# def R(n):
#     r = convert_to_3(n)
#     sm = sum(map(int,r))
#     if sm % 4 == 0:
#         r = r.replace('2', '*').replace('1', '2').replace('*','1')
#         r = '10' + r
#     else:
#         r += '20'
#         r = r[0] + '02' + r[3:]
#     return int(r,3)
# minR = 1000000
# n_pri_minR = -1
# for n in range(1,10000):
#     r = R(n)
#     if r > 302 and r <= minR:
#         minR = r
#         n_pri_minR = n
# print(n_pri_minR)

'''ege2024_3'''
# def R(n):
#     r = bin(n)[2:]
#     r += str(r.count('1') % 2)
#     r += str(r.count('1') % 2)
#     return int(r,2)
# min_R = 10000000
# for n in range(1,1000):
#     r = R(n)
#     if 75 < r < min_R:
#         min_R = r
# print(min_R)

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

'''var18'''
# def R(n):
#     r = n - n % 4
#     r = bin(r)[2:]
#     r += str(r.count('1') % 2)
#     r += str(r.count('1') % 2)
#     return int(r,2)
# min_R = 1000000000
# for n in range(1,1000):
#     r = R(n)
#     if 100 < r < min_R:
#         min_R = r
# print(min_R)

''' var15 '''
# def R(n):
#     proizved = 1
#     for c in str(n):
#         proizved *= int(c)
#     summ = sum(map(int, str(n)))
#     if summ > proizved:
#         return int(str(summ) + str(proizved))
#     return int(str(proizved) + str(summ))
# for n in range(1000,1,-1): # т.к. трёхзначное число
#     if R(n) == 33621:
#         print(n)
#         break

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



'''var8'''
# def convert_to(n, a):
#     res = ''
#     while n > 0:
#         res = str(n%a) + res
#         n //= a
#     return res
# def R(n):
#     r = convert_to(n, 4)
#     if n % 4 == 0:
#         r += r[-2:]
#     else:
#         r += convert_to((n % 4) * 2, 4)
#     return int(r,4)
# for n in range(1,1000):
#     if R(n) > 1088:
#         print(n)
#         break

'''var7'''
# def z(n,m):
#     b = ''
#     while n > 0:
#         b = str(n % m) + b
#         n //= m
#     return b
#
# def f(N):
#     b = z(N,4)
#     if N % 4 == 0:
#         b += b[-2:]
#     else:
#         b += z((N % 4) * 2, 4)
#     return int(b,4)
#
# print(min(N for N in range(1,1000) if f(N) >= 1025))
# for n in range(1,1000):
#     if f(n) >= 1025:
#         print(n)
#         break

'''var5'''
# def convert_to(n,k):
#     res = ''
#     while n > 0:
#         res += str(n%k)
#         n//=k
#     return res[::-1]
# def R(n):
#     r = convert_to(n, 4)
#     if n % 4 == 0:
#         r += r[-2:]
#     else:
#         r += convert_to((n % 4) * 2, 4)
#     return int(r,4)
# for n in range(10000,-1,-1):
#     if R(n) < 261:
#         print(n)
#         break


'''var3'''
# def R(n):
#     r = bin(n)[2:]
#     if n % 4 == 0:
#         r += r
#     else:
#         r += r[::-1]
#     return int(r,2)
# for n in range(1,1000):
#     if R(n) >= 544:
#         print(n)
#         break

'''var2'''
# def R(n):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = r.replace('1', '11')
#     else:
#         r = r.replace('0','00')
#     return int(r,2)
# for n in range(1, 10000):
#     r = R(n)
#     if r < 70 and r != n:
#         print(n)

'''var1'''
# def R(n):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = r.replace('1','11')
#     else:
#         r = r.replace('0','00')
#     return int(r,2)
# print(R(4) == 12 and R(5) == 9)
# for n in range(1,1000):
#     if R(n) > 70:
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



