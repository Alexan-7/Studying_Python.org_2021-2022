import os
h = [9, 8, 7, 4, 5, 6, 3, 2, 1, 5, 5, -2, -5]

price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}

new_price = {}
for i in price.keys():
    new_price[i] = round(price[i] * 0.85, 2)
print(new_price)
'''
в уроке "2022.02.26_Dictionaries2_part_II":
словарь new_price[новый_ключ] присвайваем ему значение из словаря
price[i] по ключу, применяем скидку 15%, округляем результат
функцией round(..., 2)
'''
    
new_d = {i: round(price[i] * 0.85, 2) for i in price.keys()}
print(new_d)
'''
Заводим переменную new_d. Записываем фигурные скобки. В скобках
for i in price.keys() (по ключу).
После { записываем i: и какое значение будет по этому ключу.
Записываем конструкцию round(price[i] * 0.85)
'''
z = (x*2 for x in h) # выражение-генератор - это совсем другое
print(z)

input('Введите Enter чтобы выйти')
