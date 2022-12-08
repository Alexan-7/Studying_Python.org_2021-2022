# захламление глобальной области не приветствуется
x = 5

def name():

    x = 100

    return name2(x)

def name2(par):
    print(par)

    name()
