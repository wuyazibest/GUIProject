import turtle


turtle.setup(width=0.5,height=0.75)
turtle.pensize(5)
turtle.speed(1)
turtle.color('yellow','red')
turtle.begin_fill()

for _ in range(5):
	turtle.forward(200)
	turtle.right(144)

turtle.end_fill()
turtle.penup()
turtle.goto(-150,-120)
turtle.color('violet')
turtle.write('Done',font = ('Arial',40,'normal'))

turtle.done()