











'''demo'''
# 19-, -2, -5, //3, 20+
# def WIN1(n):
#     return (n - 2) <= 19 or (n - 5) <=19 or (n // 3) <= 19
# def LOSE1(n):
#     return (WIN1(n - 2) and WIN1(n - 5) and WIN1(n // 3)) and not WIN1(n)
# # 19
# for n in range(20, 200):
#     if LOSE1(n):
#         print(19, n)
#         break
# # 20
# def WIN2(n):
#     return (LOSE1(n-2) or LOSE1(n-5) or LOSE1(n // 3)) and not WIN1(n)
# cnt = 0
# for n in range(20,200):
#     if WIN2(n) and cnt < 2:
#         print(20,n)
#         cnt += 1
# # 21
# def LOSE2(n):
#     return (WIN2(n - 2) or WIN1(n - 2)) and (WIN2(n - 5) or WIN1(n - 5)) and (WIN2(n // 3) or WIN1(n // 3)) \
#         and not (WIN1(n - 2) and WIN1(n - 5) and WIN1(n // 3))
# for n in range(20, 200):
#     if LOSE2(n):
#         print(21, n)
#         break
#
# from functools import lru_cache
# import sys
# sys.setrecursionlimit(10000)
# def moves(h):
#     return h - 2, h - 5, h // 3
# @lru_cache()
# def game(h):
#     if h <= 19:
#         return 'W'
#     if any(game(m) == 'W' for m in moves(h)):
#         return 'P1'
#     if all(game(m) == 'P1' for m in moves(h)):
#         return 'B1'
#     if any(game(m) == 'B1' for m in moves(h)):
#         return 'P2'
#     if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
#         return 'B2'
# for n in range(20, 200):
#     if game(n) == 'B1':
#         print(19, n)
#         break
# cnt = 0
# for n in range(20, 200):
#     if game(n) == 'P2' and cnt < 2:
#         print(20, n)
#         cnt += 1
# for n in range(20, 200):
#     if game(n) == 'B2':
#         print(21, n)


'''dosrok'''
# 87-, -2, //2, 88+
# def WIN1(n):
#     return (n - 2) <= 87 or (n // 2) <= 87
# def LOSS1(n):
#     return WIN1(n - 2) and WIN1(n // 2) and not WIN1(n)
# for n in range(88,200):
#     if LOSS1(n):
#         print(19, n)
#         break
# def WIN2(n):
#     return not WIN1(n) and (LOSS1(n - 2) or LOSS1(n // 2))
# cnt = 0
# for n in range(88,200):
#     if WIN2(n) and cnt < 2:
#         print(20, n)
# def LOSS2(n):
#     # return WIN2(n - 2) and WIN1(n // 2)
#     return (WIN2(n-2) and WIN1(n // 2)) or (WIN2(n//2) and WIN1(n - 2))
#
# for n in range(88,200):
#     if LOSS2(n):
#         print(21, n)
#         break
#
# from functools import lru_cache
# import sys
# sys.setrecursionlimit(10000)
# def moves(h):
#     return h - 2, h // 2
# @lru_cache()
# def game(h):
#     if h <= 87:
#         return 'W'
#     if any(game(m) == 'W' for m in moves(h)):
#         return 'P1'
#     if all(game(m) == 'P1' for m in moves(h)):
#         return 'B1'
#     if any(game(m) == 'B1' for m in moves(h)):
#         return 'P2'
#     if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
#         return 'B2'
# for n in range(20, 200):
#     if game(n) == 'B1':
#         print(19, n)
#         break
# cnt = 0
# for n in range(20, 200):
#     if game(n) == 'P2' and cnt < 2:
#         print(20, n)
#         cnt += 1
# for n in range(20, 200):
#     if game(n) == 'B2':
#         print(21, n)
#         break

