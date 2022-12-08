enter = input('Your name: ')

s1 = 'Hello, %s, I am %s' % (enter, 'Python') # самый древний способ
print(s1)

s2 = 'Hello, {1}, I am {0}'.format (enter, 'Python') # более новый, но не очень удобный способ
print(s2)

s3 = f'Hello, {enter}, I can do it in f-string {2+2}' # f-строка - самый новый...
print(s3) # ...способ форматирования строк

s4 = f'Hello, {enter}, I can do it in f-string. Длина имени: {len(enter) символов}'
print(s4) # функция в строке
