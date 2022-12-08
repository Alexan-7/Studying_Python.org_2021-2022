price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}

for key, value in price.items(): # распаковка кортежа
    print(key) # отдельно ключ
    print(value) # отдельно значение

new = {}
for key, value in price.items(): # поменяем местами ключ и значение
    new[value] = key # инверсия, реверс
print(new)

for value in price.values():
      print(value)

