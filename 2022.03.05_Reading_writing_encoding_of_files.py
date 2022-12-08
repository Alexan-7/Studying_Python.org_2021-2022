# код из урока "Парсер файлов"
import os

list_paths = []

for adress, papka, file in os.walk('D:\\'): 
    for i in file:
        full_path = os.path.join(adress, i)
        list_paths.append(full_path)


#'r' открыть для чтения (по умолчанию)
#'t' открыть в текстовом режиме (по умолчанию)
#'w' открыть для записи, содержимое файла удаляется. Если файла нет, то создаётся новый
#'a' открыть для дозаписи в конец файла; если файла нет, то создаётся новый
#'b' открыть в бинарном режиме
#'+' открыть для чтения и записи 'r+', 'w+', 'a+'

r = open('2022.03.05_Spisok_imyon.txt', 'w', encoding = 'UTF-8') # кодировку поменял. Была ANSI, выдавал error
for x in list_paths:
    r.write(x + '\n')
    
r.close()

##r = open('text.txt')
##u = r.read()
##print(u)
##r.close()