'''E8AF52'''
# +1, *2, >=81, (7, 1<=S<=73)
# def WIN1(n,s):
#     return n + 1 + s >= 81 or n * 2 + s >= 81 or s * 2 + n >= 81
# def False_Lose(n,s):
#     return WIN1(n+1,s) or WIN1(n*2,s) or WIN1(n,s+1) or WIN1(n,s*2)
# for s in range(1,74):
#     if False_Lose(7,s):
#         print(19,s)
#         break
# def LOSS1(n,s):
#     return WIN1(n + 1, s) and WIN1(n * 2, s) and WIN1(n, s + 1) and WIN1(n, s * 2) and not WIN1(n,s)
# def WIN2(n, s):
#     return LOSS1(n + 1, s) or LOSS1(n * 2, s) or LOSS1(n, s + 1) or LOSS1(n, s * 2)
# cnt = 0
# for s in range(1,74):
#     if WIN2(7,s) and cnt < 2:
#         print(20, s)
#         cnt += 1
# def LOSS2(n,s):
#     return (WIN1(n+1,s) or WIN2(n+1,s)) and (WIN1(n*2,s) or WIN2(n*2,s)) and (WIN1(n,s+1) or WIN2(n,s+1)) and \
#         (WIN1(n,s*2) or WIN2(n,s*2)) and (WIN2(n*2,s) or WIN2(n+1,s) or WIN2(n,s+1) or WIN2(n,s*2))
# for s in range(1,74):
#     if LOSS2(7,s):
#         print(21,s)
#         break

# from functools import lru_cache
# import sys
# sys.setrecursionlimit(10000)
# def moves(h):
#     a, b = h
#     return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)
# @lru_cache()
# def game(h):
#     if sum(h) >= 81:
#         return 'W'
#     if any(game(m) == 'W' for m in moves(h)):
#         return 'P1'
#     if all(game(m) == 'P1' for m in moves(h)):
#         return 'B1'
#     if any(game(m) == 'B1' for m in moves(h)):
#         return 'P2'
#     if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
#         return 'B2'
# for n in range(1, 73):
#     n = (7, n)
#     if game(n) == 'B1':
#         print(19, n)
#         break
# cnt = 0
# for n in range(1, 73):
#     n = (7, n)
#     if game(n) == 'P2' and cnt < 2:
#         print(20, n)
#         cnt += 1
# for n in range(1, 73):
#     n = (7, n)
#     if game(n) == 'B2':
#         print(21, n)
#         break

'''ED5E0C'''
# def WIN1(n,s):
#     return n + 1 + s >= 65 or n * 3 + s >= 65 or s * 3 + n >= 65
# def False_Lose(n,s):
#     return WIN1(n+1,s) or WIN1(n*3,s) or WIN1(n,s+1) or WIN1(n,s*3)
# for s in range(1,58):
#     if False_Lose(6,s):
#         print(19,s)
#         break
# def LOSS1(n,s):
#     return WIN1(n + 1, s) and WIN1(n * 3, s) and WIN1(n, s + 1) and WIN1(n, s * 3) and not WIN1(n,s)
# def WIN2(n, s):
#     return LOSS1(n + 1, s) or LOSS1(n * 3, s) or LOSS1(n, s + 1) or LOSS1(n, s * 3)
# cnt = 0
# for s in range(1,58):
#     if WIN2(6,s) and cnt < 2:
#         print(20, s)
#         cnt += 1
# def LOSS2(n,s):
#     return (WIN1(n+1,s) or WIN2(n+1,s)) and (WIN1(n*3,s) or WIN2(n*3,s)) and (WIN1(n,s+1) or WIN2(n,s+1)) and \
#         (WIN1(n,s*3) or WIN2(n,s*3)) and (WIN2(n*3,s) or WIN2(n+1,s) or WIN2(n,s+1) or WIN2(n,s*3))
# for s in range(1,58):
#     if LOSS2(6,s):
#         print(21,s)
#         break