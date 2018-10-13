import turtle

turtle.showturtle()
turtle.pensize(3)  # 1
turtle.speed(10)  # 2

# 三角形
turtle.penup()  # 使笔抬起
# 将turtle移动到任意一个特定的点(x,y)
turtle.goto(-200, 0)
# 使笔落下
turtle.pendown()
turtle.begin_fill()  # 3
turtle.color("blue")
turtle.circle(50, steps=3)  # 4
turtle.end_fill()  # 5

# 五边形
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("green")
turtle.circle(50, steps=5)
turtle.end_fill()

# 七边形
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.circle(50, steps=7)
turtle.end_fill()

turtle.color("blue")
turtle.penup()
turtle.goto(-230, -60)
turtle.pendown()
turtle.write("三角形", font=("Times", 18, "bold"))

turtle.color("green")
turtle.penup()
turtle.goto(-35, -60)
turtle.pendown()
turtle.write("五边形", font=("Times", 18, "bold"))

turtle.color("purple")
turtle.penup()
turtle.goto(170, -60)
turtle.pendown()
turtle.write("七边形", font=("Times", 18, "bold"))

turtle.hideturtle()

# 导致程序暂停直到用户关闭Python turtle图形化窗口位置，它的目的是给用户时间来查看图形，没有这一行，图形窗口会在程序完成时立即关闭
turtle.done()
