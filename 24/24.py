#
#
# f = open('new_24').read().strip()
# max_len = 0
# s1 = ''
# for i in range(len(f)):
#     for j in range(i+max_len, len(f)):
#         s = f[i:j+1]
#         if s[0] != '2' or s.count('2025') > 60 :
#             break
#         if len(s) == 4 and s[:4] != '2025':
#             break
#         if s.count('Y') >= 120 and s.count('2025') == 60:
#             if len(s) > max_len:
#                 max_len = max(max_len, len(s))
#                 s1 = s
# print(max_len, s1)

#for min
f = open('new_24').read().strip()
f = f.split('2025')
min_len = 100000000000
s_min = ''
for i in range(1, len(f)-59):
    s = f[i:i+59]
    s = '2025' + '2025'.join(s) + '2025'
    if s.count('Y') < 120:
        continue
    if min_len > len(s):
        min_len = len(s)
        s_min = s
print(min_len, s_min.count('Y'), s_min.count('2025'))
#for max
f = open('new_24').read().strip()
f = f.split('2025')
max_len = 0
s_max = ''
for i in range(1, len(f)-60):
    s = f[i:i+60]
    s = '2025' + '2025'.join(s)
    if s.count('Y') < 120:
        continue
    if max_len < len(s) + 3:
        max_len = len(s) + 3
        s_max = s
print(max_len, s_max.count('Y'), s_max.count('2025'))

# s = open('new_24').readline()
# from re import finditer
# reg = r'2025[A-Z1-9]+'
# reg = rf'(?=({reg}))'
# res = [x.group(1) for x in finditer(reg, s)]
# mx = max(res, key=lambda x: (x.count('2025') == 60 and x.count('Y') >= 120, len(x)))
# print(len(mx), mx.count('2025'))
'''23206'''
# f = open('24_23206.txt').read().strip()
# for d in '02468':
#     f = f.replace(d, '2')
# max_len = 0
# s1 = ''
# for i in range(len(f)):
#     for j in range(i+max_len, len(f)):
#         s = f[i:j+1]
#         if s[0] != '2' or s.count('2') > 1 or s.count('S') > 35:
#             break
#         if s.count('S') == 35:
#             if len(s) > max_len:
#                 max_len = max(max_len, len(s))
#                 s1 = s
# print(max_len)
# OR
# f = open('24_23206.txt').read().strip()
# for d in '02468':
#     f = f.replace(d, '2')
# f = f.split('S')
# max_len = 0
# s1 = ''
# for i in range(len(f)):
#     s = f[i:i+36]
#     s = 'S'.join(s)
#     if s.count('2') > 1 or f[i].count('2') == 0:
#         continue
#     if max_len < len(s) - s.index('2'):
#         max_len = len(s) - s.index('2')
#         s1 = s[s.index('2'):]
# print(max_len, s1)
# OR
# s = open('24_23206.txt').readline()
# from re import *
# for i in '2468':
#     s = s.replace(i, '0')
# reg = r'[02468]([13579A-RT-Z]*S){35}[13579A-RT-Z]*'
# reg = rf'(?=({reg}))'
# res = [x.group(1) for x in finditer(reg, s)]
# mx = max(res, key=lambda x: (x.count('S') == 35, len(x)))
# print(len(mx))

'''dv'''
# f = open('var1.txt').read().strip()
# for d in '0123456789':
#     f = f.replace(d, '1')
# max_len = 0
# for i in range(len(f)):
#     for j in range(i+max_len, len(f)):
#         s = f[i:j+1]
#         if s[0] != 'D' and s.count('D') > 1 and s.count('1') > 70:
#             break
#         if s.count('1') == 70:
#             max_len = max(max_len, len(s))
# print(max_len)

'''var8'''
# f = open('var8.txt').read().strip()
# max_len = 0
# f = f.split('A')
# for i in range(len(f)-700):
#     s = f[i:i+701]
#     s = 'A'.join(s)
#     if s.count('E') == 0:
#         max_len = max(max_len, len(s))
# print(max_len)



'''var1'''
# import re
# f = open('var1.txt').read().strip()
# reg_number = '([1-9][0-9]*|0)'
# reg_arifm = f'{reg_number}([-+]{reg_number})+'
# m = max([x.group() for x in re.finditer(reg_arifm, f)], key=len)
# print(len(m))

# f = open('var1.txt').read().strip()
# f = f.replace('+', '-')
# max_len = 0
# for i in range(len(f)):
#     for j in range(i+max_len, len(f)):
#         s = f[i:j+1]
#         if s[0] == '-':
#             break
#         if s.count('--'):
#             break
#         if s[-1] == '-':
#             continue
#         numbers = s.split('-')
#         for n in numbers:
#             if n[0] == '0' and n != '0':
#                 break
#         else:
#             max_len = max(len(s), max_len)
#             continue
#         break
# print(max_len)

