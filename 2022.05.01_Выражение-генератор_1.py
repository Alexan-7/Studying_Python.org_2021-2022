h = ['https:\\www.сайт.com', 'https:\\www.какойтосайт.net',
     'https:\\www.левыйсайт.ru',
     'https:\\www.другойсайт.org',
     'https:\\www.сайтишка.com', 'https:\\www.сайтец.info']

n = [x.split('\\')[1] for x in h]   # генератор списка
b = [x.split('\\')[1] for x in h if '.com' in x]   # генератор списка

while True:
    lis = eval(input('Введите список n или список b: '))
    if lis == n:
        print('n - ', type(n), n)
    elif lis == b:
        print('b - ', type(b), b)
