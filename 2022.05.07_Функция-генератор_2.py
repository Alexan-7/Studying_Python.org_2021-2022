def some():
    with open('2022.05.06_Text.txt', encoding='utf-8') as r:
        for x in r:
            yield x

p = some()

print(p)

##print(next(p)) # одна строка из файла прочлась и выдалась при помощи оператора next
##print(next(p)) # вторая строка
##print(next(p)) # третья строка
##print(next(p)) # выдаст ошибку

for i in p:  # тот же результат,..
    print(i) # ... что и print(next(p))

input('Нажмите Enter для выхода')    
    
'''
Эта функция - это не функция, а объект-генератор
'''
