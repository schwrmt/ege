f = open('var7.txt')
f = [int(x) for x in f]
max_19 = max([x for x in f if str(x)[-2:] == '19'])
cnt = 0
max_sum = -100000
for i in range(len(f)-2):
    troika = (f[i],f[i+1],f[i+2])
    lens = [len(str(x).replace('-','')) for x in troika]
    if lens.count(3) == 1 and sum(troika) > max_19:
        cnt += 1
        max_sum = max(sum(troika), max_sum)
print(cnt,max_sum)

'''ege2023_3'''
# f = open('ege2023_3.txt')
# f = [int(x) for x in f]
# max_el_end_3 = max([x for x in f if str(x)[-2:] == '39' and len(str(x).replace('-','')) == 4])
# cnt = 0
# max_sum = 0
# for i in range(len(f)-1):
#     pair = (f[i], f[i+1])
#     lens = [len(str(x).replace('-','')) for x in pair]
#     sm = sum(pair)
#     if lens.count(4) == 1 and sm**2 <= max_el_end_3 ** 2:
#         cnt += 1
#         if max_sum < sm:
#             max_sum = sm
# print(cnt,max_sum)

'''ege2024_3'''
# f = open('ege2024_3.txt')
# f = [int(x) for x in f]
# max_el_end_3 = max([x for x in f if str(x)[-1] == '3' and len(str(x).replace('-','')) == 3])
# cnt = 0
# max_sum = 0
# for i in range(len(f)-2):
#     troika = (f[i], f[i+1], f[i+2])
#     sm = sum(troika)
#     el_end_on_3_and_len_3 = [t for t in troika if str(t)[-1] == '3' and len(str(t).replace('-','')) == 3]
#     if len(el_end_on_3_and_len_3) > 0 and sm < max_el_end_3:
#         cnt += 1
#         max_sum = max(sm, max_sum)
# print(cnt, max_sum)

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

'''var1'''
# f = open('var1.txt')
# f = [int(x) for x in f]
# mn = min(f)
# cnt = 0
# max_sum = 0
# for i in range(len(f)-1):
#     if f[i] % 27 == mn or f[i+1] % 27 == mn:
#         cnt += 1
#         max_sum = max(max_sum, f[i] + f[i+1])
# print(cnt, max_sum)

'''var2'''
# f = open('var2.txt')
# f = [int(x) for x in f]
# mn = min(f)
# cnt = 0
# min_sum = 1000000000000000
# for i in range(len(f)-1):
#     if f[i] % 30 == mn or f[i+1] % 30 == mn:
#         cnt += 1
#         min_sum = min(min_sum, f[i] + f[i+1])
# print(cnt, min_sum)

'''var3'''
# f = open('var3.txt')
# f = [int(x) for x in f]
# mn = min(f)
# cnt = 0
# min_abs_raznost = 10000000000
# for i in range(len(f)-1):
#     if (f[i] % 44 + f[i+1] % 44) == mn:
#         cnt += 1
#         razn = f[i] - f[i+1]
#         if razn < 0:
#             razn = int(str(razn)[1:])
#             razn = int(razn)
#         min_abs_raznost = min(min_abs_raznost, razn)
# print(cnt, min_abs_raznost)

'''var5'''
# f = open('var5.txt')
# f = [int(x) for x in f]
# min_25 = min([x for x in f if x % 100 == 25])
# cnt = 0
# max_sum = 0
# for i in range(len(f)-2):
#     troika = (f[i], f[i+1], f[i+2])
#     lens = [len(str(t)) for t in troika]
#     if sum(troika) < min_25 and lens.count(2) == 1:
#         cnt += 1
#         max_sum = max(max_sum, sum(troika))
# print(cnt,max_sum)

'''var7'''
# f = open('var7.txt')
# f = [int(x) for x in f]
# max_na_90 = max([x for x in f if x % 100 == 90])
# cnt = 0
# min_sum = 10000000000000000
# for i in range(len(f) - 2):
#     troika = (f[i], f[i+1], f[i+2])
#     lens_tr = [len(str(t).replace('-','')) for t in troika]
#     if sum(troika) > max_na_90 and lens_tr.count(4) >= 1:
#         cnt += 1
#         min_sum = min(min_sum, sum(troika))
# print(cnt,min_sum)

'''var20'''
# f = open('var20.txt')
# f = [int(x) for x in f]
# cnt = 0
# min_proizved = 1000000
# for i in range(len(f)-1):
#     last_number1 = int(str(f[i])[-1]) # abs(f[i]) % 10
#     last_number2 = int(str(f[i+1])[-1])
#     if last_number1 % 2 != 0 and last_number2 % 2 != 0 and last_number2 != last_number1:
#         cnt += 1
#         min_proizved = min(min_proizved, abs(f[i]) * abs(f[i+1]))
# print(cnt,min_proizved)


'''ДЗ 1'''
# f = open('17_1.1.txt')
# f = [int(x) for x in f]
# max_13 = max(x for x in f if x % 100 == 13)
# sums = []
# for i in range(len(f)-2):
#     if ((f[i] % 2 == 0 and f[i+1] % 2 == 0 and f[i+2] % 2 == 0) \
#         or ( 9 < f[i] < 100 or 9 < f[i+1] < 100 or 9 < f[i+2] < 100)) \
#         and (f[i] + f[i+1] + f[i+2]) <= max_13:
#         sums.append(f[i] + f[i+1] + f[i+2])
# print(len(sums), sum(sums) // len(sums))

'''ДЗ 2'''
# f = open('17_1.2.txt')
# f = [int(x) for x in f]
# min_117 = min(x for x in f if x % 117 == 0 and x > 0)
# sums = []
# for i in range(len(f)-2):
#     f1, f2 = f[i],f[i+1]
#     if (f[i] < 0 < f[i + 1] or f[i + 1] < 0 < f[i]) \
#             and (f[i] + f[i+1]) % min_117 == 0:
#         sums.append(f[i]**2 + f[i+1]**2)
# print(len(sums), min(sums))

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