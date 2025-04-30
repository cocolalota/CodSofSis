import turtle
class cursorcontrol:
    wn=None
    space=None
    speed=1
    def __init__(self):
        self.wn=turtle.Screen()
        self.wn.bgcolor('lightblue')
        self.space=turtle.Turtle()
        self.space.color('red')
        self.space.penup()

    def arriba(self):
        self.space.setheading(90)
    def abajo(self):
        self.space.setheading(270)
    def izquierda(self):
        self.space.setheading(180)
    def derecha(self):
        self.space.setheading(0)

    def trigger(self):
        self.wn.listen()
        self.wn.onkey(self.arriba, 'Up')
        self.wn.onkey(self.abajo, 'Down')
        self.wn.onkey(self.izquierda, 'Left')
        self.wn.onkey(self.derecha, 'Right')
        while True:
            self.space.forward(self.speed)

c=cursorcontrol()
c.trigger()