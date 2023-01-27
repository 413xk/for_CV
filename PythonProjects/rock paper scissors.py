teamoor,russlane = input(),input()
rock_paper_scissors = {
    "ножницы": ['бумага', 'ящерица'],
    "бумага": ['камень','Спок'],
    "камень": ['ящерица','ножницы'],
    "ящерица": ['Спок','бумага'],
    "Спок": ['ножницы','камень']
}
if russlane in rock_paper_scissors[teamoor]:
    print('Тимур')
elif teamoor in rock_paper_scissors[russlane]:
    print('Руслан')
else:
    print('ничья')