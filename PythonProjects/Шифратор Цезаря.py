alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
alphabet_en = list(alphabet_en)
alphabet_en_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_en_up = list(alphabet_en_up)
alphabet_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabet_ru = list(alphabet_ru)
alphabet_ru_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_ru_up = list(alphabet_ru_up)


# choosing language and key
def choose():
    while True:
        choose_alphabet = input('which alphabet do you want to use EN or RU? ')
        if choose_alphabet.lower() == 'en':
            while True:
                key = int(input('put a key here from 1 to 25 '))
                if 0 < key < 26:
                    return alphabet_en * 2, alphabet_en_up * 2, key
            return 'en'
        elif choose_alphabet.lower() == 'ру' or choose_alphabet.lower() == 'ru':
            while True:
                key = int(input('put a key here from 1 to 31 '))
                if 0 < key < 32:
                    return alphabet_ru * 2, alphabet_ru_up * 2, key

 # присвоили вернувшийся результат функции choose
# crypt
def crypting(alphabet, alphabet_up, key): # разделить на 2 словаря и добавить ифы
    crypted_phrase = ''
    phrase = input('Put your phrase here: ')
    for i in range(len(phrase)):
        if phrase[i].isalpha() == False:
            crypted_phrase += phrase[i]
        else:
            for k in range(len(alphabet)):
                if phrase[i] == alphabet[k]:
                    crypted_phrase += alphabet[k + key]
                    break

                if phrase[i] == alphabet_up[k]:
                    crypted_phrase += alphabet_up[k + key]
                    break
    print(crypted_phrase)

def encrypting(alphabet, alphabet_up, key): # разделить на 2 словаря и добавить ифы
    encrypted_phrase = ''
    phrase = input('Put your phrase here: ')
    for i in range(len(phrase)):
        if phrase[i].isalpha() == False:
            encrypted_phrase += phrase[i]
        else:
            for k in range(len(alphabet)):
                if phrase[i] == alphabet[k]:
                    encrypted_phrase += alphabet[k - key]
                    break

                if phrase[i] == alphabet_up[k]:
                    encrypted_phrase += alphabet_up[k - key]
                    break
    print(encrypted_phrase)


while True:
    question = input('Do you want to crypt or encrypt? Press 1 or 2: ')
    if question == '1':
       alphabet, alphabet_up, key = choose()
       crypting(alphabet, alphabet_up, key)
       break
    elif question == '2':
      alphabet, alphabet_up, key = choose()
      encrypting(alphabet, alphabet_up, key)
      break

