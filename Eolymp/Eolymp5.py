mass = input().split()

n = int(mass[0])
m = int(mass[1])
k = int(mass[2])
t = m + 1
str = ''


for x in range(n):
    if mass[-k:] == ''