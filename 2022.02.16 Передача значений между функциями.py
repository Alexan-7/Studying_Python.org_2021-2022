import math

PI = math.pi # только одна глобальная переменная

# .replace(',', '.') позволяет вводить не только числа с точкой, но и с запятой

def radius():
    n = float(input('Введите диаметр цилиндра в см: ').replace(',', '.'))
    n /= 2
    return n

def height():
    m = float(input('Введите высоту цилиндра в см: ').replace(',', '.'))
    return m

def volume(): 
    r = radius()
    h = height()
    s = PI * r ** 2
    v = s * h
    return v

# print('Объём цилиндра ', volume(), 'см^3')

def massa(g):
    n = float(input('Введите удельный вес гр/см^3: ').replace(',', '.'))
    return g * n / 1000
print ('Вес цилиндра в кг: ', massa(volume())) # аргумент volume передаётся в функцию massa

# мы никак не беспокоимся об именах переменных
