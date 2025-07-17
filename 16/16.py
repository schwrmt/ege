



'''dosrok_2025'''
# import sys
#
# sys.setrecursionlimit(3000)
# def F(n):
#     if n <= 5:
#         return 1
#     if n > 5:
#         return n+ F(n-2)
# print(F(2126)-F(2122))

'''EGKR19.04.25'''
# import sys
# sys.setrecursionlimit(10000)
# def F(n):
#     if n < 20:
#         return n
#     if n >= 20:
#         return (n-6) * F(n-7)
# print((F(47872) - 290 * F(47865)) / F(47858))

'''var1'''
# import sys
# sys.setrecursionlimit(4000)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * F(n-1)
# print((F(2025)//25 + F(2024))/F(2023))

'''var16'''
@lru_cache
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return n * (n-1) + F(n-1) + F(n-2)
for n in range(1,2000):
    F(n)
print(F(2023) - F(2021) - 2 * F(2020) - F(2019))

# 15 вариант
# def F(n):
#     if n <= 1:
#         return 1
#     if n > 1 and n % 2 != 0:
#         return 3 * F(n-1) * F(n-2) - F(n-1) -F(n-2)
#     if n > 1 and n % 2 == 0:
#         return 2 * F(n-1)
# print(F(20))

#3доп
# f = [0] * 5000
# def F(n):
#     if n < 4 or n % 2 != 0:
#         f[n] = 1
#     if n > 3 and n % 2 == 0:
#         f[n] = f[n-1] + f[n-2] + f[n-3]
# for i in range(5000):
#     F(i)
# print(f[4008] - f[4002])
# # ИЛИ
# results = [-1] * 4300 # -1 => значение не подсчитано
# def F(n):
#     if results[n] != -1:
#         return results[n]
#     if n < 4 or n % 2 != 0:
#         return 1
#     if n > 3 and n % 2 == 0:
#         return F(n-1) + F(n-2) + F(n-3)
# for i in range(1,4020):
#     results[i] = F(i)
# print(results[4008] - results[4002])
# # ИЛИ
# from functools import lru_cache
# from sys import setrecursionlimit
# setrecursionlimit(2000)
# @lru_cache()
# def F(n):
#     if n < 4 or n % 2 != 0:
#         return 1
#     if n > 3 and n % 2 == 0:
#         return F(n-1) + F(n-2) + F(n-3)
# for i in range(1, 4005):
#     F(i)
# print(F(4008) - F(4002))
# for n in range(1, 20):
#     print(f'{n}: {F(n)}')
# def F_new(n):
#     if n % 2 != 0:
#         return 1
#     else:
#         return n - 1
# print(F_new(4008) - F_new(4002))

#1доп
# def fact(n):
#     p = n
#     for i in range(1,n):
#         p *= i
#     return p
# res = [0] * 5002
# for i in range(5001, 1 ,-1):
#     if i > 5000:
#         res[i] = fact(i)
#     else:
#         res[i] = res[i + 1] // (i + 1)
# print(res[12]/res[4])

#Демо-вариант
# import sys
# sys.setrecursionlimit(3000)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return (n - 1) * F(n - 1)
# print((F(2024) + 2 * F(2023)) / F(2022))

#16
#
# def F(n):
#     if n <= 3:
#         return 1
#     if n % 2 == 0 and n > 3:
#         return F(n / 5 - 3)
#     if n % 2 > 0 and n > 3:
#         return n*n*n
# for i in range(100):
#     if F(i) > 559:
#         print(i)
#         break

#15
# def F(n):
#     if n <= 19:
#         return n*n*n + 22
#     if n % 3 == 0 and n > 19:
#         return F(n-4) + F(n-8)
#     if n % 3 != 0 and n > 19:
#         return F(n-9) + n + 7
#
# def StrWithNoOddNumbers(s):
#     for c in s:
#         if int(c) % 2 != 0:
#             return False
#     return True
#
# count = 0
#
# for i in range(1,101):
#     flag = True
#     res = F(i)
#     while res > 0:
#         if res % 2 != 0:
#             flag = False
#             break
#         res //= 10
#     if flag:
#         count += 1
#      # if StrWithNoOddNumbers(str(F(i))):
#     #     count += 1
# print(count)

#14
# def F(n):
#     if n == 2:
#         return 1
#     return 4 * F(n-1) + 2 * G(n-1) - n * 3 + 8
# def G(n):
#     if n == 2:
#         return 1
#     return 3 * F(n-1) + 3* G(n-1) + n
# print(F(16)+ G(16))

