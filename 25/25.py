'''демовариант'''
def dividers(n):
    dividers = set()
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            dividers.add(x)
            dividers.add(n//x)
    return dividers
cnt = 0
for i in range(800000,10**100):
    div = dividers(i)
    if len(div) == 0:
        continue
    M = min(div) + max(div)
    if str(M)[-1] == '4':
        print(i, M)
        cnt += 1
    if cnt == 5:
        break
