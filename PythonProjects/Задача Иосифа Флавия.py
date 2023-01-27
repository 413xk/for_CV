'''n = int(input()) #количество человек
k = int(input()) #К-ый человек умирает
squad = []
survive = []

[squad.append(i) for i in range(1, n+1)] #создаем отряд от 1 до n
for j in range(1, len(squad), k):
    survive.append(j)
squad = survive
survive = []
print(squad)'''

n = int(input()) #количество человек
k = int(input()) #К-ый человек умирает
j = 0

for i in range(1, n+1):
    j = (j+k)%i
print(j+1)


