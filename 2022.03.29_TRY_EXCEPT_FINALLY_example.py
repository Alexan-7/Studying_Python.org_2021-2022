import sys

url_list = ['text1.txt', 'text2.txt', 'text3.txt', 'text4.txt']

list_defect = []
list_info = []

try:
    for url in url_list:
        try:
            r = open(url, encoding = 'UTF-8')
            list_info.append(r.read())
            print('здесь')

        except Exception:
            list_defect.append(url) # если не смогли парсить информацию, то добавляем этот URL-адрес в список дефектных
            print('тут') # ошибка в отсутствующем файле
#            sys.exit()
            continue
        
finally: # этот оператор исполнит свой блок кода ВСЕГДА
    r = open('save.txt', 'a') # сохраним данные, 'a' - создать, если нет 
    for i in list_info: # проходимся циклом по списку с информацией
        r.write(i)
    r.write(str(list_defect)) # сконвертируем список дефектных адресов
    r.close
    print('Я всё записал, несмотря на ошибки!')
