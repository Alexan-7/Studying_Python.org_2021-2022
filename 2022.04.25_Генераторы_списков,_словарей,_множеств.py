
h = [9,8,7,4,5,6,3,2,1,5,5]

newh = []
for x in h:
    newh.append(x*2)
print(newh)    

n = [x*2 for x in h] # генератор списков - в 2 раза короче и быстрее
z = {x*2 for x in h} # множество не содержит дублирующих элементов
f = {x: x*2 for x in h} # фигурные скобки, НО генератор словаря {ключ: значение}

print(n)
print(z)
print(f)
