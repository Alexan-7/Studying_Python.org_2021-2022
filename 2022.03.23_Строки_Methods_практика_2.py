q = open('2022.03.23_Text.txt', encoding = 'UTF-8')
r1 = q.read()
list_znk = ['(', ')', '"', '\n'] # создадим список и перечислим знаки, которые нужно удалить
for i in list_znk:
    r1 = r1.replace(i, ' ') # заменить знаки i на пустой знак
print(r1)

r2 = r1.split() # разбили по раздделителю (по умолчанию пробел)...
print(r2) # ...и получился список из слов

# теперь объединим их обратно
new_text = '_*_'.join(r2) # между апострофов запишем, чем заполнить пробелы между строк
print(new_text)

input('Введите Enter, чтобы выйти')
