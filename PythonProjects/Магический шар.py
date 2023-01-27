from random import randint

print('''Welcome world! I'm magic ball and I know answers to all questions!''', 'What is your name stranger? ')
name = input()
again = ''
print(f'Hola, {name}!')

def question(again):
    question = input(f'''Don't be shy. Put your {again} question here or put 'stop': ''')
    return question
list_of_answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
                   'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
                   'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
                   'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
                   'Перспективы не очень хорошие', 'Весьма сомнительно']
def choice(list_of_answers):
    answer = randint(1, 19)
    return list_of_answers[answer]

while True:
    if question(again).lower() == 'stop':
        print('See you later alligator')
        exit()
    else:
        print(choice(list_of_answers))
        again = 'next'

