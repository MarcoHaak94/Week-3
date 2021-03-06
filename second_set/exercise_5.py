import turtle

screen = turtle.Screen()
tess = turtle.Turtle()

side_length = 50

# equilateral triangle
for _ in range(3):
    tess.forward(side_length)
    tess.left(120)

# square
for _ in range(4):
    tess.forward(side_length)
    tess.left(90)

# hexagon
for _ in range(6):
    tess.forward(side_length)
    tess.left(60)

# octagon
for _ in range(8):
    tess.forward(side_length)
    tess.left(45)

# exercise 8 18 sided polygon
for _ in range(18):
    tess.forward(side_length)
    tess.left(360 / 18)
    # 360 / 18 == 20 which is the answer to the question

screen.exitonclick()
