# from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)


tim.shape("turtle")
tim.color("red")

# # Draw a Dashed Line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")


def random_color():
    """ Returns a random color in the rgb format """
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


def draw_shapes(sides):
    """ Draws various geometrical shapes """
    angle = 360/sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


# # Turtle walk
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# # Draw Shapes
# for no_sides in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shapes(no_sides)
#     tim.clear()

# Draw spiral graph
def spiral_graph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)


spiral_graph(5)

screen.exitonclick()



