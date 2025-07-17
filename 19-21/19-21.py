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
#     return not WIN1(n) and not LOSS1(n) and not WIN2(n) and (WIN1(n-2) or WIN2(n-2)) and (WIN1(n//2) or WIN2(n//2))
#
# for n in range(88,200):
#     if LOSS2(n):
#         print(21, n)
#         break



'''20var'''
# +2 *2 >=122 (3, 1<=s<=117)
# def WIN1(n,s):
#     return (n + 2 + s >= 122 or n * 2 + s >= 122 or n + s * 2 >= 122) and  n + s < 122
# def FAKE_LOSE1(n,s):
#     return WIN1(n+2,s) or WIN1(n,s+2) or WIN1(n*2, s) or WIN1(n,s*2)
# for s in range(1,117+1):
#     if FAKE_LOSE1(3,s):
#         print(19,s)
#         break
# def LOSE1(n,s):
#     return not WIN1(n,s) and WIN1(n+2,s) and WIN1(n,s+2) and WIN1(n*2, s) and WIN1(n,s*2)
# def WIN2(n,s):
#     return not WIN1(n,s) and (LOSE1(n+2,s) or LOSE1(n,s+2) or LOSE1(n*2, s) or LOSE1(n,s*2))
# for s in range(1,117+1):
#     if WIN2(3,s):
#         print(20,s)
# def LOSE2(n,s):
#     return not LOSE1(n,s) and not WIN1(n,s) and not WIN2(n,s) and (WIN1(n+2,s) or WIN2(n+2,s)) and (WIN1(n*2,s) or WIN2(n*2,s)) \
# and (WIN1(n,s+2) or WIN2(n,s+2)) and (WIN1(n,s*2) or WIN2(n,s*2))
# for s in range(1,117+1):
#     if LOSE2(3,s):
#         print(21,s)
#         break

''''ege24_1'''
# def WIN1(n,s):
#     return (n + 1 + s >= 65 or n * 3 + s >= 65 or n + 3 * s >= 65) and n + s < 65
# def FAKE_LOSE1(n,s):
#     return WIN1(n+1, s) or WIN1(n, s+1) or WIN1(n, s*3) or WIN1(n*3, s)
# for s in range(1,58+1):
#     if FAKE_LOSE1(6,s):
#         print(19, s)
#         break
# def LOSE1(n,s):
#     return not WIN1(n,s) and WIN1(n+1,s) and WIN1(n,s+1) and WIN1(n*3,s) and WIN1(n,s*3)
# def WIN2(n,s):
#     return not WIN1(n,s) and (LOSE1(n+1,s) or LOSE1(n,s+1) or LOSE1(n*3,s) or LOSE1(n,s*3))
# for s in range(1,58+1):
#     if WIN2(6,s):
#         print(20, s)
# def LOSE2(n,s):
#     return not LOSE1(n,s) and not WIN1(n,s) and not WIN2(n,s) and (WIN2(n+1,s) or WIN1(n+1,s)) and (WIN2(n,s+1) or WIN1(n,s+1)) \
#         and (WIN2(n*3,s) or WIN1(n*3,s)) and (WIN2(n,s*3) or WIN1(n,s*3))
# for s in range(1,58+1):
#     if LOSE2(6,s):
#         print(21, s)

'''var4'''
# # -3, -4, -7
# def WIN1(n):
#     return (n - 3 <= 34 or n - 7 <= 34 or n // 4 <= 34) and n > 34
# def LOSE1(n):
#     return not WIN1(n) and WIN1(n-3) and WIN1(n-7) and WIN1(n//4)
# for n in range(35, 1000):
#     if LOSE1(n):
#         print(19, n)
# def WIN2(n):
#     return not WIN1(n) and (LOSE1(n-3) or LOSE1(n-7) or LOSE1(n//4))
# for n in range(35,1000):
#     if WIN2(n):
#         print(20,n)
# def LOSE2(n):
#     return not WIN1(n) and not WIN2(n) and not LOSE1(n) and (WIN2(n-3) or WIN1(n-1)) and (WIN2(n-7) or WIN1(n-7)) and (WIN2(n//4) or WIN1(n//4))
# for n in range(35,1000):
#     if LOSE2(n):
#         print(21,n)

# def win1(s):
#  return s - 2 <= 87 or  s // 2 <= 87
# def lose1(s):
#     return win1(s-2) and win1(s//2) and not win1(s)
# for i in range(89,300):
#     if lose1(i):
#         print(19,i)
# #19b
# def false_lose1(s):
#     return win1(s-2) or win1(s//2)
# for i in range(500,88,-1):
#     if false_lose1(i):
#         print(i)
#         break
# ##20
# def win2(s):
#     return (lose1(s-2) or lose1(s//2)) and not win1(s)
# for i in range(89,1000):
#     if win2(i):
#         print(20,i)
# ##21
# def lose2(s):
#     return (win1(s-2) or win2(s-2)) and (win1(s//2) or win2(s//2)) and not win1(s) and not lose1(s)
# for i in range(89,1000):
#     if lose2(i):
#         print(21,i)










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