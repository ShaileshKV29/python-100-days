# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# extracted_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     extracted_colors.append((r, g, b))
# print(extracted_colors)
import random
import turtle
turtle.colormode(255)
extracted_colors = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]
screen = turtle.Screen()

turtle = turtle.Turtle()
y_dist = 1
turtle.speed('fastest')
turtle.hideturtle()
turtle.penup()
y_pos = -200
x_pos = -230
turtle.setposition(x_pos, y_pos)
for i in range(1, 101):
    turtle.dot(20, random.choice(extracted_colors))
    turtle.forward(50)
    if i % 10 == 0:
        turtle.setposition(x_pos, y_pos + y_dist*50)
        y_dist += 1

screen.exitonclick()
