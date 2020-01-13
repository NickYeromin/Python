import turtle
import math

turtle.shape('turtle')
pi = 3.1415926
a = 5
k = 2 * pi
predel = 5 * 2 * pi
f = 0
while f < predel:
    p = k * f
    x = p * math.cos(f)
    y = p * math.sin(f)
    turtle.goto(x, y)
    print(x,y)
    f += 0.1


