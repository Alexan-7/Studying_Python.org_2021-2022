z = {1, 2, 3, 4, 5}
x = {4, 5, 6, 7, 8}
z.add(6) # добавить элемент (должен отличаться от тех, что есть)
z.discard(6) # удалить элемент
# z.remove(7) # если передать элемент, которого нет в множестве, то будет ошибка
y = z.union(x) # объединим множество z и множество x
# z.update(x) # объединить - добавить x в z
t = z.intersection(x) # определить пересечение множеств - их общие элементы
e = z.difference(x) # разница между множествами - какие значения из множества z не встречаются во множестве x
r = x.difference(z) # разница между множествами - какие значения из множества x не встречаются во множестве z

print(z)
print(y)
print(t)
print(e)
print(r)