
from turtle import *

#saxli
width(7)
speed(5)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#movrchi kvadrats
begin_fill()
forward(200)
left(90)
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("blue")
begin_fill()
penup()
goto(150 ,175)
pendown()
left(30)
forward(40)
left(90)
forward(32)
left(90)
forward(40)
left(90)
forward(32)
end_fill()

begin_fill()
penup()
goto(26 ,175)
pendown()
left(90)
forward(40)
left(90)
forward(32)
left(90)
forward(40)
left(90)
forward(32)
end_fill()

exitonclick()

