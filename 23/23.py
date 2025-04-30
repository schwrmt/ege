import math

import math
import sys
sys.setrecursionlimit(5000)

def F(n):
    if n >= 5000:
        return math.factorial(n)
    if 1 <= n < 5000:
        return F(n + 1) // (n + 1)
print(F(12) / F(4))






# ДЗ 6
# def F(n,m):
#     if n < m:
#         return 0
#     if n == m:
#         return 1
#     return F(n-3,m) + F(n//2, m)
# print(F(28,3))

# ДЗ 5
# def F(n, m):
#     if n < m:
#         return 0
#     if n == m:
#         return 1
#     return F(n-3,m) + F(n-1,m) + F(n//2, m)
# print(F(39,19)*F(19,16)*F(16,7))

# ДЗ 4
# def F(n,m):
#     if n > m:
#         return 0
#     if n == m:
#         return 1
#     return F(n+4,m) + F(n*2,m)
# print(F(13,42))

# ДЗ 3
# def F(n,m):
#     if n > m:
#         return 0
#     if n == m:
#         return 1
#     return F(n+1,m) + F(n+3,m) + F(n*3,m)
# print(F(3,9)*F(9,27)*F(27,31))

# ДЗ 2
# def F(n,m):
#     if n < m or n == 20:
#         return 0
#     if n == m:
#         return 1
#     if n > m:
#         return F(n-2, m) + F(n-3,m) + F(n//5,m)
# print(F(41,10)*F(10,5))

# ДЗ 1
# def F(start, end):
#     if start > end or start == 11 or start == 12:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return F(start+1,end) + F(start*2,end) + F(start**2,end)
# print(F(2,10) * F(10,40))



# 19
# def F(n,m):
#     if n > m:
#         return 0
#     if n == m:
#         return 1
#     return F(n+1,m) + F(int('1' + bin(n)[2:], 2),m)
# print(F(1, int('1111011',2)))

# 18
# def F(n,m):
#     if n > m:
#         return 0
#     if n == m:
#         return 1
#     return F(n+1,m) + F(int(str(n) + '1'), m)
# print(F(1,875))

# 17
# def F(n,m):
#     if n > m:
#         return 0
#     if n == m:
#         return 1
#     return F(n+1,m) + F(n*2,m) + F(n*2+1,m)
# print(F(2,16))

# 13
# def F(start, end):
#     if start == end:
#         return 1
#     if start > end or start == 26:
#         return 0
#     return F(start+2,end) + F(start*2, end)
# print(F(2,14)*F(14,56))

# 9
# a = не более 6 *2, b = не менее 3 *3, c = ровно 3 +36
# def F(start, end, a, b, c):
#     if start > end or  (start == end and a > 6) or (start == end and b < 3) or (start == end and c != 3):
#         return 0
#     if start == end:
#         return 1
#
#     return F(start * 2, end, a + 1, b, c) + F(start * 3, end, a, b + 1, c) + F(start + 36, end, a, b, c + 1)
# print(F(1, 2790, 0, 0, 0))

# 8
# def convert_to9(n):
#     res = ''
#     while n > 0:
#         res += str(n % 9)
#         n //= 9
#     return int(res[::-1])
# def F(n,m):
#     if n < m:
#         return 0
#     if n == m:
#         return 1
#     return F(n-1,m) + F(n-3,m) + F(convert_to9(n//3),m)
# print(F(52, 16))

# 6
# n = start, m = end
# def F(n,m):
#      if n > m:
#          return 0
#      if n == m:
#          return 1
#      return F(n+5, m) + F(n*2, m)
# print(F(1,12)*F(12,24))

#3
# def F(n, m, k, j):
#     if n > m or k > 3 or j > 3:
#         return 0
#     if n == m:
#         return 1
#     return F(n + 1, m, k + 1, 0) + F(n * 3, m, 0, j + 1)
# print(F(1,30, 0, 0))
# def F(n, m, k):
#     if n > m or k.count('++++') or k.count('****'):
#         return 0
#     if n == m:
#         return 1
#     return F(n + 1, m, k + '+') + F(n * 3, m, k + '*')
# print(F(1,30,''))
#
# def f(c,e,s):
#     if c==e and '++++' not in s and '****' not in s: return 1
#     if c<e: return f(c+1,e,s + '+')+f(c*3,e,s + '*')
#     else: return 0
# print(f(1,30,''))


#2
# def F(n, m, k):
#     if n > m or (n == m and k != 2):
#         return 0
#     if n == m:
#         return 1
#     return F(n+2,m, k) + F(n+3,m, k) + F(n*2, m, k+1) + F(n*3,m, k+1)
# print(F(1,51, 0))

# 1
# def F(n,m):
#     if n < m:
#         return 0
#     if n == m:
#         return 1
#     else:
#         return F(n-1,m) + F(n//2,m) + F(n // 3, m)
# print(F(131, 41) * F(41,3))

# demo
# def F(start, end):
#     if start == end:
#         return 1
#     if start < end:
#         return 0
#     return F(start-2, end) + F(start//2, end)
# print(F(38,16)*F(16,2))