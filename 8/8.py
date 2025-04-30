from itertools import *













'''dosrok'''
# cnt=0
# for x in product ('ДГИАШЭ', repeat=5):
#         x=''.join(x)
#         if x[0] not in 'ИАЭ' and x[-1] not in 'ДГШ':
#             cnt+=1
# print(cnt)

'''demo'''
# cnt=0
# for x in product ('0123456789AB', repeat=5):
#     x=''.join(x)
#     if x[0]!='0' and x.count('7')==1 and (x.count('A')+ x.count('B')+ x.count('9')<=3) :
#         cnt+=1
# print(cnt)

'''var20'''
# cnt = 0
# for x in product('01234',repeat=3):
#     if x[0] == '0':
#         continue
#     if int(x[0]) >= int(x[1]) >= int(x[2]):
#         cnt += 1
# print(cnt)

'''var15'''
# n = 1
# for x in product('АЛМОС', repeat=5):
#     x = ''.join(x)
#     if x.count('А') <= 1 and  x.count('М') == 2 and x.count('Л') == 0:
#         print(n, x)
#         break
#     n += 1

'''E51935'''
# n = 0
# cnt = 0
# for x in product('АПРСУ', repeat=5):
#     x = ''.join(x)
#     n += 1
#     if x.count('У') <= 1 and 'УА' not in x and 'АУ' not in x:
#         print(n, x)

'''39A8D9'''
# n = 0
# cnt = 0
# for x in product("АИНПТЦЯ", repeat=6):
#     x = ''.join(x)
#     n += 1
#     if x.count ('Я') ==2 and  x[0]!= "Н" and   n%2 == 0:
#         cnt += 1
# print(cnt)

''' BA0AE2 '''
# block = []
# for x in '1357':
#     block.append(x + '0')
#     block.append('0' + x)
# cnt = 0
# for i in product('012345678', repeat=5):
#     if i[0] == '0':
#         continue
#     i = ''.join(i)
#     if i.count('0') == 1:
#         # for j in block:
#         #     if j in i:
#         #         break
#         for j in range(1, len(i)):
#             if j + 1 == len(i):
#                 if i[j] == '0' and int(i[j-1]) % 2 != 0:
#                     break
#             elif i[j] == '0' and (int(i[j-1]) % 2 != 0 or int(i[j+1]) % 2 -== 0):
#                 break
#         else:
#             cnt += 1
# print(cnt)

'''17'''
# cnt = 0
# for x in set(permutations('ДИАНА', 5)):
#     x = ''.join(x)
#     if 'АА' not in x:
#         cnt += 1
# print(cnt)

'''№10'''
# cnt=0
# for x in product ('wxyz', repeat=5):
#     x=''.join(x)
#     if 0 < x.count('x')<=3:
#         cnt+=1
# print(cnt)

''' №2 '''
# n = 0
# for i in product(sorted('ИНФОРМТКА'), repeat=6):
#     i = ''.join(i)
#     if i.count('К') > 3:
#         continue
#     n += 1
#     if i.count('А') == 3 and i[0] != 'Ф' and n % 2 != 0:
#         print(i, n)

''' №1 '''
# block = []
# for i in '024':
#     for j in '024':
#         block.append(i + j)
# cnt = 0
# for i in product('01234', repeat=10):
#     if i[0] == '0':
#         continue
#     i = ''.join(i)
#     chet = 0
#     for j in range(len(i)):
#         if int(i[j]) % 2 == 0:
#             chet += 1
#     if chet == 3:
#         for x in block:
#             if x in i:
#                 break
#         else:
#             cnt += 1
# print(cnt)

# ИЛИ

# cnt = 0
# for x in product('01234', repeat=10):
#     if x[0] == '0':
#         continue
#     x = ''.join(x)
#     if x.count('0') + x.count('2') + x.count('4') == 3:
#         for i in range(len(x)-1):
#             if int(x[i]) % 2 ==0 and int(x[i+1]) % 2 == 0:
#                 break
#         else:
#             cnt += 1
# print(cnt)

'''ДЗ 1'''
# cnt = 0
# for x in product('0123456789ABCD', repeat=5):
#     if x[0] != '0' and len(set(x)) == 2 and (x[-1] == '0' or x[-1] == '3'):
#         cnt += 1
# print(cnt)

'''ДЗ 2'''
# cnt = 0
# list1 = list(product('КОНЕЦ', repeat=5))
# list2 = list(product('ДРАКОН', repeat=5))
# for x in list2:
#     if x not in list1:
#         cnt += 1
# for x in list1:
#     if x not in list2:
#         cnt += 1
# print(cnt)

'''ДЗ 3'''
# cnt = 0
# for x in product('КАЙФ', repeat=4):
#     if x[-1] != 'Й' and 'КФ' not in ''.join(x) and len(set(x)) == 4:
#         cnt +=1
# print(cnt)

'''ДЗ 4'''
# cnt = 0
# l = list(permutations('ПРОСТО'))
# l = set(l)
# for x in l:
#     x = ''.join(x)
#     if 'ОО' not in x:
#         cnt += 1
# print(cnt)

'''ДЗ 5'''
# cnt = 0
# l = set(list(permutations('МАКАКА')))
# for x in l:
#     x = ''.join(x)
#     if 'ММ' not in x and 'КК' not in x and 'АА' not in x:
#         cnt += 1
# print(cnt)

'''ДЗ 6'''
# n = 0
# for x in product(sorted(set('КАЛЕЙДОСКОП'), reverse=True), repeat=6):
#     x = ''.join(x)
#     if x[0] == 'К' and x.count('Й') >= 2 and x.count('С') == 0 and x.count('Е') == 0 and n % 2 == 0:
#         print(x, n)
#         break
#     n += 1
