# SquareSpiral1.py - Рисование квадратной спирали
import turtle
t = turtle.Pen()
turtle.bgcolor('turquoise')
sides = eval(input('Введите количество сторон от 2 до 6: '))

colors = ['red', 'salmon', 'blue', 'green', 'purple', 'coral']

for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1) # поэкспериментировать со значением угла
    t.width(x*sides/200)
    t.left(90)
