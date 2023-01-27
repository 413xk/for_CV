n, m = [int(_) for _ in input().split()] # размерность матрицы
matrixA = [[int(_) for _ in input().split()] for _ in range(n)]# матрица 1
input() # пробел
m, k = [int(_) for _ in input().split()] # размерность матрицы 2
matrixB = [[int(_) for _ in input().split()] for _ in range(m)] # матрица 2
matrixC = [[0 for _ in range(k)] for _ in range(n)] # финальная матрица

for i in range(n):
    for j in range(k):
        for q in range(m):
            matrixC[i][j] += matrixA[i][q] * matrixB[q][j]

for s in range(n):
    print(*matrixC[s])


