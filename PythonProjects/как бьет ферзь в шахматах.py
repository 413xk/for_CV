x, y = input()
n = 8
field = [['.' for _ in range(n)] for _ in range(n)]
slovarX = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
slovarY = {'8':0, '7':1, '6':2, '5':3, '4':4, '3':5, '2':6, '1':7, '0':8}

for i in range(n):
    for j in range(n):
        if i == slovarY[y] or j == slovarX[x]:
            field[i][j] = '*'
        if abs(slovarX[x] - j) == abs(slovarY[y] - i):
            field[i][j] = '*'

field[slovarY[y]][slovarX[x]] = 'Q'

for row in field:
    print(*row)

