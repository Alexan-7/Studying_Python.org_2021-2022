def some():
    with open('2022.05.06_Text.txt', encoding='utf-8') as r:
        for x in r:
            yield x

for i in some():
    print(i.split())

input('Нажмите Enter для выхода')    
    
'''
запускаем эту функцию в цикле for, который будет запрашивать
по одному значению за раз.
'''
