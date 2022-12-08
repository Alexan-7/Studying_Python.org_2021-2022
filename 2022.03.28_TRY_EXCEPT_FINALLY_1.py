f = '2022.03.28_try_except_finally'
print(f.upper()) # в верхний регистр

while True:
    try: # туда - код, где может произойти ошибка
        enter = float(input('Введите число: ')) # если происходит ошибка, то до break доходить не будет
        print(100/enter)
        # break # прерывает цикл

    except(ValueError): # перехватил ошибку
        print('Введено НЕ число. Попробуйте снова')

    except(ZeroDivisionError): # перехватил ошибку
        print('Делить на ноль нельзя!')

# исполнится тогда, если не было ошибки в блоке try и изначально всё было как надо
    else: # дополнительный необязательный оператор
        print('Пользователь молодец, с первого раза!')

print('Всё норм')
