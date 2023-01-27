#hash table

phonebook = {}
def phonebook_checker(name):
    if phonebook.get(name):
        return 'Contact is already exist!'
    else:
        phonebook[name] = input('Put a number ')
        print(phonebook)
        return f'Contact {name} was successfully created!'

while True:
    print(phonebook_checker(input('put a name ')))