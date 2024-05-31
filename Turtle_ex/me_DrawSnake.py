import turtle


def DrawSnake(rad,angle,time,neckrad):
	'''
	画蛇
	:param rad: 半径
	:param angle: 弧度
	:param time: 循环次数
	:param neckrad: 蛇头的弧度
	:return:none
	'''
	for _ in range(time):
		turtle.circle(rad,angle)
		turtle.circle(-rad,angle)
	turtle.circle(rad,angle/2)
	turtle.forward(rad/2)
	turtle.circle(neckrad,180)
	turtle.forward(rad/4)





if __name__ == '__main__':
	#手动关闭画板turtle.setup(width=0.8,height=0.75)   #设置窗口大小
	turtle.pensize(30)     #画笔大小
	turtle.speed(2)
	turtle.color('green','white')     #画笔颜色绿，填充颜色白
	turtle.begin_fill()  #开始绘图
	turtle.penup()       #提笔，移动不画图
	turtle.setx(-200)    #设置起点
	turtle.pendown()     #下笔，移动画图
	turtle.seth(-40)     #方向

	DrawSnake(70,80,2,15)

	turtle.end_fill()    #结束画图
	turtle.done()