def decor(f):
    def wrapper(): # функция-обёртка, чтобы декоратор стал декоратором
    #Имя этой функции - всергда wrapper
        print('Код декоратора')
        f()
        print('Второй код декоратора')
    return wrapper    


@decor # make = decor(make)
def make(): # 1. Обернём её код в другую функцию
    enter = input('Enter something... ')
    print(enter)

print('здесь')
make()
