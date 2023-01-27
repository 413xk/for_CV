n, m = map(int, input().split())

matrix = [[_ for _ in range(m)] for _ in range(n)]

nm = 0
for i in range(n*m):
    for j in range(n):
        for k in range(m):
            if k + j == i:
                nm += 1
                matrix[j][k] = str(nm).ljust(2)

for r in range(n):
    print(*matrix[r])