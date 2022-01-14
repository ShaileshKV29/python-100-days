import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
bet = screen.textinput("Make your Bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

base_x = -230
base_y = -100

for turtle_index in range(0, 6):
    turtle_race = turtle.Turtle('turtle')
    turtle_race.penup()
    turtle_race.color(colors[turtle_index])
    turtle_race.goto(base_x, base_y)
    base_y += 40
    turtles.append(turtle_race)


if bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")

            is_race_on = False

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()
