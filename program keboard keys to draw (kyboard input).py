import turtle as t

t.setup(700,700)
window = t.Screen()

# creating the player
player = t.Turtle(shape="classic")
player.shapesize(1,1,1)
player.screen.bgcolor("black")
player.color("red")
player.pen("re")
player.pensize(3)

def go_forward():
    player.forward(45)


def go_back():
    player.clear()
    player.back(45)


def turn_right():
    player.right(90)


def turn_left():
    player.left(90)

def clear_screen():
    player.clear()



window.onkey(go_forward, "Up")
window.onkey(go_back, "Down")
window.onkey(turn_right, "Right")
window.onkey(turn_left, "Left")
window.onkey(clear_screen, "Delete")


# Listen to /red the commands from the keyboard
window.listen()

window.mainloop()