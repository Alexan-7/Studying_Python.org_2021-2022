#m = [[5, 6], [1, 2], ['s', 'f']]

n = list(range(10))
m = []

for i in n:
    if i == 8:
        continue
    m += [i]

else:
    print(m)

#n = list(range(10))
#for i in n:
#    print(i)

#n = list(range(10))
#print(n)

#n = list('stroka') #конвертирует строку в список
#print(n)

#m = m * 2 #продублировали список
#print(m)

#m = m + [7] #добавили элемент
#print(m)

#m[1], m[2] = m[2], m[1] #смена местами вложенных списков
#print(m)

#m[0] = 9 #замена элемента списка
#print(m)
#m[0] = m[0] + 2 #увеличение элемента списка
#print(m)
