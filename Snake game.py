# Creator : Lissan Koirala
# Date of Creation : 13/04/2020

# Importibg all the things
import turtle
import time
import random
import tkinter as tk


def snake(speed):
    score = 0
    high_score = 0                             # [  TO DISPLAY THE SCORES ]
    def score_display(how):
        scores = tk.Tk()
        lb1 = tk.Label(scores,text="GAME OVER !", fg="red")
        lb1.grid(row=1,column=1)
        lb2 = tk.Label(scores,text="High Score:", fg="blue")
        lb2.grid(row=2,column=1)
        lb = tk.Label(scores,text=high_score, fg="blue")
        lb.grid(row=2,column=2) 
        lb3 = tk.Label(scores, text="Current Score:", fg="Green")
        lb3.grid(row=3,column=1)
        lb31 = tk.Label(scores, text=score, fg="Green")
        lb31.grid(row=3,column=2)
        lb1 = tk.Label(scores, text=how, fg="red")
        lb1.grid(row=4,column=1)
    ###########
    window = turtle.Screen()  # Creating a window
    window.title("Snake game by LK")  # Naming the window
    window.bgcolor("white")  # Defining the background color
    window.setup(height=400, width=400)  # Defining the size of the window  'The Board'
    ###########

    window.tracer(0)  # Turns off the screen uptades

    ###########
    head = turtle.Turtle() # Snake Head
    head.speed(0)  # It's the highest speed that the snake can run                           [ SNAKE HEAD ]
    head.shape("square")  # The shape of the snake's head
    head.color("#006600")  # The color of head 'Snake'
    head.penup()  # Penup because it doesn't let the turtle to draw on the screen ,""" If we let it to draw then it will mess up the whole screen
    head.goto(0,0)  # It lets that the snake start on the middle of the screen
    head.direction = "stop"  # We don't want the snake to start messing up at the beggining until we want it to do so
    ###########
    food = turtle.Turtle() # Snake Food                  
    food.shape("circle")  # The shape of the snake's head                                      [ SNAKE FOOD ]
    food.color("red")  # The color of head 'Snake'
    food.penup()  # Penup because it doesn't let the turtle to draw on the screen ,""" If we let it to draw then it will mess up the whole screen
    food.goto(60,120)  # It lets that the snake doesn-t start on the middle of the screen
    ###########

    # Function to move the snake   ( We are defining the line 35  )
    def go_up():
        if head.direction !="down":
            head.direction="up"
    def go_down():
        if head.direction !="up":
            head.direction="down"
    def go_right():
        if head.direction !="left":
            head.direction="right"
    def go_left():
        if head.direction !="right":
            head.direction="left"

    # Defining if it's up moves 20 units up and so on...
    def  move():
        if head.direction == "up":
            y = head.ycor()
            head.sety( y+20 )

        if head.direction == "down":
            y = head.ycor()
            head.sety( y-20 )

        if head.direction == "left":
            x = head.xcor()
            head.setx( x-20 )

        if head.direction == "right":
            x = head.xcor()
            head.setx( x+20 )
            
    # Keyboard bindings (  Turning the keyboard commands to some functions below )
    window.listen()
    window.onkeypress(go_up, "Up")
    window.onkeypress(go_down, "Down")
    window.onkeypress(go_left, "Left")
    window.onkeypress(go_right, "Right")

    segment=[ ]
    # Main game loop to start 
    while True:
        window.update()
        
        # Check for the collision with the borders  [  If the snakes goes out the screen then the game is over ]
        if head.xcor()>170 or head.xcor()<-170 or head.ycor()>170 or head.ycor()<-170:
            time.sleep(1)  # Sleeps for a second to seem that the game restarted
            head.goto(0,0)  #vGoes to middle to restart the game
            head.direction = "stop"

            # Hide the segment
            for segments in segment:
                segments.goto(1000,1000) # Hiding it by giving the coordenetes that doesn't exists
            segment.clear()  # Clear the segment so that the body doesn't appears above the head

            # Showing the score
            score_display("You collied with the border !")

            score = 0
            
        # Check a collision with a food
        if head.distance(food) < 20:
            # Move the food to the random place
            x = random.randint( -150,150 )
            y = random.randint( -150,150 )
            food.goto( x,y )

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("#009900")
            new_segment.penup()
            segment.append(new_segment)

            # Increasing the score
            score += 10

            if score > high_score:
                high_score = score


    #################################################
        # Moving the end segment first in reverse order
        for index in range(len(segment)-1,0,-1):
            x = segment [index-1] .xcor()
            y = segment [index-1] .ycor()
            segment [index].goto(x,y)
                                                                                                            #   [ """  I DIDN'T UNTERSTOOD THIS PART  """ ]
        # Move the segment 0 to where the head is
        # [ Adding the size of the snake ]
        if len(segment)>0:
            x = head.xcor()
            y = head.ycor()
            segment[0].goto(x,y)
    ##################################################

        move()

        # Checking for the collision with the body
        for segments in segment:
            if segments.distance(head)<20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"

                # Hide the segment
                for segments in segment:
                    segments.goto(1000,1000) # Hiding it by giving the coordenetes that doesn't exists
                segment.clear()  # Clear the segment so that the body doesn't appears above the head
                
                # Showing the score
                score_display("You ate yourself !")
                score = 0
            
        time.sleep(speed) # Because if not the snake will go so fast that we even can't see it 

    window.mainloop()

###########
###########
###########

def easy():
    snake(0.15)
def medium():
    a=(0.1)-(0.02)                     # [ Defining the buttons of level ]
    snake(a)
def hard():
    a=(0.1)-(0.04)
    snake(a)

###########

board = tk.Tk()
canvas = tk.Canvas(board, height=10, width=100)
canvas.pack()
lb = tk.Label(board, text="Snake Game", fg="green")
lb.pack()
bt1 = tk.Button(board, text="Easy", command=easy)           # [ Creating a window to select the level of difficulty ]
bt1.pack()
bt2 = tk.Button(board, text="Medium", command=medium)
bt2.pack()
bt3 = tk.Button(board, text="Hard", command=hard)
bt3.pack()
board.mainloop()

###########
###########
###########




