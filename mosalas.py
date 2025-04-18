import turtle
import random

pen = turtle.Turtle()
pen.speed(8)  
pen.pensize(2)  

colors = ["red", "yellow", "blue"]

def draw_triangle(size):
    pen.color(random.choice(colors)) 
    for _ in range(3):  
        pen.forward(size)
        pen.left(120) 

def sierpinski(size, depth):
    if depth == 0: 
        draw_triangle(size)
        return

    sierpinski(size / 2, depth - 1) 
    pen.forward(size / 2)
    sierpinski(size / 2, depth - 1)  
    pen.left(120)
    pen.forward(size / 2)
    pen.right(120)
    sierpinski(size / 2, depth - 1)
    pen.right(120)
    pen.forward(size / 2)
    pen.left(120)

pen.penup()
pen.goto(-150, -100)
pen.pendown()

sierpinski(300, 3) 

pen.hideturtle()
turtle.done()
