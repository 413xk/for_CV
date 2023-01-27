n = int(input())
pascal = []
for i in range(n+1):
    row = [1] * (i + 1)
    for j in range(i+1):
        if j == 0 or j == i:
            row[0] == 1
            row[j] == 1
        else:
            row[j] = pascal[i-1][j-1] + pascal[i-1][j]

    pascal.append(row)
#print(row)
for k in range(n):
    print(*pascal[k])


