# SquareSpiral1.py - Рисование квадратной спирали
import turtle
t = turtle.Pen()
colors = ['red', 'blue', 'salmon', 'green']
turtle.bgcolor('turquoise')
sides = 2
for x in range(300):
    t.pencolor(colors[x%4])    
    t.forward(x)
    t.left(61) # поэкспериментировать со значением угла
