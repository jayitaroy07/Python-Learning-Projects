import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
# Set up the screen width and length
screen.setup(width=500, height=400)
# Create a user input screen
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# Make a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# Create a list of positions for turtle on the racing track; note that the X axis value will be the same
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

# Create the turtle objects and assign the position
for turtle_index in range(0, 6):
    # Create turtle objects having shape as turtle
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(random.choice(colors))
    # Move the turtle to it's initial position
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

# To check whether user has given some input to bet on the race
if user_bet:
    is_race_on = True


while is_race_on:
    # Move the turtle forward with different speeds
    for turtle in all_turtle:
        # Check the boundary condition, when either of the turtle reaches the end, the game is over
        # End boundary = 250 - (40 / 2); 40 is the width and height of the turtle
        if turtle.xcor() > 230:
            # Once either of the turtle reaches the boundary, the game is over
            is_race_on = False
            # Turtle.color() returns both pencolor and fillcolor, here we are extracting only pencolor
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()