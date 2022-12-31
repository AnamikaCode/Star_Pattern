import turtle
import colorsys
s=turtle.Screen()
turtle.title('Star Design')
s.setup(width=550,height=650)
turtle.bgcolor('white')
turtle.tracer(2)
c=10
for i in range(350):
     p=colorsys.hsv_to_rgb(c,1,0.99)
     c+=0.003
     turtle.pencolor(p)
     turtle.right(120)
     turtle.right(295)
     turtle.left(290)
     turtle.forward(i)
     turtle.left(200)
     turtle.forward(i)
     turtle.right(30)
     
turtle.done()