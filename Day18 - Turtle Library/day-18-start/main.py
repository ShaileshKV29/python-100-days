from turtle import Turtle, Screen

t_object = Turtle()
# t_object.shape("turtle")
t_object.color("#1b1c1e")
# t_object.forward(100)
# t_object.right(90)
# t_object.forward(100)
# t_object.right(90)
# t_object.forward(100)
# t_object.right(90)
# t_object.forward(100)
# t_object.right(90)

# t_object.forward(100)
# t_object.dot(20)
# t_object.forward(100)

# for i in range(50):
#     if i % 2 != 0:
#         t_object.pendown()
#         t_object.forward(10)
#     else:
#         t_object.penup()
#         t_object.forward(10)

for _ in range(15):
    t_object.forward(10)
    t_object.penup()
    t_object.forward(10)
    t_object.pendown()



t_screen = Screen()
t_screen.exitonclick()
