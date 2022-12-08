m = 'stroka text'
count = 0

for i in m:
    if i == 't':
        continue
        print('В строке есть буква t')
        count += 1
    print(i)
#    if i == 'a':
#       break


else:
    print('Цикл завершён, букв t = ', count)

print('Программа работает дальше')
