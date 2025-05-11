



















'''sergey 4 send'''
# f = open('sergery4file.txt')
# f = list(map(int,f))
# max_13 = max([x for x in f if str(x)[-2:] == '13'])
# cnt = 0
# max_sum = 0
# for i in range(len(f)-2):
#     t = (f[i], f[i+1], f[i+2])
#     cnt_trehznach = 0
#     for n in t:
#         if len(str(n)) == 3:
#             cnt_trehznach += 1
#     if cnt_trehznach == 2 and sum(t) <= max_13:
#         cnt += 1
#         max_sum = max(max_sum, sum(t))
# print(cnt, max_sum)

''' demo '''
# f = open('demo_2025_17.txt')
# l = [int(s) for s in f]
# m = min(l)
# cnt = 0
# maxSum = 0
# for i in range(len(l) - 1):
#     if l[i] % 16 == m or l[i+1] % 16 == m:
#         cnt += 1
#         if (l[i] + l[i+1]) > maxSum:
#             maxSum = l[i] + l[i+1]
# print(cnt, maxSum)

'''dosrok'''
# f = open('dosrok_2025_17.txt')
# l = [int(s) for s in f]
# negative_sum = 0
# for i in l:
#     if i < 0:
#         negative_sum += i
# max_sum = -10000
# cnt = 0
# for i in range(len(l) - 2):
#     mi = min(l[i], l[i+1], l[i+2])
#     ma = min(l[i], l[i+1], l[i+2])
#     if mi * ma > negative_sum:
#         cnt += 1
#         su = l[i] + l[i + 1] + l[i + 2]
#         if su > max_sum:
#             max_sum = su
# print(cnt, abs(max_sum))

'''E89C8A'''
# f = open('E89C8A.txt')
# l = list(map(int,f))
# min110 = 100000000000
# for s in l:
#     if s > 0 and s % 110 == 0 and s < min110:
#         min110 = s
# cnt = 0
# maxSum = -100000
# for i in range(len(l)-1):
#     if (l[i] + l[i+1]) < min110:
#         cnt += 1
#         if (l[i] + l[i+1]) > maxSum:
#             maxSum = l[i] + l[i+1]
# print(cnt, abs(maxSum))

'''FCE3BE'''
# f=open('FCE3BE.txt')
# l=[int(s) for s in f]
# max_dvuznach=-1
# for i in l:
#     if 9<i<100:
#         if max_dvuznach < i:
#             max_dvuznach = i
# cnt=0
# max_sum=-1
# for i in range(len(l)-1):
#
#     if (9 < l[i] < 100) != (9 < l[i+1] < 100) and (l[i] + l[i + 1]) % max_dvuznach == 0:
#             cnt=cnt+1
#             if max_sum<l[i]+l[i+1]:
#                 max_sum=l[i]+l[i+1]
# print(cnt,max_sum)
# len(str(l[i])) == 2 and len(str(l[i+1])) != 2 \
#             or len(str(l[i+1])) == 2 and len(str(l[i])) != 2: # ровно одно двузначное
# if 9<l[i]<100 and (l[i+1]<=9 or l[i+1]>=100) \
#         or 9<l[i+1]<100 and (l[i]<=9 or l[i]>=100):
#     if (l[i]+l[i+1]) % max_dvuznach==0:
#         cnt = cnt + 1
#         if max_sum < l[i] + l[i + 1]:
#             max_sum = l[i] + l[i + 1]