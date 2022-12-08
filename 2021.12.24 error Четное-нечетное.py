number = input("Введите любое число ")
if number == 0:
    print("Вы ввели число 0. Попробуйте другое число.")
if number % 2 == 0:
    print("Число {} яаляется четным".format(number))
else:
    print ("Число {} является нечётным".format(number))
input('Нажмите Enter для выхода')
