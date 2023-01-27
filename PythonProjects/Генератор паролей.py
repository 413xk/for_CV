from random import randint
print('''Hi! I can generate you safe password. Let's do it!''')
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
special_symbols = 'il1Lo0O'
chars = ''
number_of_passwords = int(input('How many passwords do you need to generate? '))
lenght = int(input('What lenght of password do you want? '))
question1 = input(f'Do you want to add digits {digits}? y = yes, n = no ')
question2 = input(f'Do you want to add lower case letters {lowercase_letters}? y = yes, n = no ')
question3 = input(f'Do you want to add upper case letters {uppercase_letters}? y = yes, n = no ')
question4 = input(f'Do you want to add punctuation signs {punctuation}? y = yes, n = no ')
question5 = input(f'Do you want to exclude bad symbols? {special_symbols} ? y = yes, n = no ')

if question1 == 'y':
    chars += digits
if question2 == 'y':
    chars += lowercase_letters
if question3 == 'y':
    chars += uppercase_letters
if question4 == 'y':
    chars += punctuation
if question5 == 'y':
    for i in special_symbols:
        chars = chars.replace(i, '')


def generate_password(number_of_passwords, lenght, chars):
    for i in range(number_of_passwords):
        password = []
        for k in range(lenght):
            password.append(chars[randint(1, len(chars) - 1)])
        print('Here is your safe password: ', *password, sep = '')

generate_password(number_of_passwords, lenght, chars)





