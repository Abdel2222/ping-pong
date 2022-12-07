
import turtle # importer la classe de toertue pour creer un jeu 

wind = turtle.Screen() # creer une fenetre 
wind.title("ping pong") # donner un titre a la fenetre du jeu
wind.bgcolor("black") # mettre une couleur au bg du window
wind.setup(width=800,height=600) # definir une hauteur et largeur de la fenetre
wind.tracer(0) # controler la mise a jour 
Racket1 = turtle.Turtle()# creer une fenetre 
Racket1.speed(0)# vitesse 
Racket1.shape("square")#forme objet
Racket1.color("red")# couleur
Racket1.penup()# pas de ligne laissee derriere
Racket1.goto(-350,0)#position 
Racket1.shapesize(stretch_wid=3,stretch_len=2)# dimension
Racket2 = turtle.Turtle()
Racket2.speed(0)
Racket2.shape("square")
Racket2.color("green")
Racket2.penup()
Racket2.goto(350,0)
Racket2.shapesize(stretch_wid=3,stretch_len=2)
#Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx = 1 # type: ignore
Ball.dy = 1 # type: ignore # delta de vitesse en px en diagognale avec l axe x,y
#score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("joueur Papa:0 joueuse2 Alice:0", align="center",font=("Courier",24,"normal"))
score.clear()

def  Racket1_up():
     y = Racket1.ycor()
     y += 20
     Racket1.sety(y)
def  Racket1_down():
      y = Racket1.ycor()
      y -= 20
      Racket1.sety(y)
def  Racket2_up():
         y = Racket2.ycor()
         y += 20
         Racket2.sety(y)

def  Racket2_down():
          y = Racket2.ycor()
          y -= 20
          Racket2.sety(y)
wind.listen()# attente que le clavier soit saisit
wind.onkeypress(Racket1_up,"w")# evenement recuperer lorsque la touche est active la fonction est execute sur le window
wind.onkeypress(Racket1_down,"z")
wind.onkeypress(Racket2_up,"Up")
wind.onkeypress(Racket2_down,"Down")
while True :
    wind.update()
    # move the ball 
    Ball.setx(Ball.xcor() + Ball.dx)  # type: ignore
    Ball.sety(Ball.ycor() + Ball.dy)  # type: ignore
    # limiter les dimensions de la balle
    if Ball.ycor() >290:
        Ball.sety(290)
        Ball.dy *= -1  # type: ignore
    if Ball.ycor() <-290:
           Ball.sety(-290)
           Ball.dy *= -1  # type: ignore
    if  Ball.xcor() >390:
        Ball.goto(0,0)
        Ball.dx *=-1  # type: ignore
    if Ball.xcor() <-390:
        Ball.goto(0,0)
        Ball.dx *=-1  # type: ignore
       
    if (Ball.xcor()>340 and Ball.xcor()<350 ) and(Ball.ycor() < Racket2.ycor() +40 and Ball.ycor()> Racket2.ycor() - 40):
         Ball.setx(340)
         Ball.dx*=-1  # type: ignore
         score1 +=1  # type: ignore
         score.clear()
         score.write("joueur1 Papa: {} joueuse2 Alice: {} ".format(score1,score2), align="center",font=("Courier",24,"normal"))
    if (Ball.xcor()<-340 and Ball.xcor()>-350 ) and(Ball.ycor() < Racket1.ycor() +40 and Ball.ycor() >Racket1.ycor() -40):
         Ball.setx(-340)
         Ball.dx*=-1  # type: ignore
         score2 +=1
         score.clear()
         score.write("joueur Papa:{} joueuse2 Alice:{}".format(score1,score2), align="center",font=("Courier",24,"normal"))

