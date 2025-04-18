import turtle as t


t.speed(20)
t.color("black")
t.pensize("7")
t.shape("circle")
window=t.Screen()
window.bgcolor("yellow")
# t.ht()

t.penup()
t.goto(400,200)
t.pendown()
t.forward(300)
t.penup()
t.goto(550,230)
t.pendown()
t.left(90)
t.forward(55)

t.penup()
t.goto(550,230)
t.pendown()
t.left(60)
t.forward(-40)

t.penup()
t.goto(550,230)
t.pendown()
t.left(60)
t.forward(40)

t.penup()
t.goto(550,255)
t.pendown()
t.right(60)
t.forward(40)

t.penup()
t.goto(550,255)
t.pendown()
t.right(120)
t.forward(40)

t.penup()
t.goto(558,287)
t.pendown()
t.circle(20)

# توپ
t.penup()
t.goto(-400,-200)
t.pendown()
t.right(-150)
t.forward(300)

t.penup()
t.goto(-550,-200)
t.pendown()
t.right(180)
t.circle(20)

t.penup()
t.goto(-460,-107)
t.pendown()
t.right(150)
t.forward(140)
t.right(90)
t.forward(25)
t.right(90)
t.forward(140)
t.right(90)
t.forward(25)

t.penup()
t.goto(-554,-182)
t.pendown()
t.circle(5)

# تیر
t.penup()
t.goto(-465,-95)
t.pendown()
t.left(60)

t.pencolor("yellow")
a=float(input(' '))
b=float(input(' '))
t.left(a)
t.forward(b)

t.done()