from turtle import *
import random

body = []

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.penup()
    pen.goto(-240, 240)
    pen.pendown()
    pen.begin_fill()
    pen.goto(240, 240)
    pen.goto(240, -240)
    pen.goto(-240, -240)
    pen.goto(-240, 240)
    pen.end_fill()

class Head(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape("arrow")
        self.color("green")
        self.speed(0)
        self.penup()
        self.goto(0, 0)
        self.direction = "stop"
        self.alive = True
        
        screen.onkey(self.up, "Up")
        screen.onkey(self.down, "Down")
        screen.onkey(self.left, "Left")
        screen.onkey(self.right, "Right")

    def up(self):
        if self.direction != "down":
            self.setheading(90)
            self.direction = "up"

    def down(self):
        if self.direction != "up":
            self.setheading(270)
            self.direction = "down"

    def left(self):
        if self.direction != "right":
            self.setheading(180)
            self.direction = "left"

    def right(self):
        if self.direction != "left":
            self.setheading(0)
            self.direction = "right"

    def move(self):
        if self.direction != "stop":
            self.forward(20)
        
        if self.xcor() > 240 or self.xcor() < -240 or self.ycor() > 240 or self.ycor() < -240:
            self.hideturtle()
            self.alive = False
    def collision(self):
        for i in body:
            if i.distance(head)<20:
                self.alive=False
class Apple(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.speed(0)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(random.randint(-230, 230), random.randint(-230, 230))
        self.st()

class Segment(Turtle):
    def __init__(self, other):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(other.pos())
        body.append(self)

    def move(self, other):
        for i in range(len(body) - 1, 0, -1):
            x = body[i - 1].xcor()
            y = body[i - 1].ycor()
            body[i].goto(x, y)
            
        x = other.xcor()
        y = other.ycor()
        body[0].goto(x, y)

def update():
    if head.alive:
        if head.distance(apple) < 20:
            apple.goto(random.randint(-230, 230), random.randint(-230, 230))
            Segment(head)
        if len(body)>0:
            body[0].move(head)
        head.move()
    screen.ontimer(update, 30)

screen = Screen()
screen.bgcolor("black")
screen.setup(520, 520)
screen.listen()

playing_area()
head = Head(screen)
apple = Apple()

update()
collision()
screen.exitonclick()