'''var2'''
# f = open('var2.txt').read()
# f = f.replace('+', '-')
# f = f.split('--')
# f = sorted(f, key=len, reverse=True)
# for i in range(10):
#     print(len(f[i]), f[i])
#
# import re
# f = open('var2.txt').read().strip()
# number = r'([1-9][0-9]*|0)'
# reg = fr'{number}([-+]{number})+'
# m = max([x.group() for x in re.finditer(reg, f)], key=len )
# print(len(m), m)
#
# f = open('var2.txt').read()
# f = f.replace('+', '-')
# max_len = 0
# for i in range(len(f)):
#     for j in range(i+max_len, len(f)):
#         s = f[i:j+1]
#         if s[-1] == '-':
#             continue
#         if s[0] == '-' or s.count('--'):
#             break
#         flag_wrong_numbers = False
#         for number in s.split('-'):
#             if number[0] == '0' and number != '0':
#                 flag_wrong_numbers = True
#         if flag_wrong_numbers:
#             break
#         if max_len < len(s):
#             max_len = len(s)
#             print(s)
# print(max_len)

'''var2 if expression should be 0'''
# import re
# f = open('var2.txt').read().strip()
# number = r'([1-9][0-9]*|0)'
# reg = fr'{number}([-+]{number})+'
# reg = f'(?=({reg}))'
# corrects = ([x.group(1) for x in re.finditer(reg, f)])
# corrects = sorted(corrects, reverse=True, key=len)
# print(corrects[:5])
# for c in corrects:
#     if eval(c) == 0:
#         print(len(c), c)
#         break
#
# f = open('var2.txt').read()
# max_len = 0
# for i in range(len(f)):
#     for j in range(i+max_len, len(f)):
#         s = f[i:j+1]
#         if s[-1] == '-' or s[-1] == '+':
#             continue
#         if s[0] == '-' or s[0] == '+' or s.count('--') or s.count('++') or s.count('-+') or s.count('+-'):
#             break
#         flag_wrong_numbers = False
#         for number in s.replace('+','-').split('-'):
#             if number[0] == '0' and number != '0':
#                 flag_wrong_numbers = True
#         if flag_wrong_numbers:
#             break
#         if eval(s) == 0:
#             if max_len < len(s):
#                 max_len = len(s)
# print(max_len)

'''var3'''
# import re
# f = open('var3.txt').read().strip()
# number = r'([1-9][0-9]*|0)'
# reg = fr'{number}([-*]{number})+'
# m = max([x.group() for x in re.finditer(reg, f)], key=len )
# print(len(m), m)
#
# f = open('var3.txt').read()
# f = f.replace('*', '-')
# max_len = 0
# for i in range(len(f)):
#     for j in range(i+max_len, len(f)):
#         s = f[i:j+1]
#         if s[-1] == '-':
#             continue
#         if s[0] == '-' or s.count('--'):
#             break
#         flag_wrong_numbers = False
#         for number in s.split('-'):
#             if number[0] == '0' and number != '0':
#                 flag_wrong_numbers = True
#         if flag_wrong_numbers:
#             break
#         if max_len < len(s):
#             max_len = len(s)
# print(max_len)

'''var5'''
# f = open('var5.txt').read()
# f = f.split('A')
# min_len = 100000000
# for i in range(1, len(f)-2023):
#     s = f[i:i+2023]
#     lens = [len(x) for x in s]
#     if min_len > sum(lens) + 2024:
#         min_len = sum(lens) + 2024
# print(min_len)

'''var6'''
# f = open('var6.txt').read()
# max_len = 0
# f = f.split('A')
# for i in range(len(f)):
#     s = f[i:i+351]
#     lens = [len(x) for x in s]
#     max_len = max(max_len, sum(lens) + 350)
#     # s = 'A'.join(s)
#     # print(s.count('A'))
#     # max_len = max(max_len, len(s))
# print(max_len)

'''demo'''
# import re
# f = open('demo_2025_24.txt').read().strip()
# number = r'([1-9][0-9]*|0)'
# reg = fr'{number}([-*]{number})+'
# m = max([x.group() for x in re.finditer(reg, f)], key=len )
# print(len(m), m)
# # ИЛИ
# f = open('demo_2025_24.txt').read().strip()
# f = f.replace('-', '*')
# f = f.split('**')
# max_len = 0
# for expression in f:
#     for i in range(len(expression)):
#         for j in range(i + max_len, len(expression)):
#             correct_numbers = True
#             s = expression[i:j + 1]
#             if s[0] == '*':
#                 break # Переносим начало дальше
#             for number in s.split('*'):
#                 # Проверка на длину, чтобы не было ошибки при взятии индекса
#                 # Проверяем, что число либо 0, либо не начинается с незнач. 0
#                 if len(number) != 0 and number != '0' and number[0] == '0':
#                     correct_numbers = False
#                     break
#             else:
#                 if s[-1] != "*":
#                     max_len = max(len(s), max_len)
#                     print(s)
#             if not correct_numbers:
#                 break
# print(max_len)

