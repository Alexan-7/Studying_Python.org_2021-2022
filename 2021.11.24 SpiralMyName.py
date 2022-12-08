# SpiralMyName.py - печатает цветную спираль из имени пользователя

import turtle # Установка графики Turtle
t = turtle.Pen()
turtle.bgcolor('burlywood') # цвет с сайта https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html
colors = ['red', 'yellow', 'aquamarine', 'green']

# Запрос имени пользователя с помощью всплывающего окна textinput
your_name = turtle.textinput('Введите своё имя', 'Как Вас зовут?')

# Нарисовать на экране спираль из имени, повторенного много раз
for x in range(200):
    t.pencolor(colors[x%4]) # По очереди выбрать все 4 цвета
    t.penup() # Не рисовать обычные линии спирали
    t.forward(x*4) # Просто переместить черепашку по экрану
    t.pendown() # Написать имя пользователя, увеличивая каждый раз шрифт
    t.write(your_name, font = ('Arial', int((x + 4) / 4), 'bold'))
    t.left(92) # Повернуть налево, как в других спиралях
