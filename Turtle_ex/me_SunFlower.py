import turtle


turtle.pensize(8)
turtle.color('red','yellow')
turtle.speed(2)
turtle.begin_fill()
while True:
	turtle.forward(200)
	turtle.left(160)
	if abs(turtle.position()) < 1:   #离起点的位置小于设定值1则跳出,回到原点
		break

turtle.end_fill()
turtle.done()  #手动关闭画板