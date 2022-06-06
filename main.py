# import colorgram
#
# colors = colorgram.extract('hirst_spot_painting.jpg', 10)
# rgb_color = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)
import turtle
from turtle import Turtle , Screen
import random

color_list = [(226, 231, 236), (58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (142, 178, 203), (139, 82, 105)]

turtle.colormode(255)
tim = Turtle()
tim.speed(10)
tim.penup()
tim.hideturtle()

y_pos = -200

for i in range(10):
    tim.setposition(-250.00, y_pos)
    y_pos += 50
    for j in range(10):
        random_color = random.choice(color_list)
        tim.dot(20, random_color)
        tim.forward(50)

screen = Screen()
screen.exitonclick()


