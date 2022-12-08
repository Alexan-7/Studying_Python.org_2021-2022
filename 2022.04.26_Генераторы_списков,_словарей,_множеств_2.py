
h = [9, 8, 7, 4, 5, 6, 3, 2, 1, 5, 5, -2, -5]

newh = []
for x in h:
    if x % 2 == 0:
        newh.append(x*2)
print(newh)    

g = [x for x in h if x % 2 == 0 and x >0]
print(g)
print(type(g))
