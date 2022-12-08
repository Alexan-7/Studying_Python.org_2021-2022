# SquareSpiral1.py - Рисование квадратной спирали
import turtle
t = turtle.Pen()
t.pencolor("salmon")
for x in range(300):
    t.circle(x)
    t.left(61) # поэкспериментировать со значением угла
