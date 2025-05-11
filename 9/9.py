



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