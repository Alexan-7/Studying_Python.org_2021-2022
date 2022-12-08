x = [9, 8, 7, 6, 5]
x.append(4) # метод добавляет элемент в конец списка
x.insert(1, 7) # добавляет элемент по указанному индексу
print(x.count(7)) # посмотреть кол-во одинаковых эл-тов в списке
x.sort() # сортирует список по возрастанию
x.reverse() # переворачивает список в обратную сторону
y = x.pop(0) # удаляет элемент по индексу
print(y)     # вывод удалённого элемента
x.remove(7) # удаляет элемент по его имени (один раз)
# x.clear() # полностью очищает список
x.extend(['a', 'b']) # добавить в конец списка другой список
h = x.copy() # скопировать/продублировать список в др. список
print(h)
print(x)