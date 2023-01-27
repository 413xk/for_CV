n, ss = int(input('введите число: ')), int(input('введите систему счисления: ')) #user number
new_number = list()
while n > 1:
    new_number.append(n % ss)
    n = n // ss
if n != 0:
    new_number.append(n)
print(*new_number[::-1], sep = '')