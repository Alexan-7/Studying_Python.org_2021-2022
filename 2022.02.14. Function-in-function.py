x = 5

def name():
    x = 10
    def name2():
        nonlocal x # меняем значение в материнской функции
        x = 100
        print(x)

    name2() # 2. Потом срабатывает print функции name2
    print(x)

name() # 1. Сначала запускаем name и запускается функция name2
print(x) # 3. Срабатывает print глобальной области видимости
