














'''15 variant'''
# B = list(range(14,20+1))
# C = list(range(15,27+1))
# A = list(range(14,27+1))
# for x in range(1000):
#     if not ((not (x in A)) <= ((x in B) == (x in C))):
#         print(x)

# 12 variant
# def Triangle(n, m, k):
#     return max((n, m, k)) < sum((n,m,k)) - max((n, m, k))
# for A in range(10000, 0, -1):
#     if all( not((Triangle(x, 12, 20) == (not(max(x, 5) > 28))) and Triangle(x, A, 3)) for x in range(1,1000)):
#         print(A)
#         break

'''var3'''
# B = list(range(200,300+1))
# for A in range(1,1000):
#     for x in range(1,10000):
#         f = (x % A == 0) or ((x in B) <= (not (x % 77 == 0)))
#         if not f:
#             break
#     else:
#         print(A)

'''var4'''
# B = list(range(200,250+1))
# for A in range(1000,0,-1):
#     for x in range(1,10000):
#         f = (x % A == 0) or ((x in B) <= (not (x % 55 == 0)))
#         if f == False:
#             break
#     else:
#         print(A)
#         break

'''var5'''
# for A in range(0,1000):
#     flag_A_norm = True
#     for x in range(0,1000):
#         for y in range(0,1000):
#             F = (4 * x + y < A) or (x < y) or (22 <= x)
#             if F == 0:
#                 flag_A_norm = False
#                 break
#         if flag_A_norm == False:
#             break
#     if flag_A_norm:
#         print(A)
#         break

'''var6'''
# for A in range(0,1000):
#     for x in range(1000):
#         for y in range(1000):
#             f = (x**2 + y**2 > 128) or (y < -x + A)
#             if not f:
#                 break
#         else:
#             continue
#         break
#     else:
#         print(A)
#         break

'''12var'''
# def Triangle(n,m,k):
#     return max(n,m,k) < sum([n,m,k]) - max(n,m,k)
# for A in range(1000,1,-1):
#     for x in range(1,1000):
#         F = not((Triangle(x,12,20) == (not(max(x,5) > 28))) and Triangle(x,A,3))
#         if not F:
#             break
#     else:
#         print(A)
#         break


# def Del(n, m):
#     return n % m == 0
# B = list(range(45,90+1))
# count = 0
# for A in range(1,1000):
#     for x in range(1,1000):
#         F = ( Del(x,52) and not (not (x in B) or Del(x,A)) )
#         if F:
#             break
#     else:
#         count += 1
#
# print(count)
#
# def Del(n,m):
#     return n%m==0
# B= list (range(45,90+1))
# for a in range (1,1000):
#     if not any ((Del(x,52) and not(not(x in B) or Del(x,a))) for x in range (10000)):
#         print (a)

# ДЗ 1.2.7
# P = list(range(25,55+1))
# Q = list(range(13,30+1))
# A = list(range(31,55+1))
# for x in range(1,1000):
#     F = (not ((x in P) <= ((x % 14 == 0) or (x in Q))) and (x not in A))
#     if F:
#         print(x)


# ДЗ 1.2.4
# D = list(range(17,58+1))
# C = list(range(29,80+1))
# A = list()
# for x in range(1000):
#     if not ((x in D) <= (((not (x in C)) and (not (x  in A))) <= (not ( x in D)))):
#         print(x)

# ДЗ 1.2.2
# P = list(range(20,67+1))
# Q = list(range(33,98+1))
# A = list()
# for x in range(1000):
#     if not ((x in P) <= (((x in Q) and (not (x in A))) <= (not (x in P)))):
#         print(x)

# ДЗ 1.2.1
# B = list(range(15,40+1))
# C = list(range(21,63+1))
# A = list()
# for x in range(1000):
#     if not ((not (x in B)) <= (((x in C) and (not (x in A))) <= (x in B))):
#         print(x)

# ДЗ 1.1.5
# def Del(n,m):
#     return n % m == 0
# for A in range(1,1000):
#     for x in range(1,1000):
#         if not ((A + x < 123) <= (Del(x,5) <= (not Del(x,7)))):
#             break
#     else:
#         print(A)
#         break

