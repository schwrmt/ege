f = open('26_1.txt')
l = list(map(int,f))
l = l[1:]
l = sorted(l)
minPrice = 0
maxPrice = 0
for i in range(len(l) // 2):
    minPrice += l[i] + l[-i-1] / 2
    maxPrice += l[-i-1] + l[i] / 2
if len(l) % 2 != 0:
    maxPrice += l[len(l) // 2]
    minPrice += l[len(l) // 2]
print(minPrice, maxPrice)
mnPrice = sum(l) - (sum(l[len(l)//2:]) / 2)
mxPrice = sum(l) - sum(l[:len(l)//2]) / 2
print(mnPrice, mxPrice)