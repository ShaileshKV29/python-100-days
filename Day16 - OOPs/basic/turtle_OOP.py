# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("triangle")
# timmy.forward(200)
# timmy.left(20)
# timmy.backward(200)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Demon Slayer", ["Taniro", "Zenitsu", "Inosuke"])
table.add_column("Breathing", ["Water/Sun", "Thunder", "Beast"])

print(table)