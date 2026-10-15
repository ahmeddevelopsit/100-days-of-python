import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
colors = ["red", "green", "yellow", "blue", "magenta", "cyan"]
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                is_race_on = False
                print(f"you've won! The {winning_turtle} wins!")
            else:
                print(f"you've lost! The {winning_turtle} wins!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()