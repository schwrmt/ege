def dividers(n):
    divs = list()
    for d in range(2,int(n**0.5) + 1):
        if n % d == 0:
            divs.append(d)
            divs.append(n//d)
    return sorted(divs)
cnt_anwsers = 0
for n in range(1_481_0112, 10**10):
    divs = dividers(n)
    if not divs:
        continue
    prime_divs = [x for x in divs if len(dividers(x)) == 0 and str(x).count('7') == 1]
    if len(divs) == 2 :
        if len(prime_divs) == 2:
            print(n, max(divs))
            cnt_anwsers += 1
    if cnt_anwsers == 5:
        break


'''19779'''
from xml.sax.handler import feature_namespaces

# def dividers(n):
#     divs = set()
#     for d in range(2,int(n**0.5) + 1):
#         if n % d == 0:
#             divs.add(d)
#             divs.add(n//d)
#     return sorted(divs)
# cnt_answers = 0
# for n in range(55_000_001, 10**10):
#     divs = dividers(n)
#     if not divs: # len(divs) == 0
#         continue
#     min_div_end_in_777 = -1
#     for d in divs:
#         if d % 1000 == 777 and d != 777: #str(d)[-3:] == '777'
#             min_div_end_in_777 = d
#             break
#     if min_div_end_in_777 != -1:
#         print(n, min_div_end_in_777)
#         cnt_answers += 1
#     if cnt_answers == 4:
#         break

'''var2'''
# def dividers(n):
#     divs = set()
#     for d in range(2,int(n**0.5)+1):
#         if n % d == 0:
#             divs.add(d)
#             divs.add(n//d)
#     return sorted(divs)
# cnt = 0
# for n in range(1_000_000, 10**10):
#     if cnt == 5:
#         break
#     divs = dividers(n)
#     if not divs:
#         continue
#     M = min(divs) + max(divs)
#     if M % 10 == 6:
#         print(n,M)
#         cnt += 1

'''var5'''
# import string
# from itertools import product
# res = set()
# for l in 0,1,2,3:
#     for a1 in product(string.digits, repeat = l):
#         for a2 in string.digits:
#                 for a3 in string.digits:
#                     a1 = ''.join(a1)
#                     a = int(f'1{a1}34{a2}5{a3}9')
#                     if a % 31007 == 0:
#                         res.add(a)
# for r in sorted(res):
#     print(r,r//31007)

'''var8'''
# import string
# from itertools import product
# res = set()
# for a1 in string.digits:
#     for a2 in string.digits:
#         for l in 0,1,2:
#             for a3 in product(string.digits, repeat=l):
#                 a = int(f'{a1}79{a2}8{''.join(a3)}3')
#                 if a % 3377 == 0:
#                     res.add(a)
# for a in sorted(res):
#     print(a, a // 3377)

'''VAR10'''
# from fnmatch import fnmatch
# from itertools import product
# import string
# for n in range(123,10**8,123):
#     if fnmatch(str(n),'32*823'):
#         print(n, n//123)
# res = set()
# for l1 in 0,1,2,3:
#     for a1 in product(string.digits, repeat=l1):
#         a = int(f'32{''.join(a1)}823')
#         if a % 123 == 0:
#             res.add(a)
# for a in sorted(res):
#     print(a,a//123)

'''var18'''
# def dividers(n):
#     divs = set()
#     for d in range(2,int(n**0.5) + 1):
#         if n % d == 0:
#             divs.add(d)
#             divs.add(n//d)
#     return sorted(divs)
# cnt_anwsers = 0
# for n in range(850_001, 10**10):
#     divs = dividers(n)
#     if not divs:
#         continue
#     F = max(divs) - min(divs)
#     if F % 5 == 0:
#         print(n, F)
#         cnt_anwsers += 1
#     if cnt_anwsers == 6:
#         break

'''ЕГКР 19.04.25'''
# import string
# from itertools import product
# res = set()
# for l1 in range(5):
#     for a1 in product(string.digits, repeat=l1):
#         for l2 in range(5-l1):
#             for a2 in product(string.digits, repeat=l2):
#                 a1 = ''.join(a1)
#                 a2 = ''.join(a2)
#                 a = int(f'4{a1}4736{a2}1')
#                 if a % 7993 == 0:
#                     res.add(a)
# for r in sorted(res):
#     print(r,r//7993)
#
# from fnmatch import fnmatch
# for a in range(7993,10**10,7993):
#     if fnmatch(str(a), '4*4736*1'):
#         print(a, a//7993)

'''661336'''
# from fnmatch import *
#
# for n in range(3023, 10**8, 3023):
#     if fnmatch(str(n),'3?5*2?7'):
#         print(n, n//3023)
# import string
# from itertools import product
# res = set()
# for a1 in string.digits:
#     for a3 in string.digits:
#         for l in range(2+1):
#             for a2 in product(string.digits, repeat=l):
#                 a2 = ''.join(a2)
#                 n = int(f'3{a1}5{a2}2{a3}7')
#                 if n % 3023 == 0:
#                     res.add(n)
# for r in sorted(res):
#     print(r, r//3023)

'''демовариант делители'''
# def dividers(n):
#     dividers = set()
#     for x in range(2, int(n**0.5) + 1):
#         if n % x == 0:
#             dividers.add(x)
#             dividers.add(n//x)
#     return dividers
# cnt_answers = 0
# for n in range(800000,10**100):
#     div = dividers(n)
#     if not div: # нет делителей кроме 1 и самого числа
#         continue
#     M = min(div) + max(div)
#     if str(M)[-1] == '4':
#         print(n, M)
#         cnt_answers += 1
#     if cnt_answers == 5:
#         break

'''демовариант маски'''
# import time
# from fnmatch import *
# start_time = time.time()
# for x in range(1917, 10**10+1, 1917):
#     if fnmatch(str(x), '3?12?14*5'):
#         print(x, x//1917)
# end_time = time.time()
# print(end_time - start_time)
#
# from itertools import *
# import string
# import time
# start_time = time.time()
# res = set()
# for a1 in string.digits:
#     for a2 in string.digits:
#         for l in 0, 1,2:
#             for a3 in product(string.digits, repeat=l):
#                 a3 = ''.join(a3)
#                 a = int(f'3{a1}12{a2}14{a3}5')
#                 if a % 1917 == 0:
#                     res.add(a)
# for a in sorted(res):
#     print(a, a//1917)
# end_time = time.time()
# print(end_time - start_time)

'''dosrok2025'''
# def dividers(n):
#     dividers = set()
#     for x in range(2, int(n**0.5) + 1):
#         if n % x == 0:
#             dividers.add(x)
#             dividers.add(n//x)
#     return sorted(dividers)
# cnt = 0
# for n in range(1125000, 10 ** 100):
#     divs = dividers(n)
#     if not divs:
#         continue
#     min_div_end_in_7 = -1
#     for d in divs:
#         if d != 7 and d % 10 == 7:
#             min_div_end_in_7 = d
#             break
#     if min_div_end_in_7 != -1:
#         print(n, min_div_end_in_7)
#         cnt += 1
#     if cnt == 5:
#         break

''' 953C66 '''
# def dividers(n):
#     dividers = set()
#     for x in range(2, int(n**0.5) + 1):
#         if n % x == 0:
#             dividers.add(x)
#             dividers.add(n//x)
#     return dividers
# cnt = 0
# for n in range(500_000,10**100):
#     if cnt == 5:
#         break
#     div = dividers(n)
#     r = sum(dividers(n))
#     if r % 10 == 7:
#         print(n, r)
#         cnt += 1
