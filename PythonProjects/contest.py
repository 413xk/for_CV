n, m = map(int, input().split())

matrix = [i[::-1] for i in [input() for _ in range(n)]]
print(matrix)


