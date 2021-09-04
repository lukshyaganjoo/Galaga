import math
import turtle
import random
import winsound
import sys

#Set up the screen

main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.title("Galaga")
main_screen.bgpic("space_invaders_background.gif")


#Register the shapesize
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#Draw the border (turtle) (600 * 600 square)

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(2)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Setting Score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,250)
scorestring = "Score : %s" %score
score_pen.write(scorestring, False, align = "left", font = ("Arial", 14,"normal"))
score_pen.hideturtle()
#Create a player turtle for shooting

player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

#Creating player's bullet

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 25

#Defining bullet state(ready, fire)

bulletstate = "ready"

#Creating functional attributes for the keyboard(moving left and right)

playerspeed = 15
def move_left():
    x = player.xcor()
    x -= 15
    if x < -280:
        x = -280 #(blockade)
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 15
    if x > 280:
        x = 280 #(blockade)
    player.setx(x)

def fire_bullet():
    if not bullet.isvisible():
        winsound.PlaySound("laser.wav",winsound.SND_ASYNC)
        x = player.xcor()
        y = player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#Assigning values to keys on keyboard

turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(fire_bullet, "Up ")


#Choosing a number of enemies

number_of_enemies = 6
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())


for enemy in enemies:
#Creating enemy turtles and position

    enemy.speed(0)
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    x = random.randint(-250,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)
    enemyspeed = 4.5
# Loop
while True:

    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280: # (reversing enemy direction and pushing them down)
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= - 1
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.ycor() < -250:
            print("Game over")
            sys.exit()
            break

        if isCollision(bullet,enemy):
            #Reset bullet
            winsound.PlaySound("explosion.wav",winsound.SND_ASYNC)
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #Resetting enemy
            x = random.randint(-250,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            score += 10
            scorestring = "Score : %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left", font = ("Arial", 14,"normal"))


    if isCollision(player,enemy):
        winsound.PlaySound("explosion.wav",winsound.SND_ASYNC)
        player.hideturtle()
        enemy.hideturtle()
        sys.exit()
        break

    if bullet.isvisible():
        y = bullet.ycor() + bulletspeed
        bullet.sety(y)

        #Check to see if bullet has reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"



delay = input("Press enter to exit the game")
