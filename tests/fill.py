from turtle_pil import *

# Square in the upper-left quadrant.
pu()
goto(-160, 80)
seth(0)
pd()
color('red')
fillcolor('red')
begin_fill()
for _ in range(4):
    fd(70)
    lt(90)
end_fill()

# Triangle in the lower-right quadrant.
pu()
goto(120, -40)
pd()
color('blue')
fillcolor('blue')
begin_fill()
goto(180, -40)
goto(150, -110)
goto(120, -40)
end_fill()

# Filled circle.
radius = 75
pu()
goto(60, -40 - radius)
seth(0)
pd()
color('orange')
fillcolor('orange')
begin_fill()
circle(radius)
end_fill()

done()
