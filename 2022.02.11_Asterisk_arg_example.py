def exclusive_item(*args, key = False):
    new_list = []
    for i in args: # кортеж из трёх списков обрабатываем циклом
        for y in i: # итерируем список, который уже в переменной i
            if y not in new_list:
                new_list.append(y)
    if key == True: # если убрать из вызова функции, то список не отсортируется
        new_list.sort()
    return new_list

z = [9, 8, 7]
x = [8, 15, 9, 7, 6, 5]
c = [1, 2, 3, 4, 5, 6, 7, 10]

t = exclusive_item(z, x, c, key = True) # к ключевому параметру надо обратиться по имени
print('t =', t)
