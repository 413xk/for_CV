from random import randint
#добавить счетчик попыток и защиту от дурака у answer
rand = randint(1, 101)
print('Welcome to Ugadayka')


def is_valid(user_number):
    return user_number.isdigit() and 0 < int(user_number) < 101

def play_game(again):
    while True:
        answer = input(f'Do u wanna play {again}? Y = yes, N = no ').lower()
        if answer == 'n':
            print('See you later, Alligator!')
            exit()
        elif answer == 'y':
            print('Welcome!')
            loop()
            break
        else:
            continue

def loop():
    counter = 7
    while True:
        user_number = input(f'Put here number from 1 to 100, you have {counter} chances: ')
        if not is_valid(user_number) == True:
            print('God damn. Jesus Christ! ')
            continue
        else:
            user_number = int(user_number)

        if user_number == rand:
            print('Congratulations!')
            break
        elif user_number < rand:
            counter -= 1
            print(f'bigger than {user_number}')
        elif user_number > rand:
            print(f'less than {user_number}')
            counter -= 1
        if counter < 1:
            print('you loose :(')
            again = 'again'
            play_game(again)
            break
again = ''
play_game(again)