#9
# def F(n):
#     if n < 3:
#         return 1
#     if n > 2:
#         return F(n-1) + F(n-2)
# def F_new(n):
#     n1 = 1
#     n2 = 1
#     for i in range(n-1):
#         n1, n2 = n2, n1 + n2
#     return n1
# def G_new(n):
#     return (1 + n) * n / 2
# def G(n):
#     if n >= 2:
#         return n + G(n-1)
#     return 1
# print((G_new(123456789)-F_new(65))//F_new(12))

#8
# import sys
# sys.set_int_max_str_digits(100000)
#
# def F(n):
#     if n <= 10000:
#         return Fact(n)
#     if n > 10000 and n % 2 == 0:
#         return F((n // 2) - 123) + n
#     if n > 10000 and n % 2 != 0:
#         return F(n - 1) + Fact(n//100) + 2
#
# # def G(n):
# #     if n == 1:
# #         return 1
# #     if n >= 2:
# #         return n * G(n-1)
# # for x in range(10):
# #     print(x, G(x))
# def Fact(n):
#     res = 1
#     for x in range(1,n+1):
#         res *= x
#     return res
# print(sum((map(int,str(F(1234567)+Fact(100))))))

#7
# def F(n, m):
#     if n == 0:
#         return m
#     if n > 0:
#         return F(n // 10, 10 * m + (n % 10))
# s = 1030223
# print( str(F(s,0)))

#6
# def F(n, m):
#     if n == 0 and m == 0:
#         return 0
#     if n > m:
#         return F(n-1,m) + m
#     if n <= m and m > 0:
#         return F(n,m-1) + n
# print(F(10, 15))
# cnt = 0
# for i in range(1, int(8388608 ** 0.5) + 1):
#     if 8388608 % i == 0:
#         cnt += 2
# print(cnt)

#5

# @lru_cache()
# def F(n):
#     if n == 1:
#         return 1
#     if n >= 2:
#         return F(n-1) + 3 * G(n-1) + n
# @lru_cache()
# def G(n):
#     if n == 1:
#         return 1
#     if n >= 2:
#         return 11 * F(n-1) + G(n-1) * 2 - n * n
# print( F(28) // G(14))

#4
# def F(n):
#     if n >= 2023:
#         return n
#     if n < 2023:
#         return n // 3 + F(n + 2)
# print( F(2015) - F(2018))

#3
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 3 * F(n-1) - G(n-1)
# def G(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2 * F(n-1) + 2 * G(n-1) + n * n
# print(sum(map(int, str(G(5)))))

#2
# def F(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 2
#     if n % 2 == 0 and n > 1:
#         return 7 + int(3 * F(n - 2) / 2)
#     if n % 2 != 0 and n > 1:
#         return 6 * n + int((F(n-2) + F(n-1) + 8)/5)
# print(F(71))

#1
# def F(n):
#     if n == 1 or n == 0:
#         return 5
#     if n > 1 and n % 5 == 0:
#         return F(n-5) // 3 + 9
#     if n > 1 and n % 5 > 0:
#         return F(n - (n%5)) + n * 2
# print(F(42))

# ДЗ 6

# import sys
# sys.setrecursionlimit(1000)
# def F(x):
#     if x >= 4040:
#         return x
#     if x < 4040:
#         return x + 4 + F(x+4)
# print(F(3)-F(15))

# ДЗ 5

# import sys
# sys.setrecursionlimit(5000)
# def F(n):
#     if n >= 10000:
#         return 1
#     if n < 10000 and n % 2 == 0:
#         return F(n+3) + 7
#     return F(n+1) - 3
# print(F(50)-F(57))

# ДЗ 4

# def F(n):
#     if n >= 2222:
#         return n
#     if n < 2222:
#         return F(n+5)+7
# print(F(45)-F(49))

# ДЗ 3

# import sys
# sys.setrecursionlimit(6000)
#
# def F(n):
#     if n <= 6:
#         return n
#     if n > 6:
#         return 2*n + 3 + F(n-1)
# print(F(6188) - F(6185))

# ДЗ 2

# import sys
# sys.setrecursionlimit(3000)
#
# def F(n):
#     if n < 3:
#         return 2**1024
#     if n > 2:
#         return 2 * n + 3 + F(n-2)
# print(F(4048) - F(16))

# ДЗ 1

# import functools
# from functools import lru_cache
#
# @lru_cache()
# def F(n):
#     if n <= 5:
#         return n
#     if n > 5:
#         return 2*n - 8 + F(n-2) + F(n-1) // 8
# print(F(163))