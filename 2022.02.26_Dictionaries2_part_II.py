price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}

new_price = {}
for i in price.keys():
    new_price[i] = round(price[i] * 0.85, 2) # работаем со значениями словаря, обращаемся непосредственно к словарю

print(price) # проитерировали словарь, поменяли значения со скидкой
print(new_price)