#ДЗ 1.1.4
# def Triangle(a, b, c):
#     return  a < b + c and b < a + c and c < a + b
#
# def Max(a,b):
#     if a > b:
#         return a
#     return b
# #если A < x + 5, то получим неправильный ответ)
# for A in range(1,5000):
#     for x in range(1, 4994):
#         if not ( not ((Triangle(x, 11, 18) == (not (Max(x, 5) > 68))) and Triangle(x, A, 5))) :
#             break
#     else:
#         print(A)

#ДЗ 1.1.3
# def Del(n,m):
#     return n % m == 0
# B = list(range(120,131))
# for A in range(1,1000):
#     for x in range(1, 1000):
#         if not (((x in B) <= (not Del(x, 7)) or (A > 2*x))):
#             break
#     else:
#         print(A)
#         break


#ДЗ 1.1.2
# def Mod(m,n):
#     return m % n
# for A in range(1,1000):
#     for x in range(1,1000):
#         if not ((A + x > 700 - A) and (Mod(A,100) + Mod(100,x) > 50)):
#             break
#     else:
#         print(A)
#         break


#ДЗ 1.1.1
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if not ((x**2 + y**2 > 1024 - x) or (y < -2 * x + A)):
#                 break
#         if not ((x ** 2 + y ** 2 > 1024 - x) or (y < -2 * x + A)):
#             break
#     else:
#         print(A)

# 3.5
# def Del(n,m):
#     return n % m == 0
# for A in range(1,1000):
#     if all(((Del(x, A) and Del(x,42)) <= (Del(x,8) and Del(x,150)) ) for x in range(10000)):
#         print(A)
#         break

# 3.4
# def Del(n, m):
#      return not bool(n % m)
# B = list(range(45,90+1))
# for A in range(1,1000):
#     for x in range(1,1000):
#         if Del(x, 52) and (not (not (x in B) or Del(x, A))):
#             break
#     else:
#         print(A)

# 3.3
# B = list(range(100,120+1))
# cnt = 0
# for A in range(1,1000):
#     if all( ( (x in B) <= (( (x % 35 == 0) == (x % A == 0)) or (x % A == 0)) ) for x in range(1,1000)):
#         cnt += 1
#         print(A)
# print(cnt)

# 3.2
# P = list(range(25,120))
# Q = list(range(54,75+1))
# A = list()
# for x in range(1000):
#     F = ( (x in Q) <= (((x in P) == (x in Q)) or ((not (x in P)) <= (x in A))))
#     if not F:
#         A.append(x)
# print(A)

# 3.1
# P = list(range(13,37+1))
# Q = list(range(22,51+1))
# A = list(range(37,51+1))
# x_true = list()
# for x in range(1000):
#     F = ( not ((x in Q) <= ((x % 18 == 0) or (x in P))) and (x not in A) )
#     if F:
#         x_true.append(x)
# print(x_true)

# 2.15
# for A in range(-100,1000):
#     if A == 0: continue
#     if all( (((x + 40 < A) or (x + A < 40)) <= (x % A == 0)) for x in range(1, 1000) ):
#             print(A)

# 2.11
# for A in range(1, 1000):
#     if all( (2*y + x != 17) or (A > 7 * x) and (A > 3 * y) for x in range(1, 1000) for y in range(1,1000) ):
#         print(A)
#         break

# 2.10
# for A in range(1, 1000):
#     if all( (x & 60 != 0) or (x & 47 == 0) or (x & A !=0 ) for x in range(1, 1000) ):
#         print(A)
#         break

# 2.9
# for A in range(1, 1000):
#     if all( ((x & 41 != 0) and (x & 50 != 0)) <= ((x & A != 0) or (x & 76 != 0)) for x in range(1, 1000) ):
#
#         print(A)
#         break

# 2.8
# for A in range(1, 1000):
#     if all( (x & 23 == 0) <= ((x & 13 != 0) <= (x & A !=0)) for x in range(1,1000)):
#         print(A)
#         break

# 2.7
# for A in range(1, 1000):
#     if all( ((x % A == 0) and (x % 8 == 0)) <= ((x % 8 != 0) or (x % 240 == 0)) for x in range(1,10000)):
#         print(A)
#         break

# 2.2
# for A in range(1,1000):
#     for B in range(1,1000):
#         flag = True
#         for x in range(1,1000):
#             for y in range(1,1000):
#                 if not ( (( y <= 2 * x ** 2 - 12 * x + A - 2 ) or (y <= -4*x + B)) == (y <= ((x - 4)**2 + abs((x - 2) ** 2 - 16)))):
#                     flag = False
#                     break
#             if not flag:
#                 break
#         if flag:
#             print(abs(A-B))

