while True:
    x = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    y = input('Введите строку:\n')

    for i in x: #берём одну букву из введённого текста
        count = 0
        for r in y:
            if i == r:  #сравниваем
                count +=1
        if count > 0:
            print('Букв ', i, ' было ', count)
