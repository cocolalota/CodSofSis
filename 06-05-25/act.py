import turtle
import math  # Importa el módulo math

class CursorControl:
    wn = None
    space = None
    speed = 1
    limite_x = 300
    limite_y = 300
    texto = None
    obstaculos = []

    def __init__(self):
        # Pantalla
        self.wn = turtle.Screen()
        self.wn.bgcolor("lightblue")
        self.wn.title("Juego con colisiones")
        self.wn.setup(width=600, height=600)

        # Tortuga jugador (cubo rojo)
        self.space = turtle.Turtle()
        self.space.shape("square")
        self.space.shapesize(1.5, 1.5)
        self.space.color("red")
        self.space.penup()

        # Texto en pantalla
        self.texto = turtle.Turtle()
        self.texto.hideturtle()
        self.texto.penup()
        self.texto.goto(0, 260)
        self.texto.color("black")
        self.mensaje("Usa las flechas para mover.")

        # Crear obstáculos (cubo negro)
        posiciones = [(100, 100), (-100, 50), (0, -100)]
        for pos in posiciones:
            obs = turtle.Turtle()
            obs.shape("square")
            obs.shapesize(1.5, 1.5)
            obs.color("black")
            obs.penup()
            obs.goto(pos)
            self.obstaculos.append(obs)

    def mensaje(self, texto):
        self.texto.clear()
        self.texto.write(texto, align="center", font=("Arial", 14, "bold"))

    # Dirección
    def arriba(self): self.space.setheading(90)
    def abajo(self): self.space.setheading(270)
    def izquierda(self): self.space.setheading(180)
    def derecha(self): self.space.setheading(0)

    def detectar_colision(self):
        for obs in self.obstaculos:
            if self.space.distance(obs) < 30:
                return True
        return False

    def trigger(self):
        self.wn.listen()
        self.wn.onkey(self.arriba, 'Up')
        self.wn.onkey(self.abajo, 'Down')
        self.wn.onkey(self.izquierda, 'Left')
        self.wn.onkey(self.derecha, 'Right')

        while True:
            # Movimiento y rebote
            x = self.space.xcor()
            y = self.space.ycor()
            h = self.space.heading()

            # Cambiar las funciones a math
            nuevo_x = x + self.speed * math.cos(math.radians(h))
            nuevo_y = y + self.speed * math.sin(math.radians(h))

            # Rebote si toca borde
            if -self.limite_x < nuevo_x < self.limite_x:
                self.space.setx(nuevo_x)
            else:
                self.space.setheading(180 - h)
                self.mensaje("¡Rebote lateral!")

            if -self.limite_y < nuevo_y < self.limite_y:
                self.space.sety(nuevo_y)
            else:
                self.space.setheading(-h)
                self.mensaje("¡Rebote vertical!")

            # Verificar colisión
            if self.detectar_colision():
                self.mensaje("💥 ¡Colisión detectada!")
                break

c = CursorControl()
c.trigger()



