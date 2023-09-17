from random import randint
from functools import partial
from turtle import Screen, Turtle
import time

screen = Screen()
screen.bgcolor('gray')

turtleFunction1 = Turtle()
turtleFunction1.hideturtle()
turtleFunction1.shape('turtle')
turtleFunction1.turtlesize(3, 3, 3)
turtleFunction1.speed(0)


turtleFunction2 = Turtle.clone(turtleFunction1)
turtleFunction2.hideturtle()
turtleFunction2.penup()
turtleFunction2.goto(-75, 350)
turtleFunction2.write("Score :       Points", font=('Arial', 24, 'normal'), align='center')
turtleFunction2.goto(-65, 320)
turtleFunction2.write("  Time  :       Seconds", font=('Arial', 24, 'normal'), align='center')
turtleFunction2.speed(0)


turtleFunction3 = Turtle.clone(turtleFunction1)
turtleFunction3.hideturtle()
turtleFunction3.penup()
timeD = 20
turtleFunction3.goto(-80, 320)
turtleFunction3.write(f"{timeD}", font=('Arial', 24, 'normal'))
turtleFunction3.speed(0)

turtleFunction4 = Turtle.clone(turtleFunction1)
turtleFunction4.hideturtle()
turtleFunction4.penup()
turtleFunction4.speed(0)
score = 0
turtleFunction4.clear()
turtleFunction4.goto(-80, 350)
turtleFunction4.write(f"{score}", font=('Arial', 24, 'normal'))


def timerFunction(a):
    turtleFunction3.clear()
    turtleFunction3.goto(-80, 320)
    turtleFunction3.write(f"{a}", font=('Arial', 24, 'normal'))


def scoreFunction(*args):
    global score

    if timeD > 0:

        score = score+1
        turtleFunction4.clear()
        turtleFunction4.goto(-80, 350)
        turtleFunction4.write(f"{score}", font=('Arial', 24, 'normal'))

        print(score, "points")
    else:
        print("Game Over")



for a in range(20):

    turtleFunction1.penup()
    turtleFunction1.turtlesize(2, 2, 3)
    turtleFunction1.color("navy")
    turtleFunction1.fillcolor("yellow")

    x = randint(-35, 35)
    y = randint(-35, 35)
    turtleFunction1.goto(10 * x, 10 * y)
    turtleFunction1.showturtle()
    time.sleep(0.5)
    timeD = timeD - 1
    timerFunction(timeD)
    print(timeD, "seconds")


    turtleFunction1.onclick(partial(scoreFunction,turtleFunction1))

    if timeD == 0:
        turtleFunction3.goto(-150, 150)
        turtleFunction3.write("Time's Up!", font=('Arial', 50, 'normal'))
        turtleFunction4.goto(-250, 0)
        turtleFunction4.write("Game Over!", font=('Arial', 75, 'normal'))

        print("Time's Up!")
        turtleFunction1.ht()
        break




screen.mainloop()
