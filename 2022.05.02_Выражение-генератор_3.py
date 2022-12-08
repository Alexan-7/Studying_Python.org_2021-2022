h = ['https:\\www.сайт.com', 'https:\\www.какойтосайт.net',
     'https:\\www.левыйсайт.ru',
     'https:\\www.другойсайт.org',
     'https:\\www.сайтишка.com', 'https:\\www.сайтец.info']

z = (x.split('\\')[1] for x in h if '.com' in x)   # выражение-генератор

for i in z: # итерируем выражение-генератор
    print(i)
