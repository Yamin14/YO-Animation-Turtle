import turtle
pen = turtle.Turtle()
win = turtle.Screen()
win.bgcolor("#770077")

#setting the pen
pen.pensize(14)
pen.color("#77ff00")

#moving pen to starting position
pen.penup()
pen.setx(-250)
pen.sety(500)

#writing Y
pen.pendown()
pen.right(60)
pen.forward(260)
pen.left(120)
pen.forward(260)
pen.backward(460)

#writing O
pen.right(60)
pen.penup()
pen.forward(300)
pen.pendown()
pen.circle(150)

#writing !
pen.penup()
pen.forward(200)
pen.pendown()
pen.begin_fill()
pen.circle(1)
pen.fillcolor("#77ff00")
pen.end_fill()
pen.left(90)
pen.penup()
pen.forward(70)
pen.pendown()
pen.forward(300)

turtle.done()
