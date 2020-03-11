import turtle
from turtle import *

screen = Screen()
t = turtle.Screen()
t.speed(-1) # max speed
screen.bgcolor("blue")
t.pencolor("red")
t.pensize(10)

wn = turtle.Screen()
def test(x):
    t.forward(x)
    t.left(x)
    t.forward(x)


t.onclick(test(50))

# def draggin(x,y):
#
#     t.ondrag(None)
#     t.setheading(t.towards(x, y))
#     t.goto(x, y)
#     t.ondrag(draggin)
#
#
# def click():
#     t.clear()
#
#
# def main():
#     turtle.listen()
#     t.ondrag(draggin)
#     turtle.onscreenclick(click(),3) # 3 = right mouse button

screen.mainloop()



if __name__ == '__main__':
    main()