'''dosrok 2025'''
# #Способ-лайфхак
# f = open('dosrok_2025.txt').read()
# for c in string.ascii_uppercase[2:]:
#     f = f.replace(c, ' ')
# f = f.split()
# f = sorted(f, key=len, reverse=True)
# l = []
# for i in f:
#     l.append((i, len(i)))
# for j in range(10):
#     print(l[j])
# # 2 цикла
# f = open('dosrok_2025.txt').read()
# for c in string.ascii_uppercase[2:]:
#     f = f.replace(c, ' ')
# m = 0
# for i in range(len(f)):
#     for j in range(i + m, len(f)):
#         s = f[i:j+1]
#         if s[0] != '0' and  ' ' not in s:
#             if  s[-1] in '02468A':
#                 if m < len(s):
#                     m = len(s)
#         else:
#             break
# print(m)
# # # ИЛИ
# from re import *
# f = open('dosrok_2025.txt').read()
# reg = r'[1-9AB][0-9AB]*[02468A]'
# # reg = rf'(?=({reg}))'
# m = max((x.group() for x in finditer(reg,f)), key = len)
# print(len(m))

'''open2025'''
# #Способ-лайфхак
# f = open('open2025.txt').read()
# for c in string.ascii_uppercase[4:]:
#     f = f.replace(c, ' ')
# f = f.split()
# f = sorted(f, key=len, reverse=True)
# l = []
# for i in f:
#     l.append((i, len(i)))
# for j in range(10):
#     print(l[j])
# # 2 цикла
# f = open('open2025.txt').read()
# for c in string.ascii_uppercase[4:]:
#     f = f.replace(c, ' ')
# m = 0
# for i in range(len(f)):
#     for j in range(i + m, len(f)):
#         s = f[i:j+1]
#         if s[0] != '0' and  ' ' not in s:
#             if  s[-1] in '02468AC':
#                 if m < len(s):
#                     m = len(s)
#         else:
#             break
# print(m)
# # регулярки
# from re import *
# f = open('open2025.txt').read()
# reg = r'[123456789ABCD][0123456789ABCD]*[02468AC]'
# l = findall(reg,f)
# m = max(l, key=len)
# print(len(m),m)

'''A520F8'''
# f = open('A520F8.txt').readline().strip()
# f = f.replace('BD', 'B D')
# f = f.replace('DB', 'D B')
# print(len(max(f.split(), key=len)))
# # или
# f = open('A520F8.txt').read()
# m = 0
# for i in range(len(f)):
#     for j in range(i + m, len(f)):
#         s = f[i:j+1]
#         if 'BD' not in s and 'DB' not in s:
#             m = max(len(s),m)
#         else:
#             break
# print(m)

'''B92F00'''
# f = open('B92F00.txt').readline().strip()
# f = f.replace('AB', 'A B')
# f = f.replace('BA', 'B A')
# print(len(max(f.split(), key=len)))

'''E74424'''
# f = open('E74424.txt').read().strip()
# for c in 'QWR':
#     f = f.replace(c, 'Q')
# for c in '124':
#     f = f.replace(c, '1')
# f = f.replace('11', '1 1')
# f = f.replace('QQ','Q Q')
# f = f.replace('11', '1 1')
# f = f.replace('QQ','Q Q')
# print(len(max(f.split(), key=len)))
# # ИЛИ
# f = open('E74424.txt').read().strip()
# for c in string.ascii_uppercase:
#     f = f.replace(c, 'Q')
# for c in '0123456789':
#     f = f.replace(c, '1')
# m = 0
# for i in range(len(f)):
#     for j in range(i + m, len(f)):
#         s = f[i:j+1]
#         if '11' not in s and 'QQ' not in s:
#             m = max(len(s),m)
#         else:
#             break
# print(m)

'''A9D03C'''
# f = open('A9D03C.txt').read().strip()
# f = f.replace('B','A')
# f = f.replace('C','A')
# f = f.replace('AA', 'A A')
# f = f.replace('AA', 'A A')
#
# print(len(max(f.split(), key=len)))

