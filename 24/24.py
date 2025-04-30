f = open('demo_2025_24.txt')
s = f.readline()
s = s.replace('*', '-')
s = s.split('-')
max_cnt = 0
cnt = 0
for i in range(len(s)-1):
    j = s[i]
    if len(j) > 0 and j[0] != '0':
        cnt += len(j) + 1
    elif len(j) == 0 or j[0] == '0':
        cnt = 0
    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)