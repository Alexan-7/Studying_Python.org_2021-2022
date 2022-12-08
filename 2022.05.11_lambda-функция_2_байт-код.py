from dis import dis # покажет байт-код интерпретатора

def some(x):
    return x/5

var = lambda x: x/5 # аналогично записи def some():, x - параметр, после двоеточия - желаемое выражение

print(dis(some)) # запускаем функцию dis и передаём имя функции some
print(dis(var)) # ... передаём переменную, которая ссылается на объект функции lambda

input('enter')
