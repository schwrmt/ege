from itertools import product
'''EGKR190425'''
# n = 1
# for x in product('АБДЕОП',repeat=6):
#     x = ''.join(x)
#     if x[0] == 'О' and n % 2 == 0 and len(set(x)) == 6:
#         print(n,x)
#     n += 1

'''openVar2025'''
# ban = []
# for odd1 in '13579':
#     for odd2 in '13579':
#         ban.append(odd1 + odd2)
# for evan1 in '02468':
#     for evan2 in '02468':
#         ban.append(evan1 + evan2)
# cnt = 0
# for x in product('0123456789', repeat=4):
#     x = ''.join(x)
#     if x[0] == '0':
#         continue
#     have_banned_comb = False
#     for b in ban:
#         if x.count(b) != 0:
#             have_banned_comb = True
#             break
#     if len(set(x)) == 4 and not have_banned_comb:
#         cnt+= 1
# print(cnt)

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
#     for i in range(len(x)-1):
#         if int(x[i]) < int(x[i+1]):
#             break
#     else:
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

'''var8'''
# ban = []
# for x in '1357':
#     ban.append(x + '4')
#     ban.append('4' + x)
# cnt = 0
# for x in product('01234567',repeat=5):
#     x = ''.join(x)
#     if x[0] == '0':
#         continue
#     if x.count('4') == 2:
#         for b in ban:
#             if x.count(b):
#                 break
#         else:
#             cnt += 1
# print(cnt)

'''var7'''
# cnt = 0
# n = 0
# for x in product('АГИЛМНОФ', repeat=5):
#     x = ''.join(x)
#     n += 1
#     if n % 2 != 0 and x[0] != 'Н' and x.count('О') <= 1:
#         cnt += 1
# print(cnt)

'''var5'''
# from itertools import product
# n = 0
# cnt_answ = 0
# for x in product('АВИОРТФ', repeat = 6):
#     n += 1
#     if n % 2 == 0 and x[0] != 'О' and x.count('Р') == 2:
#         cnt_answ += 1
# print(cnt_answ)

'''var4'''
# cnt = 0
# for x in product('123456', repeat=5):
#     x = ''.join(x)
#     cnt_odds = x.count('1') + x.count('3') + x.count('5')
#     cnt_evens = x.count('2') + x.count('4') + x.count('6')
#     if x.count('3') == 1 and (cnt_odds >= cnt_evens):
#         cnt += 1
# print(cnt)

'''var3'''
# cnt = 0
# for x in product('123456', repeat=4):
#     x = ''.join(x)
#     cnt_odds = x.count('1') + x.count('3') + x.count('5')
#     cnt_evens = x.count('2') + x.count('4') + x.count('6')
#     if x.count('3') == 1 and (cnt_odds >= cnt_evens):
#         cnt += 1
# print(cnt)

'''var1'''
# from itertools import product
# ban = []
# for n in '135':
#     ban.append(f'0{n}')
#     ban.append(f'{n}0')
# cnt =0
# for x in product('012345', repeat=6):
#     x = ''.join(x)
#     if x[0] == '0':
#         continue
#
#     if x.count('0') == 1:
#         for b in ban:
#             if x.count(b) != 0:
#                 break
#         else:
#             cnt += 1
# print(cnt)

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
