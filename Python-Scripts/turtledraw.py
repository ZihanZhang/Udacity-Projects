import turtle


def draw():
    canvas = turtle.Screen()
    canvas.bgcolor("blue")

    dudu = turtle.Turtle()
    dudu.forward(100)

    canvas.exitonclick()


draw()
