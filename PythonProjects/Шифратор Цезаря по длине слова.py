# Шифратор Цезаря по длине слова (сдвиг = длина слова в буквах)

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
                    return alphabet_en * 2, alphabet_en_up * 2
            return 'en'
        elif choose_alphabet.lower() == 'ру' or choose_alphabet.lower() == 'ru':
            while True:
                    return alphabet_ru * 2, alphabet_ru_up * 2


# encrypt
def crypting(alphabet, alphabet_up):
    crypted_phrase = []
    phrase = input('Put your phrase here: ').split()
    for i in range(len(phrase)): #проходим по списку и каждому символу, чтобы его переместить на ключ вправо
        for j in range(len(phrase[i])):
            key = 0
            jjj = phrase[i]
            #находим ключ только из букв
            for s in jjj:
                if s.isalpha() == True:
                    key += 1

            if jjj[j].isalpha() == False:
                crypted_phrase.append(jjj[j])
            else:
                for k in range(len(alphabet)):
                    if jjj[j] == alphabet[k]:
                        crypted_phrase.append(alphabet[k + key])
                        break

                    if jjj[j] == alphabet_up[k]:
                        crypted_phrase.append(alphabet_up[k + key])
                        break

        crypted_phrase.append(' ')
    print(''.join(crypted_phrase))

def encrypting(alphabet, alphabet_up):
    encrypted_phrase = []
    phrase = input('Put your phrase here: ').split()
    for i in range(len(phrase)):  # проходим по списку и каждому символу, чтобы его переместить на ключ вправо
        for j in range(len(phrase[i])):
            key = 0
            jjj = phrase[i]
            # находим ключ только из букв
            for s in jjj:
                if s.isalpha() == True:
                    key += 1

            if jjj[j].isalpha() == False:
                encrypted_phrase.append(jjj[j])
            else:
                for k in range(len(alphabet)):
                    if jjj[j] == alphabet[k]:
                        encrypted_phrase.append(alphabet[k - key])
                        break

                    if jjj[j] == alphabet_up[k]:
                        encrypted_phrase.append(alphabet_up[k - key])
                        break

        encrypted_phrase.append(' ')
    print(''.join(encrypted_phrase))


while True:
    question = input('Do you want to crypt or encrypt? Press 1 or 2: ')
    if question == '1':
       alphabet, alphabet_up = choose()
       crypting(alphabet, alphabet_up)
       break
    elif question == '2':
      alphabet, alphabet_up = choose()
      encrypting(alphabet, alphabet_up)
      break

