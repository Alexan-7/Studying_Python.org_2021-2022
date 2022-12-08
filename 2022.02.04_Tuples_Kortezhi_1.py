x = (9, 8, 7, 6)
y = (9) # скобки - это условность
z = (7,) # главное в кортеже - запятая
print(type(x))
print(type(y))
print(type(z))

a = tuple('stroka')
print(a)

b = [9, 8, 7, 6, 5, 4, 3]

for i in range(len(x)):
    b[i] += 3
    
print(b)








#z, c, k = b

r = 5
u = 7

r, u = (u, r) # обмен данными между переменными

print(b[1:5])
