import turtle

screen = turtle.Screen()
drone = turtle.Turtle()


def move_forward():
    drone.forward(50)


def move_backward():
    drone.backward(50)


def move_left():
    drone.left(90)


def move_right():
    drone.right(90)


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

screen.mainloop()
