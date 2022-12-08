# SquareSpiral1.py - Рисование квадратной спирали
import turtle
t = turtle.Pen()
colors = ['red', 'blue', 'salmon', 'green']
turtle.bgcolor('turquoise')
sides = 6
for x in range(1200):
    t.pencolor(colors[x%4])
    t.forward(x) # вместо circle
    t.left(61) # поэкспериментировать со значением угла
    t.left(90)
