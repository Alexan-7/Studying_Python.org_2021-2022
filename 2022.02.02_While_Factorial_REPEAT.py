while True:
    x = int(input())
    count = 0
    y = 1

    while count < x:
        count += 1
        y *= count

    else:
        print(y)
input('Нажмите Enter для выхода')
