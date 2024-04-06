n = int(input())
c = 0
mass = []
minus = []
null = []

while c < n:
    n1 = int(input())
    c1 = 0
    mass.append(n1)
    mass0 = []
    k = 0
    nul = 0
    mass0 = input().split()
    y = 0
    for r in mass0:
        mass0[y] = int(r)
        y += 1     
    while c1 < n1:
        num = mass0[c1]
        c1 += 1
        if num < 0:
            k += 1
        if num == 0:
            nul += 1
    mass[c] = mass0
    minus.append(k)
    null.append(nul)
    c += 1

o = 0
end = []

for x in mass:
    if minus[o] % 2 == 0 and null[o] == 0:
        print(0)
    elif minus[o] % 2 == 0 and null[o] != 0:
        print(null[o])
    elif minus[o] % 2 == 1 and null[o] == 0:
        for y in x:
            if y >= 0:
                end.append(y)
            else:
                end.append(-y)
        print(min(end)+1)
        end = []
    elif minus[o] % 2 == 1 and null[o] != 0:
        for y in x:
            if y > 0:
                end.append(y)
            elif y < 0:
                end.append(-y)
        print(null[o])
        end = []
    o += 1