# 2.1
# cnt = 0
# for R in range(1, 1000):
#     if all( (x & 54 != 0) and (x & 45 != 0) or (x & A == 0) or (x & R == 0) \
#             for x in range(1, 1000) for A in range(1, 1000)):
#         cnt += 1
#         print(bin(R)[2:])
# print(f'Количество: {cnt}')
# ИЛИ
# for x in range(1, 1000):
#     if not ((x & 54 != 0) and (x & 45 != 0)):
#         print(bin(x))
# for R in range(1,1000):
#     flag = 1
#     for A in range(1,1000):
#         for x in range(1,1000):
#             if not ((x & 54 != 0) and (x & 45 != 0) or (x & A == 0) or (x & R == 0)):
#                 flag = 0
#                 break
#     if flag:
#         print(R)

# 1.9
# P = list(range(27, 130 + 1))
# Q = list(range(50, 62 + 1))
# R = list(range(38, 94 + 1))
# A = list()
# for x in range(1, 150):
#     if not (((x not in P) or (x in Q)) or ((x not in A) <= ( x not in R))):
#         A.append(x)
# print(A[-1]-A[0])

#1.8
# def Del(n, m):
#      return not bool(n % m)
# for A in range(1,1000):
#     for x in range(1,1000):
#         if not (Del(A,256) and not(Del(A,2) <= (Del(A,x) and not Del(A,2)))):
#             break
#     else:
#         print(A)
#         break

#1.7
# for A in range(1, 1000):
#     flag = True
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if not ((y + 3*x < A) or (2*y + x > 50) or (4*y - x < 40)):
#                 flag = False
#                 break
#         if not flag:
#             break
#     if flag:
#         print(A)
#         break
# # ИЛИ
# for A in range(1,100):
#     if all(((y + 3*x < A) or (2*y + x > 50) or (4*y - x < 40)) for x in range(1,1000) for y in range(1,1000)):
#         print(A)
#         break

#1.6
# for A in range(1, 100):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             f = (x >= 13) or (x < 4 * y) or (x * y < A)
#             if f == 0:
#                 break
#         if f == 0:
#             break
#     else:
#         print(A)
#         break

# 1.3
# def Del(n,m):
#     return n % m == 0
#
# for A in range(1,1000):
#     for x in range(1,1000):
#         F = Del(x, A) <= (Del(x,21) or Del(x,35))
#         if not F: # Если F == False, то дальше нет смысла перебирать X, А не выполнил свою функцию - меняем
#             break
#     else: # если в цикле x не был вызван break
#         print(A)
#         break # Нужно только наименьшее = первое подходящее

# 1.1
# def Del(n, m):
#     return n % m == 0
#
# for A in range(1, 100):
#     flag = True
#     for x in range(1, 1000):
#         if not ((Del(x, A) and (not Del(x, 36))) <= (not Del(x, 12))):
#             flag = False
#             break
#     if flag:
#         print(A)
#         break

# def Del(n, m):
#     return not bool(n % m)
#
# for A in range(1, 100):
#     flag = True
#     for x in range(1, 1000):
#         if not (Del(x, A) <= (not Del(x,42) or Del(x,56))):
#             flag = False
#             break
#     if flag:
#         print(A)
# for R in range(1,1000):
#     for A in range(1,1000):
#         for x in range(1,1000):
#             f = (x & 54 != 0) and (x & 45 != 0) or (x & A == 0) or (x & R == 0)
#             if not f: break
#         if not f: break
#     else:
#         print(R)

# def Del(n, m):
#     return n % m == 0
# B = list(range(45,90+1))
# count = 0
# for A in range(1,1000):
#     for x in range(1,1000):
#         F = ( Del(x,52) and not (not (x in B) or Del(x,A)) )
#         if F:
#             break
#     else:
#         count += 1
#
# print(count)

'''var2'''
# def Del(n,m):
#     return n % m == 0
# for A in range(1,1000):
#     for x in range(1,1000):
#         f = (Del(x,14) <= (not Del(x,4))) or (x + A >= 200)
#         if not f:
#             break
#     else:
#         print(A)
#         break