'''896732'''
# f = open('896732.txt').readline().strip()
# f = f.replace('XZZY', 'XZZ ZZY')
# print(len(max(f.split(), key=len)))
# # или
# f = open('896732.txt').readline().strip()
# max_len = 0
# for i in range(len(f)):
#     for j in range(i + max_len, len(f)):
#         s = f[i:j+1]
#         if 'XZZY' not in s:
#             max_len = max(len(s), max_len)
#         else:
#             break
# print(max_len)

'''BDE963'''
# import re
# f = open('BDE963.txt').readline().strip()
# reg = r'([CDF][AU])+'
# x = (x.group() for x in re.finditer(reg, f))
# print(len(max(x, key=len)) // 2)
# # ИЛИ
# f = open('BDE963.txt').readline().strip()
# for i in 'CDF':
#     for j in 'AU':
#         f = f.replace(i + j, '*')
# for h in 'ACDFU':
#     f = f.replace(h, ' ')
# print(len(max(f.split(), key=len)))

'''907644'''
# import re
# f = open('907644.txt').readline().strip()
# reg = r'([C][AB])+'
# x = (x.group() for x in re.finditer(reg, f))
# print(len(max(x, key=len)) // 2)
# import re
# f = open('907644.txt').readline().strip()
# reg = r'(CA|CB)+'
# x = (x.group() for x in re.finditer(reg, f))
# print(len(max(x, key=len)) // 2)
# # ИЛИ
# f = open('907644.txt').readline().strip()
# f = f.replace('CA', '*')
# f = f.replace('CB', '*')
# for x in 'ABC':
#     f = f.replace(x, ' ')
# print(len(max(f.split(), key=len)))

'''ACDF4D'''
# f = open('ACDF4D.txt').read().strip()
# f = f.replace('T', ' ')
# f = f.split(' ') # Важно именно пробел
# max_len = 0
# for i in range(len(f) - 100):
#     s = 'T'.join(f[i: i + 101])
#     max_len = max(len(s), max_len)
# print(max_len)

'''7E659E'''
# f = open('7E659E.txt').read().strip()
# f = f.replace('X', ' ')
# f = f.split(' ') # Важно именно пробел
# max_len = 0
# for i in range(len(f) - 140):
#     s = 'X'.join(f[i: i + 141])
#     max_len = max(len(s), max_len)
# print(max_len)
#
# f = open('7E659E.txt').readline().strip()
# max_len = 0
# for i in range(len(f)):
#     for j in range(i+max_len, len(f)):
#         s = f[i:j+1]
#         if s.count('X') == 140:
#             max_len = max(max_len, len(s))
#         if s.count('X') > 140:
#             break
# print(max_len)

'''F04010'''
# f = open('F04010.txt').read().strip()
# f = f.replace('Y', ' ')
# f = f.split(' ')
# min_len = 20000
# for i in range(len(f) - 260):
#     s = 'Y'.join(f[i: i + 261])
#     min_len = min(len(s)- len(f[i]) - len(f[i + 260]), min_len)
# print(min_len)

'''3380E0'''
# s = open('3380E0.txt').read().strip()
# s = s.split('AB')
# lens = [len(i) for i in s]
# mx = 0
# for i in range(len(lens) - 100):
#     k = sum(lens[i:i + 101]) + 200 + 2
#     mx = max(mx, k)
# print(mx)
#
# f = open('3380E0.txt').read().strip()
# max_len = 0
# for i in range(len(f)):
#     for j in range(i + max_len, len(f)):
#         s = f[i:j+1]
#         if s.count('AB') == 100:
#             max_len = max(max_len, len(s))
#         elif s.count('AB') > 100:
#             break
# print(max_len)


'''ege2024rezervGrob(=0)'''
# import re
# f = open('EGE2024grob.txt').read().strip()
# number = r'([1-9][0-9]*|0)'
# reg = fr'{number}([+*]{number})+'
# reg = fr'(?=({reg}))'
# m = sorted([x.group(1) for x in re.finditer(reg, f)], key=len, reverse=True )
# for i in m:
#     if eval(i) == 0:
#         print(len(i), i)
#         break
#
# f = open('EGE2024grob.txt').read().strip()
# max_len = 0
# for expression in f:
#     for i in range(len(expression)):
#         for j in range(i + max_len, len(expression)):
#             correct_numbers = True
#             s = expression[i:j + 1]
#             if s[0] == '*' or '**' in s or '+*' in s or '++' in s or '*+':
#                 break
#             for number in s.split('*'):
#                 if len(number) != 0 and number != '0' and number[0] == '0':
#                     correct_numbers = False
#                     break
#             else:
#                 if s[-1] != "*" and eval(s) == 0:
#                     max_len = max(len(s), max_len)
#                     print(s)
#             if not correct_numbers:
#                 break
# print(max_len)