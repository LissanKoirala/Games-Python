# Creator : Lissan Koirala
# Date of Creation : 27/11/2019

# Importing all the libraries that is needed
import tkinter as tk
import random
from tkinter import messagebox
import os

# Defining the wins
def win():
    if n1["text"]=="N":
        if n2["text"]=="E":
            if n3["text"]=="P":
                if n4["text"]=="A":
                    if n5["text"]=="L":
                            window.destroy()

# Creating a Window with all the things
window = tk.Tk()

canvas = tk.Canvas(window, height=200, width=300)
canvas.pack()

frame = tk.Frame(window, bg='white')
frame.place(height=300, width=400)

label = tk.Label(window, text="HANGING MAN", bg="red", fg="white")
label.pack()

ans1="NEPAL"

# Defining the images thats pops up when you make a mistake
turn=1
def ifn():
    global turn
    if turn == 1:
        os.system("1.png")
        turn = 2
    elif turn == 2:
        os.system("2.png")
        turn = 3
    elif turn == 3:
        os.system("3.png")
        turn = 4
    elif turn == 4:
        os.system("4.png")
        turn = 5
    elif turn == 5:
        os.system("5.png")
        turn = 6
    elif turn == 6:
        os.system("6.png")
        window.destroy()
        
          

# Defining that the button becomes green when the answer is correct
def n():
    if ans1=="NEPAL":
        n1=tk.Button(frame, text="N")
        n1.grid(row=30, column=5)
        bt14=tk.Button(frame, text=" N ", bg="green", command=n)
        bt14.grid(row=42, column=11)
    win()
def e():
    if ans1=="NEPAL":
        n2=tk.Button(frame, text="E")
        n2.grid(row=30, column=6)
        bt5=tk.Button(frame, text=" E ", bg="green", command=e)
        bt5.grid(row=40, column=14)
    win()
def p():
    if ans1=="NEPAL":
        n3=tk.Button(frame, text="P")
        n3.grid(row=30, column=7)
        bt16=tk.Button(frame, text=" P ", bg="green", command=p)
        bt16.grid(row=42, column=13)
    win()
def ah():
    if ans1=="NEPAL":
        n4=tk.Button(frame, text="A")
        n4.grid(row=30, column=8)
        bt1=tk.Button(frame, text=" A ", bg="green",  command=ah)
        bt1.grid(row=40, column=10)
    win()
def l():
    if ans1=="NEPAL":
        n5=tk.Button(frame, text="L")
        n5.grid(row=30, column=9)
        bt12=tk.Button(frame, text=" L ", bg="green", command=l)
        bt12.grid(row=41, column=15)
    win()

                        

                        

a="-"
n1=tk.Button(frame, text=a)
n1.grid(row=30, column=5)
n2=tk.Button(frame, text=a)
n2.grid(row=30, column=6)
n3=tk.Button(frame, text=a)
n3.grid(row=30, column=7)
n4=tk.Button(frame, text=a)
n4.grid(row=30, column=8)
n5=tk.Button(frame, text=a)
n5.grid(row=30, column=9)


label = tk.Label(window, text="------------------------------------")
label.pack()


# Making all the buttons for the user to choose
bt1=tk.Button(frame, text=" A ", command=ah)
bt1.grid(row=40, column=10)
bt2=tk.Button(frame, text=" B ", command=ifn)
bt2.grid(row=40, column=11)
bt3=tk.Button(frame, text=" C ", command=ifn)
bt3.grid(row=40, column=12)
bt4=tk.Button(frame, text=" D ", command=ifn)
bt4.grid(row=40, column=13)
bt5=tk.Button(frame, text=" E ", command=e)
bt5.grid(row=40, column=14)
bt6=tk.Button(frame, text=" F ", command=ifn)
bt6.grid(row=40, column=15)
bt7=tk.Button(frame, text=" G ", command=ifn)
bt7.grid(row=41, column=10)
bt8=tk.Button(frame, text=" H ", command=ifn)
bt8.grid(row=41, column=11)
bt9=tk.Button(frame, text="  I ", command=ifn)
bt9.grid(row=41, column=12)
bt10=tk.Button(frame, text="  J ", command=ifn)
bt10.grid(row=41, column=13)
bt11=tk.Button(frame, text=" K ", command=ifn)
bt11.grid(row=41, column=14)
bt12=tk.Button(frame, text=" L ", command=l)
bt12.grid(row=41, column=15)
bt13=tk.Button(frame, text=" M ", command=ifn)
bt13.grid(row=42, column=10)
bt14=tk.Button(frame, text=" N ",command=n)
bt14.grid(row=42, column=11)
bt15=tk.Button(frame, text=" O ", command=ifn)
bt15.grid(row=42, column=12)
bt16=tk.Button(frame, text=" P ", command=p)
bt16.grid(row=42, column=13)
bt17=tk.Button(frame, text=" Q ", command=ifn)
bt17.grid(row=42, column=14)
bt18=tk.Button(frame, text=" R ", command=ifn)
bt18.grid(row=42, column=15)
bt19=tk.Button(frame, text=" S ", command=ifn)
bt19.grid(row=43, column=10)
bt20=tk.Button(frame, text=" T ", command=ifn)
bt20.grid(row=43, column=11)
bt21=tk.Button(frame, text=" U ", command=ifn)
bt21.grid(row=43, column=12)
bt22=tk.Button(frame, text=" V ", command=ifn)
bt22.grid(row=43, column=13)
bt23=tk.Button(frame, text=" W ", command=ifn)
bt23.grid(row=43, column=14)
bt24=tk.Button(frame, text=" X ", command=ifn)
bt24.grid(row=43, column=15)
bt25=tk.Button(frame, text=" Y ", command=ifn)
bt25.grid(row=44, column=12)
bt26=tk.Button(frame, text=" Z ", command=ifn)
bt26.grid(row=44, column=13)

window.mainloop()




