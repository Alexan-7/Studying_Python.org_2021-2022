def some():
    list_text = []
    with open('2022.05.06_Text.txt', encoding='utf-8') as r:
        for x in r:
            list_text.append(x)
    return list_text

for i in some():
    print(i.split())

input('Нажмите Enter для выхода')    
    
'''
Считывает информацию с текстового документа,
возвращает список, выгрузив это в память.
'''
