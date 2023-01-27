n, m = map(int, input().split())

tab = [[0 for _ in range(m)] for _ in range(n)]
tab[0] = [str(col+1).ljust(2) for col in range(m)]

index = m
y = 0; x = m - 1; vert = n; hor = m

while index < n * m:
    vert -= 1
    hor -= 1
    for _ in range(vert): #vertical
        y += 1
        index += 1
        tab[y][x] = str(index).ljust(2)
    for _ in range(hor): #horizontal
        x -= 1
        index += 1
        tab[y][x] = str(index).ljust(2)

    if index >= n * m:
        break

    vert -= 1
    hor -= 1
    for _ in range(vert): #vertical2
        y -= 1
        index += 1
        tab[y][x] = str(index).ljust(2)

    for _ in range(hor): #horizontal2
        x += 1
        index += 1
        tab[y][x] = str(index).ljust(2)

for i in range(n):
    print(*tab[i])
