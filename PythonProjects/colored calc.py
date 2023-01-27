#всратый калькулятор v2

from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.BLACK, Back.RED, end = '')
what = input('Что делаем? +/-')

print(Back.GREEN, end = '')
a = int(input('Введите первое число'))
print(Back.CYAN, end = '')
b = int(input('Введите второе число'))
#print(Back.YELLOW, end = '')
if what == '+':
    print(Back.YELLOW, a, '+', b, '=', a + b)
elif what == '-':
    print(a, '-', b, '=', a - b)
