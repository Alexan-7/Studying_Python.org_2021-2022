def decor(f):
    def wrapper():
        try:
            h = f()
        except Exception:
            print('Повторите ввод...')
            h = f()
        return h
    return wrapper # функция-декоратор возвращает нам имя вложенной функции wrapper
# имя make становится равным имени wrapper


@decor # make = decor(make) - имя функции make передается как аргумент
def make1():
    enter = float(input('Введите число: '))
    return enter
@decor
def make2():
    enter = float(input('Введите число опять: '))
    return enter 

make2()
make1()

'''
Как работают декораторы в этой программе:
Внутри функции-декоратора мы создаём вложенную функцию wrapper
и в главной функции decor пишем return wrapper.
стр. 7 - первое, что мы делаем - запускаем функцию в декораторе.
Мы должны сохранить возвращаемое значение h = f()

Обращаясь к функциям по именам (стр. 22, 23), можем исполнять
их код внутри функции-декоратора

'''
