f = open('896732.txt').read().strip()
f = f.replace('XZZY','XZZ ZZY')
f = f.split()
print(len(max(f, key=len)))

f = open('896732.txt').read().strip()
m = 0
for i in range(len(f)):
    for j in range(i + m, len(f)):
        s = f[i:j+1]
        if 'XZZY' not in s:
            m = max(m, len(s))
        else:
            break
print(m)








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
# долгий способ
# f = open('7E659E.txt').read().strip()
# f = f.replace('X', ' ')
# f = f.split(' ') # Важно именно пробел
# max_len = 0
# for i in range(len(f) - 140):
#     s = 'X'.join(f[i: i + 141])
#     max_len = max(len(s), max_len)
# print(max_len)

'''F04010'''
# f = open('F04010.txt').read().strip()
# f = f.replace('Y', ' ')
# f = f.split(' ') # Важно именно пробел
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