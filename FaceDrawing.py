
import turtle

window = turtle.Screen()
window.bgcolor("lightblue")
window.title("Face")


Sofia = turtle.Turtle()
Rex = turtle.Turtle()
Lamp = turtle.Turtle()

def main():
    window = turtle.Screen()
    window.bgcolor("lightpink")
    window.title("Main")

def draw_face(face):
    
    Sofia.color("black") #circle
    Rex.color("blue")    #eyes
    Lamp.color("red") #mouth

    if face == "circle":

        Sofia.pendown()  #Draws circle
        for i in range(1, 360):   #This loop draws a circle
            Sofia.fd(1)  #Circle size / scale
            Sofia.lt(1) #Rotation
        Sofia.fd(0)    #Sofia moves forward

Sofia.penup() #moves up without drawing

def draw_pattern(geometry):

    if geometry == "triangle":
        Lamp.pendown()
        for i in range (0,3):
            Lamp.forward(50)
            Lamp.left(120)
        Lamp.forward(75)

    if geometry == "rectangle":
        Lamp.pendown()
        for i in range (0,4):
            Lamp.fd(50)
            Lamp.left(90)
        Lamp.forward(75)
            
Lamp.up()
Rex.up()

#Draws right eye from upper face
Rex.goto(25,265) # ( right (W/E, left N/S)
Rex.down()
Rex.begin_fill()
Rex.circle(5)
Rex.end_fill()
#draws left eye
Rex.up()
Rex.goto(-15,265)
Rex.down()
Rex.begin_fill()
Rex.circle(5)
Rex.end_fill()

#Upper face mouth
Lamp.up()
Lamp.goto(5,220)
Lamp.down()
Lamp.circle(50,70) #( Lenght, high scale)


Sofia.goto(0,200)  #it makes Sofia go up to draw a circle

draw_face("circle")


#Face: left side --> Draws left eye 
Rex.up()
Rex.goto(-265,70)
Rex.down()
Rex.begin_fill()
Rex.circle(5)
Rex.end_fill()
#Draws right eye
Rex.up()
Rex.goto(-290,70)
Rex.down()
Rex.begin_fill()
Rex.circle(5)
Rex.end_fill()

main()

#mouth

Lamp.up()
Lamp.goto(-230,10)
Lamp.down()
Lamp.circle(50,80)

Sofia.penup()

#Draws left eye
Rex.up()
Rex.goto(-10,120)
Rex.down()
Rex.begin_fill()
Rex.circle(5)
Rex.end_fill()
#Draws right eye
Rex.up()
Rex.goto(5,120)
Rex.down()
Rex.begin_fill()
Rex.circle(5)
Rex.end_fill()

Rex.up()
Rex.goto(0,1)

Rex.ht()

#draws mouth

Lamp.up()
Lamp.goto(2,90)
Lamp.down()
Lamp.circle(50,70)

Lamp.up()
Lamp.goto(0,0)

Sofia.goto(-250,0) #Sofia goes to the left screen corner
draw_face("circle")

draw_pattern("triangle")
draw_pattern("rectangle")
draw_pattern("triangle")
draw_pattern("rectangle")
draw_pattern("triangle")
draw_pattern("rectangle")
draw_pattern("triangle")

Lamp.ht()

Sofia.penup()
Sofia.goto(0,50)


draw_face("circle")

Sofia.ht()

