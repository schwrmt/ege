import string
'''A9D03C'''
f = open('A9D03C.txt').readline()
f = f.replace('B', 'A')
f = f.replace('C', 'A')
max_len = 0
for i in range(len(f)):
    for j in range(i + max_len, len(f)):
        s = f[i:j+1]
        if 'AA' not in s:

            max_len = max(len(s), max_len)
        else:
            break
print(max_len)

'''E74424'''
# f = open('E74424.txt').readline()
# f=f.replace('Q','A')
# f=f.replace('R','A')
# f=f.replace('W','A')
# f=f.replace('2','1')
# f=f.replace('4','1')
# f=f.replace('AA','A A')
# f=f.replace ('11', '1 1')
# f=f.replace('AA','A A')
# f=f.replace ('11', '1 1')
# f=f.split()
# print(len(max(f, key=len)))



'''A520F8'''
# f = open('A520F8.txt').read().strip()
# f = f.replace('BD', 'B D')
# f = f.replace('DB', 'D B')
# f = f.replace('BD', 'B D')
# f = f.replace('DB', 'D B')
# f = f.split() # разбиение на список по пробелу
# print(len(max(f, key = len)))