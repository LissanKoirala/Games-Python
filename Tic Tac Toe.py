# Creator : Lissan Koirala
# Date of Creation : 29/01/2020

import tkinter as tk
import random
import os
from tkinter import messagebox
HEIGHT=100
WIDTH=200
con="Congrats"
#clash the window

def clash():
    ans = "Game Complete"
    messagebox.showinfo(con , who)
    root.destroy()
    
#########################################################################################
#########################################################################################
def check():
    global who
    if button["text"]==button1["text"]:
        if button1["text"]==button2["text"]:
            if button2["text"]==" X ":
                who="Lissan"
                clash()
    elif button3["text"]==button4["text"]:
        if button4["text"]==button5["text"]:
            if button5["text"]==" X ":
                who="Lissan"
                clash()
    elif button6["text"]==button7["text"]:
        if button7["text"]==button8["text"]:
            if button8["text"]==" X ":
                who="Lissan"
                clash()
    elif button["text"]==button3["text"]:
        if button3["text"]==button6["text"]:
            if button6["text"]==" X ":
                who="Lissan"
                clash()
    elif button1["text"]==button4["text"]:
        if button4["text"]==button7["text"]:
            if button7["text"]==" X ":
                who="Lissan"
                clash()
    elif button2["text"]==button5["text"]:
        if button5["text"]==button8["text"]:
            if button8["text"]==" X ":
                who="Lissan"
                clash()
    elif button["text"]==button4["text"]:
        if button4["text"]==button8["text"]:
            if button5["text"]==" X ":
                who="Lissan"
                clash()
    elif button2["text"]==button4["text"]:
        if button4["text"]==button6["text"]:
            if button6["text"]==" X ":
                who="Lissan"
                clash()
    ##############################################################
    if button["text"]==button1["text"]:
        if button1["text"]==button2["text"]:
            if button2["text"]==" 0 ":
                who="0"
                clash()
    if button3["text"]==button4["text"]:
        if button4["text"]==button5["text"]:
            if button5["text"]==" 0 ":
                who="0"
                clash()
    if button6["text"]==button7["text"]:
        if button7["text"]==button8["text"]:
            if button8["text"]==" 0 ":
                who="0"
                clash()
    if button["text"]==button3["text"]:
        if button3["text"]==button6["text"]:
            if button6==["text"]==" 0 ":
                who="0"
                clash()
    if button1["text"]==button4["text"]:
        if button4["text"]==button7["text"]:
            if button7==["text"]==" 0 ":
                who="0"
                clash()
    if button2["text"]==button5["text"]:
        if button5["text"]==button8["text"]:
            if button8==["text"]==" 0 ":
                who="0"
                clash()
    if button["text"]==button4["text"]:
        if button4["text"]==button8["text"]:
            if button5==["text"]==" 0 ":
                who="0"
                clash()
    if button2["text"]==button4["text"]:
        if button4["text"]==button6["text"]:
            if button6==["text"]==" 0 ":
                who="0"
                clash()


num=0       
    
#########################################################################################
turn=1
def first():
    global num
    global turn
    if button["text"]=="---":
        if turn==1:
            turn=2
            button["text"]=" X "
            num=num+1
        elif turn==2:
            turn=1
            button["text"]=" 0 "
            num=num+1
    check()
def second():
    global num
    global turn
    if button1["text"]=="---":
        if turn==1:
            turn=2
            button1["text"]=" X "
            num=num+1
        elif turn==2:
            turn=1
            button1["text"]=" 0 "
            num=num+1
    check()
def third():
    global num
    global turn
    if button2["text"]=="---":
        if turn==1:
            turn=2
            button2["text"]=" X "
            num=num+1
        elif turn==2:
            turn=1
            button2["text"]=" 0 "
            num=num+1
    check()
def fourth():
    global num
    global turn
    if button3["text"]=="---":
        if turn==1:
            turn=2
            button3["text"]=" X "
            num=num+1
        elif turn==2:
            turn=1
            button3["text"]=" 0 "
            num=num+1
    check()
def fifth():
    global num
    global turn
    if button4["text"]=="---":
        if turn==1:
            turn=2
            button4["text"]=" X "
            num=num+1
        elif turn==2:
            turn=1
            button4["text"]=" 0 "
            num=num+1
    check()
def sixth():
    global num
    global turn
    if button5["text"]=="---":
        if turn==1:
            turn=2
            button5["text"]=" X "
            num=num+1
        elif turn==2:
            turn=1
            button5["text"]=" 0 "
            num=num+1
    check()
def seven():
    global num
    global turn
    if button6["text"]=="---":
        if turn==1:
            turn=2
            button6["text"]=" X "
            num=num+1
        elif turn==2:
            turn=1
            button6["text"]=" 0 "
            num=num+1
    check()
def eight():
    global num
    global turn
    if button7["text"]=="---":
        if turn==1:
            turn=2
            button7["text"]=" X "
            num=num+1
        elif turn==2:
            turn=1
            button7["text"]=" 0 "
            num=num+1
    check()
def nine():
    global num
    global turn
    if button8["text"]=="---":
        if turn==1:
            turn=2
            button8["text"]=" X "
            num=num+1
        elif turn==2:
            turn=1
            button8["text"]=" 0 "
            num=num+1
    check()

#########################################################################################
#########################################################################################
#########################################################################################    
    
    
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relx=0.1, rely=0.1, relwidth=0.99, relheight=0.99)

#kepping the button on frame    1
button = tk.Button(frame, text="---" , bg='black' , fg='white', command=first)
button.grid(row=0, column=0)
################################
#keeping another button     2
button1 = tk.Button(frame, text="---" , bg='black' , fg='white', command=second)
button1.grid(row=0, column=1)
################################
#keeping another button        3
button2 = tk.Button(frame, text="---" , bg='black' , fg='white', command=third)
button2.grid(row=0, column=2)
################################
#keeping another button      4
button3 = tk.Button(frame, text="---" , bg='black' , fg='white', command=fourth)
button3.grid(row=1, column=0)
################################
#keeping another button     5
button4 = tk.Button(frame, text="---" , bg='black' , fg='white', command=fifth)
button4.grid(row=1, column=1)
################################
#keeping another button         6
button5 = tk.Button(frame, text="---" , bg='black' , fg='white', command=sixth)
button5.grid(row=1, column=2)
################################
#keeping another button      7
button6 = tk.Button(frame, text="---" , bg='black' , fg='white', command=seven)
button6.grid(row=2, column=0)
################################
#keeping another button            8
button7 = tk.Button(frame, text="---" , bg='black' , fg='white', command=eight)
button7.grid(row=2, column=1)
################################
#keeping another button        9
button8 = tk.Button(frame, text="---" , bg='black' , fg='white', command=nine)
button8.grid(row=2, column=2)
################################


#label

label1 = tk.Label(root, text="TIC TAC TOE", bg='white', fg='black')
label1.pack()

label = tk.Label(root, text="1ºPlayer:", bg='#ff0000')
label.pack()

#entry we can write Lissan Koirala

entry = tk.Entry(root, bg='white')
entry.pack()
###
#label2 = tk.Label(root, text="2ºPlayer:", bg='#ff0000')
#label2.pack()

#entry we can write Lissan Koirala

#entry1 = tk.Entry(root, bg='white')
#entry1.pack()

#Submit
  
submit = tk.Button(root, text="SUBMIT", bg='white', fg='black')
submit.pack()
    
root.mainloop()
