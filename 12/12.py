# for i in range(121,500):
#     x = '0' + i * '1' + i * '2' + '0'
#     while not ('00' in x):
#         x = x.replace('02', '101',1)
#         x = x.replace('11','2',1)
#         x = x.replace('12','21',1)
#         x = x.replace('010', '00',1)
#     sum_x = sum(map(int,x))
#     isPrime = True
#     for j in range(2, int(sum_x**0.5)):
#         if sum_x % j == 0:
#             isPrime = False
#             break
#     if isPrime:
#         print(i)
#         break



""" №1 """
# a = '3'
# for n in range(1000,1, -1):
#     a = '3' + '5' * n
#     while '355' in a or '25' in a or '555' in a:
#         if '25' in a:
#             a = a.replace('25','5',1)
#         if '355' in a:
#             a = a.replace('355','52',1)
#         if '555' in a:
#             a = a.replace('555','3',1)
#     if sum(map(int, a)) == 27:
#         print(n)
#         break

""" №2 """
# for n in range(3, 10000):
#     a = '5' + '2'* n
#     while '52' in a or '1122' in a or '2222' in a:
#         if '52' in a:
#             a = a.replace('52','11',1)
#         if '2222' in a:
#             a = a.replace('2222','5',1)
#         if '1122' in a:
#             a = a.replace('1122','25',1)
#     if sum(map(int,a)) == 64:
#         print(n)
#         break

""" №5 """
# a_res = [-1] * 1000
# for n in range(342, 1000, 9):
#     a = n * '8'
#     while '888' in a or '44' in a or '5' in a:
#         if '888' in a:
#             a = a.replace('888','4',1)
#         if '44' in a:
#             a = a.replace('44','58', 1)
#         if '5' in a:
#             a = a.replace('5','8', 1)
#     a_res[n] = int(a)
#     # print(n,a) # повторяются одни и те же числа 88 4 48 488
# print(a_res.index(max(a_res)))

# maxX = -1
# n_pri_max_X = -1
# for n in range(342,10000, 9):
#     x = n * '8'
#     while '888' in x or '44' in x or '5' in x:
#         if '888' in x:
#             x = x.replace('888', '4',1)
#         if '44' in x:
#             x = x.replace('44', '58',1)
#         if '5' in x:
#             x = x.replace('5','8',1)
#     x = int(x)
#     if maxX < int(x):
#         maxX = x
#         n_pri_max_X = n
# print(n_pri_max_X)

""" 6 """
# def check_s(s:str):
#     sum_s = sum(map(int,s))
#     res = []
#     while sum_s > 0:
#         res = res + [sum_s % 12]
#         sum_s //= 12
#     return bool(res.count(3))
#
# for n in range(30, 10000):
#     s = '0' + n * '6'
#     while '06' in s or '556' in s or '666' in s:
#         if '06' in s:
#             s = s.replace('06','6',1)
#         if '566' in s:
#             s = s.replace('566','60',1)
#         if '666' in s:
#             s = s.replace('666','5',1)
#     if check_s(s):
#         print(n)
#         break

""" №12 """
# a = 96 * '7' + 24 * '4'
# while '4444' in a or '7777' in a:
#     if '4444' in a:
#         a = a.replace('4444','77',1)
#     else:
#         a = a.replace('7777','44',1)
# print(a)

""" 6A308D """
# maxSum = -1
# for n in range(3,10000):
#     x = '1' + n * '9'
#     while '19' in x or '49' in x or '999' in x:
#         if '19' in x:
#             x = x.replace('19','9',1)
#         if '49' in x:
#             x = x.replace('49','91',1)
#         if '999' in x:
#             x = x.replace('999', '4', 1)
#     sumX = sum(map(int,x))
#     if sumX > maxSum:
#         maxSum = sumX
# print(maxSum)

""" D50F56 """
# a = '>' + 15 * '1' + 20 * '2' + 16 * '3'
# while '>1' in a or '>2' in a or '>3' in a:
#     if '>1' in a:
#         a = a.replace('>1', '22>', 1)
#     if '>2' in a:
#         a = a.replace('>2','2>', 1)
#     if '>3' in a:
#         a = a.replace('>3', '1>', 1)
# print(sum(map(int, a.replace('>', ''))))

""" 53009A """
# a = '1' + 90*'0'
# while '1' in a:
#     if '10' in a:
#         a = a.replace('10','0001',1)
#     else:
#         a = a.replace('1','000',1)
# print(a.count('0'))

""" var15 """
# a = 65*'1'
# while '11111' in a or '15' in a:
#     if '11111' in a:
#         a = a.replace('11111','15',1)
#     else:
#         a = a.replace('15','1')
# print(a)


""" Demo """
# a = 81 * '1'
# while '11111' in a or '888' in a:
#     if '11111' in a:
#         a = a.replace('11111', '88', 1)
#     else:
#         a = a.replace('888','8')
# print(a)

""" Dosrok """
# for n in range(3,10000):
#     x = '3'+'1'* n
#     while '31' in x or '211' in x or '1111' in x:
#         if '31' in x:
#             x=x.replace('31','1',1)
#         if '211' in x:
#             x=x.replace('211','13',1)
#         if '1111' in x:
#             x=x.replace('1111','2',1)
#     if sum(int(i) for i in x) == 15:
#         print(n)
#         break

"""ДЗ 2"""
# for n in range(3, 1000):
#     x = '9' + '4' * n
#     while '94' in x or '644' in x or '444' in x:
#         if '94' in x:
#             x = x.replace('94','4',1)
#         if '644' in x:
#             x = x.replace('644','49',1)
#         if '444' in x:
#             x = x.replace('444','6',1)
#     if x.count('4') == n / 18:
#         print(n)
#         break

"""ДЗ 4"""
# maxSum = 0
# for n in range(3, 10000):
#     x = '5' + '7' * n
#     while '57' in x or '877' in x or '777' in x:
#         if '57' in x:
#             x = x.replace('57','7',1)
#         if '877' in x:
#             x = x.replace('877','75',1)
#         if '777' in x:
#             x = x.replace('777', '8', 1)
#     sumX = sum(map(int,x))
#     if  sumX > maxSum:
#         maxSum = sumX
# print(maxSum)