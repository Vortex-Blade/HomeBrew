from turtle import *
color('green')
bgcolor('black')
speed(11)
hideturtle()
b = 0
while True:
    while b < 200:
        right(b)
        forward(b * 3)
        b = b + 1
        continue

