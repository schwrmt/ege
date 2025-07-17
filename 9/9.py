f = open('-')
f = [list(map(int,x.split())) for x in f]
res = []
for s in f:
   s_repeat = []
   s_unique = []
   for x in s:
       if s.count(x) > 1:
           s_repeat.append(x)
       else:
           s_unique.append(x)
   if len(s_repeat) == 3 and len(set(s_repeat)) == 1:
       if s_repeat[0] < min(s_unique) * 2:
           res += s
print(sum(res) / len(res))

'''21592'''
# f = open('21592 .txt')
# f = [list(map(int,x.split())) for x in f]
# number = 0
# max_number = -1
# for s in f:
#     number += 1
#     s_cnt_2 = [x for x in s if s.count(x) == 2]
#     s_unique = [x for x in s if s.count(x) == 1]
#     if len(set(s_cnt_2)) == 3:
#         if (max(s_cnt_2) - min(s_cnt_2)) ** 2 > 2 * sum([y**2 for y in s_unique]):
#             max_number = number
# print(max_number)


'''EGKR190425'''
# f = open('EGKR190425.txt')
# f = [list(map(int,x.split())) for x in f]
# sm = -1
# for s in f:
#     flag = True
#     for i in range(len(s)-1):
#         if s[i] <= s[i+1]:
#             flag = False
#             break
#     if flag:
#         if (max(s)  + min(s))/ 2 > (sum(s) - max(s) - min(s))/ 5:
#             sm = sum(s)
#             break
# print(sm)

'''ege2023_1'''
# f = open('ege2023_3.txt')
# f = [list(map(int,x.split())) for x in f]
# sm = -1
# for s in f:
#     s_repeat = []
#     s_unique = []
#     for x in s:
#         if s.count(x) > 1:
#             s_repeat.append(x)
#         else:
#             s_unique.append(x)
#     if len(s_unique) == 3 and len(set(s_repeat)) == 2:
#         if s_repeat.count(max(s)) == 0:
#             sm = sum(s)
#             break
# print(sm)

'''ege2023_1'''
# f = open('ege2023_1.txt')
# f = [list(map(int,x.split())) for x in f]
# cnt = 0
# for s in f:
#     s_repeat = []
#     s_unique = []
#     for x in s:
#         if s.count(x) > 1:
#             s_repeat.append(x)
#         else:
#             s_unique.append(x)
#     if len(s_unique) == 4: # len(s_unique) == 4 and len(s_repeat) == 3 and len(set(s_repeat)) == 1
#         if (sum(s_unique) / len(s_unique)) <= s_repeat[0]:
#             cnt += 1
# print(cnt)





















'''demo'''
# f = open('demo_2025_9.txt')
# cnt = 0
# for s in f:
#     s = list(map(int,s.split()))
#     s_uniq = []
#     s_repeat = []
#     for i in s:
#         if s.count(i) == 1:
#             s_uniq.append(i)
#         elif not s_repeat.count(i):
#             s_repeat.append(i)
#     if len(s_uniq) == 3 and len(s_repeat) == 1:
#         if (s_repeat[0]* 3 )**2 > sum(s_uniq)**2:
#             cnt += 1
# print(cnt)

'''dosrok'''
# f = open('dosrok.txt')
# cnt = 0
# for s in f:
#     s = list(map(int, s.split()))
#     s_uniq = []
#     s_repeat = []
#     for i in s:
#         if s.count(i) == 1:
#             s_uniq.append(i)
#         else:
#             s_repeat.append(i)
#     if len(s_uniq) == 1 and len(set(s_repeat)) == 2 and s_repeat.count(s_repeat[0]) == 3:
#         if max(s_repeat) > s_uniq[0]:
#             cnt += 1
# print(cnt)

'''var2'''
# f = open('var2.txt')
# cnt = 0
# for s in f:
#     s = list(map(int, s.split()))
#     if len(s) == len(set(s)) and (max(s)) > ((sum(s)) - (max(s))):
#         cnt += 1
# print(cnt)

'''var3'''
# from statistics import median
#
# f = open('var3.txt')
# cnt = 0
# for s in f:
#     s = list(map(int,s.split()))
#     s_set = set(s)
#     if len(s_set) == 3 and median(s_set) > 23:
#         cnt += 1
# print(cnt)

'''var6'''
# f = open('var6.txt')
# cnt = 0
# for s in f:
#     s = list(map(int,s.split()))
#     s_repeat2 = [x for x in s if s.count(x) == 2]
#     if len(set(s_repeat2)) == 3 and s_repeat2.count(min(s)) == 0:
#         cnt += 1
# print(cnt)

'''var9'''
# f = open('var9-12.csv')
# f = [list(map(int, x.split(';'))) for x in f]
# cnt = 0
# for s in f:
#
#     if max(s) * 2 < sum(s) - max(s):
#         if max(s) + min(s) == sum(s) - max(s) - min(s):
#             cnt += 1
#         # flag = False
#         # for i in range(len(s)):
#         #     for j in range(i, len(s)):
#         #         if i == j:
#         #             continue
#         #         if s[i] + s[j] == sum(s) - s[i] - s[j]:
#         #             flag = True
#         #             break
#         # if flag:
#         #     cnt += 1
# print(cnt)



'''№8'''
# f = open('8.txt')
# cnt = 0
# for s in f:
#     s = list(map(int,s.split()))
#     s_uniq = []
#     s_repeat = []
#     for i in s:
#         if s.count(i) == 1:
#             s_uniq.append(i)
#         else:
#             s_repeat.append(i)
#     if len(s_uniq) == 4 and max(s_uniq) + min(s_uniq) <= sum(s_repeat):
#         cnt += 1
# print(cnt)

'''№9'''
# f = open('9.txt')
# cnt = 0
# for s in f:
#     s = list(map(int,s.split()))
#     s_uniq = []
#     s_repeat = []
#     for i in s:
#         if s.count(i) == 1:
#             s_uniq.append(i)
#         else:
#             s_repeat.append(i)
#     if len(s_repeat) != 0 and sum(s_uniq) % 2 != 0:
#         cnt += 1
# print(cnt)

'''№13'''
# f = open('13.txt')
# cnt = 0
# for s in f:
#     s = list(map(int,s.split()))
#     is_have_increasing = False
#     is_have_square = False
#     for i in range(len(s)-2):
#         if s[i] < s[i+1] < s[i+2]:
#             is_have_increasing = True
#             break
#     for i in s:
#         if i != 1 and (i ** 2) in s:
#             is_have_square = True
#             break
#     if is_have_increasing and is_have_square:
#         cnt += 1
# print(cnt)

'''B32E8E'''
# f = open('B32E8E.txt')
# cnt = 0
# for s in f:
#     s = list(map(int, s.split()))
#     if len(s) == len(set(s)) and (max(s)) < ((sum(s)) - (max(s))):
#         cnt += 1
# print(cnt)

'''40F07C'''
# f = open('40F07C.txt')
# cnt = 0
# for s in f:
#     s = list(map(int, s.split()))
#
#     s_uniq = []
#     s_repeat = []
#     for i in s:
#         if s.count(i) == 1:
#             s_uniq.append(i)
#         else:
#             s_repeat += [i]
#
#     if len(s_uniq) == 3 and (s_repeat[0] ** 2) * 3 > sum([s_uniq[0]**2, s_uniq[1]**2, s_uniq[2]**2]):
#         cnt += 1
# print(cnt)