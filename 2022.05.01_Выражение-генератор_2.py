h = ['https:\\www.сайт.com', 'https:\\www.какойтосайт.net',
     'https:\\www.левыйсайт.ru',
     'https:\\www.другойсайт.org',
     'https:\\www.сайтишка.com', 'https:\\www.сайтец.info']

n = [x.split('\\')[1] for x in h if '.com' in x]   # генератор списка
print(type(n))

z = (x.split('\\')[1] for x in h if '.com' in x)   # выражение-генератор
print(type(z))
