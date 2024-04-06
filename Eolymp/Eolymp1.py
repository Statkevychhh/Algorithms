n = int(input())
c = 0
mass = []
mass1 = []

while c < n:
    c1 = 0
  
    mass0 = []
    massive = input().split()
    y = 0   
    for r in massive:
        massive[y] = int(r)
        y += 1
    n1 = massive[0]
    massive = massive[1:].copy()
    mass.append(n1)
    while c1 < n1:
        num = massive[c1]
        mass0.append(num)
        mass1.append(num)
        c1 += 1
      
    #print(mass0)
    mass[c] = mass0
    c += 1
#print(mass)
# print(mass1)

mass2 = [[98], [6, 9], [8, 4, 8], [15, 2022]]
mass3 = [[98], [6, 9], [8, 4, 8], [15, 2022]]

for x in mass1:
    mass2 = mass1.copy()
    mass2.remove(x)
    for y in mass1:
        mass3 = mass2.copy()
        mass3.remove(y)
        for z in mass1:
            if x + y > z and x+z > y and z+y>x:
                print(x,y,z)
print(-1)