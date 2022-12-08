h = ['https:\\www.сайт.com', 'https:\\www.какойтосайт.net',
     'https:\\www.левыйсайт.ru',
     'https:\\www.другойсайт.org',
     'https:\\www.сайтишка.com', 'https:\\www.сайтец.info']

n = [x.split('\\')[1] for x in h if '.com' in x]   # генератор списка
print('n - ', n)

z = (x.split('\\')[1] for x in h if '.com' in x)   # выражение-генератор
print('z - ', z, "Пиши 'next(z)' и enter")

'''
>>> help(next)
Help on built-in function next in module builtins:

next(...)
    next(iterator[, default])
    
    Return the next item from the iterator. If default is given and the iterator
    is exhausted, it is returned instead of raising StopIteration.
'''
