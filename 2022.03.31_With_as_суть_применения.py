##r = open('text-2022.03.31.txt', 'a')
##try:
##    r.write('something' + '\n')
##    10/0
##    r.write('что-то')
##finally:
##    r.close()

print('Все норм')

with open('text-2022.03.31.txt', 'a') as r:
    r.write('something' + '\n')
    10/0
    r.write('что-то' + '\n')
print('Все норм')
