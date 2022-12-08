# https://pythobyte.com/what-is-asterisk-in-python-0f39ea7b/

def name(h, b, *args, key):
    print(h, b) # возьмут на себя по одному аргументу
    print(args)
    print(key)

name(1, 2, 3, 4, 5, key = 10) # можно передать сколь угодно аргументов
