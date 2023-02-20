import turtle  
tao = turtle.Turtle()  
tao.shape('turtle')
tao.speed(0)
tao.penup()
tao.setpos(-400, 0)
tao.pendown()

for o in range(3):
    for r in range(100):
        for i in range(4):
            tao.pendown()
            tao.color('red')
            tao.forward(30)
            tao.left(90)
            tao.begin_fill()
            for p in range (1):
                tao.circle(7)
                tao.forward(5)
                tao.circle(6)
                tao.forward(10)
                tao.circle(3)
            tao.end_fill()
            tao.left(3.6)
        tao.penup()
        tao.forward(30)
        tao.right(3.6)
    tao.penup()
    tao.forward(250)
    tao.right(7.2)

turtle.mainloop()  