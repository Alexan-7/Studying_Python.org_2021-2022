import os # модуль по работе с операционной системой
import time # модуль по работе со временем
('D:\\Studying_Python_python.org\\для примера', ['папка 1', 'папка 2'],
 ['файл 1.txt', 'файл 2.txt', 'файл 3.bmp'])

spisok = []

for adress, dirs, files in os.walk('D:'): # первоначальный путь - \\Studying_Python_python.org\для примера
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 86555400: # if '.txt' in full: # если есть текстовые файлы, то только тогда добавлять в список
            spisok.append(full) # список с адресами ко всем папкам и файлам
print(spisok)



##import time
##('D:\\ДИССЕРТАЦИЯ - ПРЕДЗАЩИТА И ЗАЩИТА', ['Аспирантам к защите НКР и диссертации', 'До защиты 29.09.2020'],
## ['BIT_04_cover_PRINT.pdf'])
##
##spisok = []
##
##for adress, dirs, files in os.walk('D:\\ДИССЕРТАЦИЯ - ПРЕДЗАЩИТА И ЗАЩИТА'):
##    for file in files:
##        full = os.path.join(adress, file)
##        if time.time() - os.path.getctime(full) < 62208000: #'.txt' in full:
##            spisok.append(full)
##        
##print(spisok)
input('Нажмите Enter, чтобы выйти')
