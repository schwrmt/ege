import string
numbers = string.digits + string.ascii_uppercase
for x in numbers[:14]:
    for y in numbers[:14]:
        a = int(f'ABCD3{y}2{x}1', 14) + int(f'192{x}9', 14)
        if a % 107 == 0:
            print(a // 107)
            break
















# digits = string.digits + string.ascii_uppercase
# def convert_to(n,base):
#     result = ''
#     numbers = string.digits + string.ascii_uppercase
#     while n > 0:
#         result += numbers[n % base]
#         n //= base
#     return result[::-1]
# a = 16 ** 44 * 16 ** 30 - (32**5 * (8**40 - 8**32) * (16**17 - 32**4))
# a_16 = convert_to(a, 16)
# a_16 = a_16.replace('E', '1')
#
# print(a_16)
#
# a_16 = a_16[:-5] + a_16[-4:]
# print(a_16)
# print(a_16.count('1'))



''' dosrok '''
# digits = string.digits + string.ascii_uppercase
# for x in digits[:21]:
#     a = int(f'82934{x}2',21) + int(f'2924{x}{x}7',21) + int(f'67564{x}8',21)
#     if a % 20 == 0:
#         print( a // 20)
#         break

''' var15 '''
# a = 2 * 3**2022 + 5 * 3**1800 + 3**1001 + 4 * 3**1000 + 3
# count = 0
# while a > 0:
#     if a % 9 == 0:
#         count += 1
#     a //= 9
# print(count)

''' 62CE57 '''
# for x in range(2030, 0, -1):
#     a = 5**150 + 5**100 - x
#     a_5 = ''
#     while a > 0:
#         a_5 = str(a % 5) + a_5
#         a //= 5
#     if a_5.count('0') == 50:
#         print(x)
#         break

''' 404DD6 '''
# digits = string.digits + string.ascii_uppercase
# # '0123456789ABCDFH....XYZ'
# print(digits[:19])
# for x in digits[:19]:
#     a = int(f'98{x}79731', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)
#     if a % 18 == 0:
#         print(a // 18)
#         break

'''DE4AE1'''
# zero_count_max = (0, 0)
# for x in range(1,2030+1):
#     a = 7**170 + 7**100 - x
#     a_7 = ''
#     while a > 0:
#         a_7 += str(a % 7)
#         a //= 7
#     a_7 = a_7[::-1]
#     if zero_count_max[0] <= a_7.count('0'):
#         zero_count_max = (a_7.count('0'), x)
# print(zero_count_max)

''' 3D5C96 '''
# for x in range(2035,0,-1):
#     n = 3 ** 100 - x
#     count_0 = 0
#     while n > 0:
#         if n % 3 == 0:
#             count_0 += 1
#         n //= 3
#     if count_0 == 2:
#         print(x)
#         break

''' 551280 '''
# x=2*729**2014+2*243**2016-2*81**2018+2*27**2020-2*9**2022-2024
# a=[]
# while x>0:
#     a = [x%27]+a
#     x = x//27
# count =0
# for i in range(10,27):
#     count += a.count(i)
# print(count)
# # или
# a = 2*729**2014+2*243**2016-2*81**2018+2*27**2020-2*9**2022-2024
# def convert(n, base):
#     res = ''
#     numbers = '0123456789' + string.ascii_uppercase
#     while n > 0:
#         res += numbers[n % base]
#         n //= base
#     return res[::-1]
# result = convert(a, 27)
# # print(set(result))
# # print(result.count('Q') + result.count('O'))
# count = 0
# for c in string.ascii_letters:
#     count += result.count(c)
# print(count)



''' ДЗ 1'''
# a = 3 * 3125**9 + 2 * 625**8 - 4*625**7 + 3 * 125**6 - 2 * 25**5 - 2024
# cnt = 0
# while a > 0:
#     if a % 25 == 0:
#         cnt +=1
#     a //= 25
# print(cnt)
# # ИЛИ
# a = 3 * 3125**9 + 2 * 625**8 - 4*625**7 + 3 * 125**6 - 2 * 25**5 - 2024
# def convert_to(n,base):
#     digits = string.digits + string.ascii_uppercase
#     res = ''
#     while n > 0:
#         res += digits[n % base]
#         n //= base
#     return res[::-1]
# print(convert_to(a,25).count('0'))

''' ДЗ 2'''
# a = 361 * 2349**84 - 89**192 + 1953**481 * 4843**151
# cnt = 0
# while a > 0:
#     if a % 9 == 5:
#         cnt += 1
#     a //= 9
# print(cnt)

''' ДЗ 3'''
# a = 7 * 5**123 + 6 * 5**111 - 5 * 25**50 + 4 * 125**30 - 3 * 5**10
# cnt = 0
# while a > 0:
#     if a % 5 == 4:
#         cnt += 1
#     a //= 5
# print(cnt)

''' ДЗ 4'''
# digits = string.digits + string.ascii_uppercase
# def convert_to(n, base):
#     digits = string.digits + string.ascii_uppercase
#     result = ""
#     while n > 0:
#         result += digits[ n % base ]
#         n //= base
#     return result[::-1]
# for x in digits[:19]:
#     if (int(f"78{x}79643", 19) + int(f"25{x}43", 19) + int(f"63{x}5", 19)) % 18 == 0:
#         print((int(f"78{x}79643", 19) + int(f"25{x}43", 19) + int(f"63{x}5", 19)) // 18)
#         break



''' 2.1.5 '''
# a = 283**382 + 9**15 + 2**3
# def convert_to(n,base):
#     result = ''
#     numbers = '0123456789' + string.ascii_letters
#     while n > 0:
#         result += numbers[n % base]
#         n //= base
#     return result[::-1]
# res = convert_to(a,14)
# print(abs(res.count('B') - res.count('C')))


''' 2.1.1. '''
# a = 2 * 729 ** 333 + 2 * 243 ** 334 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338
# def convert_to9(n):
#     result = ''
#     while n > 0:
#         result += str(n % 9)
#         n //= 9
#     return result[::-1]
#
# print(len(convert_to9(a)) - convert_to9(a).count('0'))
# ### Или
# a = 2 * 729**333 + 2 * 243**334 - 81**335 + 2 * 27**336 - 2 * 9 ** 337 - 338
# count = 0
# a1 = a
# while a1 > 0:
#     if a1 % 9 != 0:
#         count += 1
#     a1 //= 9
# print(count)



''' 2.3.4 '''
# def trio(n):
#     output = ''
#     while n > 0:
#         output += str(n % 3)
#         n //= 3
#     return int(output[::-1])
# for x in range(2030, 1, -1):
#     if str(trio(3**100 - x)).count('0') == 5:
#         print(x)
#         break

''' 2.3.2 '''
# def convert(n, base):
#     res = ''
#     numbers = '0123456789' + string.ascii_letters
#     while n > 0:
#         res += numbers[n % base]
#         n //= base
#     return res[::-1]
# for x in range(1, 2031):
#     a = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
#     if convert(a, 6).count('0') == 202:
#         print(x)
#         break

''' 1.17 '''
# digits = '0123456789' + string.ascii_lowercase
# for p in range(14, 37):
#     for x in digits[:p]:
#         for y in digits[:p]:
#             if (int(f'1{x}{y}1',p) + int(f'{x}{y}{x}9',p)) == int(f'D65{y}', p):
#                 print(int(f'{x}{x}{y}',p))

''' 1.16 '''
# digits = '0123456789' + string.ascii_uppercase
# for x in digits[:14]:
#     for y in digits[:14]:
#         a = int(f'ABCD3{y}2{x}1', 14) + int(f'192{x}9',14)
#         if a % 107 == 0:
#             print(a // 107)
#             break

''' 1.9 '''
# a = 77777 ** 290 - 777 ** 29 + 77 ** 2 - 7
# a_20 = []
# while a > 0:
#     a_20 += [a % 20]
#     a //= 20
# print(len(set(a_20)))

''' 1.2 '''
# digits = string.digits + string.ascii_uppercase
# def convert_to(n,base):
#     result = ''
#     numbers = string.digits + string.ascii_uppercase
#     while n > 0:
#         result += numbers[n % base]
#         n //= base
#     return result[::-1]
# for x in digits[:22]:
#     a= int(f'5AG{x}2',22) + int(f'6{x}2{x}7',22)
#     n = convert_to(a, 9)
#     if n.count('7') == 2:
#         print(int(f'5AG{x}',22) + int(f'6{x}2{x}7',22))

''' 1.1 '''
# digits = '0123456789' + string.ascii_uppercase + string.ascii_lowercase + 'АБВГД'
# global d
# d = {}
# for i in range(67):
#     d[digits[i]] = i
#
# def int67(x):
#     a = list(x)[::-1]
#     s = 0
#     for i in range(len(a)):
#         s += d[a[i]] * (67 ** i)
#     return s
#
# for x in digits:
#     for y in digits:
#         if (int67(f'5{y}{x}{y}1') + int67(f'4{x}{y}27')) % 5437 == 0:
#             print(hex((int67(f'5{y}{x}{y}1') + int67(f'4{x}{y}27')) // 5437)[2:])
# # ИЛИ
# for x in range(67):
#     for y in range(67):
#         if ( (5*67**4 + y*67**3 + x*67**2 + y*67**1 + 1*67**0) + (4*67**4 + x*67**3 + y*67**2 + 2*67**1 + 7*67**0)) % 5437 == 0:
#             print(hex((5*67**4 + y*67**3 + x*67**2 + y*67**1 + 1*67**0 + 4*67**4 + x*67**3 + y*67**2 + 2*67**1 + 7*67**0) // 5437))
