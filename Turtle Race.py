# Creator : Lissan Koirala
# Date of Creation : 18/04/2019

import turtle
import random
import time
import tkinter as tk

one = ""
two = ""
three = ""
four = ""
    
# Guessing who is gonna win
win = tk.Tk()
win.title("Lissan Game - Trutle Race")
lb = tk.Label(win, text="Turtle Race", fg="brown")
lb.grid(row=1,column=0)
lb =  tk.Label(win, text="Choose your Player:")
lb.grid(row=1,column=1)

bt1 = tk.Label(win,text="Black Turtle", fg="black")
bt1.grid(row=3,column=0)
entry1 = tk.Entry(win)
entry1.grid(row=3,column=1)

bt1 = tk.Label(win,text="Yellow Turtle", fg="#ffcc00")
bt1.grid(row=4,column=0)
entry2 = tk.Entry(win)
entry2.grid(row=4,column=1)

bt1 = tk.Label(win,text="Blue Turtle", fg="blue")
bt1.grid(row=5,column=0)
entry3 = tk.Entry(win)
entry3.grid(row=5,column=1)

bt1 = tk.Label(win,text="Green Turtle", fg="green")
bt1.grid(row=6,column=0)
entry4 = tk.Entry(win)
entry4.grid(row=6,column=1)

lb = tk.Label(win,text="© Lissan Koirala",fg="red")
lb.grid(row=7,column=1)

def getinfo():
    global one
    global two
    global three
    global four
    one = entry1.get()
    two = entry2.get()
    three = entry3.get()
    four = entry4.get()
    win.destroy()
    
submit = tk.Button(win,text="Submit",command=getinfo)
submit.grid(row=7,column=0)

win.mainloop()

# Creating Window
window = turtle.Screen()
window.title("Turtle Race by 'Lissan'")
turtle.bgcolor("white")
turtle.speed(0)
turtle.penup()
turtle.goto( -90,150 )
turtle.write("Turtle Race", font=("Arial",30,"bold"))
turtle.forward(220)
turtle.penup()
turtle.goto(80,-150)
turtle.color("green")
turtle.write("© Lissan Koirala", font=("Arial",15,"bold"))
turtle.pendown()
turtle.penup()
turtle.shape("turtle")
turtle.color("red")

# Finish line
turtle.begin_fill()
turtle.goto(150,100)
turtle.pendown()
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(10)
turtle.end_fill()
turtle.hideturtle()

# Turtle 1
turtle1 = turtle.Turtle()
turtle1.speed(0)
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250,70)

# Turtle 2
turtle2 = turtle.Turtle()
turtle2.speed(0)
turtle2.color("#e6b800")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250,20)

# Turtle 3
turtle3 = turtle.Turtle()
turtle3.speed(0)
turtle3.color("blue")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250,-30)

# Turtle 4
turtle4 = turtle.Turtle()
turtle4.speed(0)
turtle4.color("green")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250,-80)

# End the game
def finish(n):
        if n == 1:
            te = one
            c = "Black"
        elif n == 2:
            te = two
            c = "#ffcc00"
        elif n == 3:
            te = three
            c = "blue"
        elif n == 4:
            te = four
            c = "green"
            
        # The message box telling who won
        won = tk.Tk()
        lb = tk.Label(won,text="Turtle Race",fg="brown")
        lb.grid(row=1,column=0)
        lb = tk.Label(won,text=te,fg=c)
        lb.grid(row=2,column=0)
        lb = tk.Label(won,text="Won",fg="green")
        lb.grid(row=2,column=1)
        bt = tk.Button(won,text="Retry")
        bt.grid(row=3,column=0)
        bt2 = tk.Button(won,text="Close")
        bt2.grid(row=3,column=1)
        won.mainloop()
        
# Turtle finish line
def turtle_f(t,n):
    if t.xcor()>149:
        finish(n)
        time.sleep(1000)
    else:
        t.forward(random.randint(1,2))


def turtle_finish():
    h = random.randint(1,4)
    if h == 2:
        turtle_f(turtle1,1)
    if h == 4:
        turtle_f(turtle2,2)
    if h == 1:
        turtle_f(turtle3,3)
    if h == 3:
        turtle_f(turtle4,4)


while True:
    turtle_finish()




