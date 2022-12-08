x = 5 # глобальная область видимости

def name():
    global x # хотим внести изменения в переменную из глобальной области видимости
    x = 100

    print(x)

name()
print(x)

def name2():
    print(x)
name2()
