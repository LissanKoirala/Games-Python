# Creator : Lissan Koirala
# Date of Creation : 18/10/2019

import tkinter as tk
import os
import random
#variables
HEIGHT=20
WIDTH=150
email=""
password=""
turn=1
num=0 
###############################
###############################
###############################
#define quiz
def quizdef():
    #global num
    #global num1
    #DEFINE THE ANSWER
    #DEFINE THE ANSWERS:
    
    def ans1s():
        ans = tk.Button(window2, text="1.RUSSIA", bg="red", fg="black")
        ans.pack()
        #num1=num1-1
    def ans2s():
        ans2 = tk.Button(window2, text="2.ITALY", bg="red", fg="black")
        ans2.pack()
        #num1=num1-1
    def ans3s():
        ans3 = tk.Button(window2, text="3.AUSTRIA", bg="green", fg="black")
        ans3.pack()
        window3()
        #num=num+1
    def ans4s():
        ans4 = tk.Button(window2, text="4.SPAIN", bg="red", fg="black")
        ans4.pack()
        #num1=num1-1
        
###############################
###############################
###############################

    window2 = tk.Tk()

    #canvas height ra width kati bhanera...
    canvas = tk.Canvas(window2, height=30, width=100)
    canvas.pack()
##################################################################
##################################################################
##################################################################
    #label
    label3 = tk.Label(window2, text="WHAT IS THE NATURALITY OF HITLER ?", bg='white')
    label3.pack()

    #Keeping the button....
    ans = tk.Button(window2, text="1.RUSSIA", bg="white", fg="black", command=ans1s)
    ans.pack()
    ans2 = tk.Button(window2, text="2.ITALY", bg="white", fg="black", command=ans2s)
    ans2.pack()
    ans3 = tk.Button(window2, text="3.AUSTRIA", bg="white", fg="black" ,command=ans3s)
    ans3.pack()
    ans4 = tk.Button(window2, text="4.SPAIN", bg="white", fg="black" ,command=ans4s)
    ans4.pack()

    window2.mainloop() 
##################################################################
##################################################################
##################################################################
def window3():
    #defining the answers
    def ans1s():
        ans = tk.Button(window3, text="1.LISSAN KOIRALA", bg="red", fg="black")
        ans.pack()
        #num1=num1-1
    def ans2s():
        ans2 = tk.Button(window3, text="2.LUIS GUERRA",bg="red", fg="black")
        ans2.pack()
        #num1=num1-1
    def ans3s():
        ans3 = tk.Button(window3, text="3.MARCELO REBELO DA SOUSA",bg="green", fg="black")
        ans3.pack()
        
        #num=num+1
    def ans4s():
        ans4 = tk.Button(window3, text="4.ANTÓNIO COSTA",bg="red", fg="black")
        ans4.pack()
        #num1=num1-1
    
    window3 = tk.Tk()
    #label

    label3 = tk.Label(window3, text="WHO IS THE PRESIDENT OF PORTUGAL ?", bg='white')
    label3.pack()

    #Keeping the button....
    ans = tk.Button(window3, text="1.LISSAN KOIRALA", bg="white", fg="black", command=ans1s)
    ans.pack()
    ans2 = tk.Button(window3, text="2.LUIS GUERRA", bg="white", fg="black", command=ans2s)
    ans2.pack()
    ans3 = tk.Button(window3, text="3.MARCELO REBELO DA SOUSA", bg="white", fg="black" ,command=ans3s)
    ans3.pack()
    ans4 = tk.Button(window3, text="4.ANTÓNIO COSTA", bg="white", fg="black" ,command=ans4s)
    ans4.pack()

    window3.mainloop()

##################################################################
##################################################################
##################################################################
def lotdef():
    def rand():
        x=random.randint(1,5)
        if one["text"]==x:
            won = tk.Button(window4, text="YOU WON", bg="green", fg="white")
            won.pack()
        elif two["text"]==x:
            won = tk.Button(window4, text="YOU WON", bg="green", fg="white")
            won.pack()
        elif three["text"]==x:
            won = tk.Button(window4, text="YOU WON", bg="green", fg="white")
            won.pack()
        elif four["text"]==x:
            won = tk.Button(window4, text="YOU WON", bg="green", fg="white")
            won.pack()
        elif five["text"]==x:
            won = tk.Button(window4, text="YOU WON", bg="green", fg="white")
            won.pack()
        else:
            won = tk.Button(window4, text="YOU LOSE", bg="red", fg="white")
            won.pack()            
        
        
        
    window4 = tk.Tk()
    label = tk.Label(window4, text="CHOOSE A NUMBER:", bg="white", fg="black")
    label.pack()
    one = tk.Button(window4, text="1", bg="white" , fg="black", command=rand)
    one.pack()
    two = tk.Button(window4, text="2", bg="white" , fg="black", command=rand)
    two.pack()
    three = tk.Button(window4, text="3", bg="white" , fg="black", command=rand)
    three.pack()
    four = tk.Button(window4, text="4", bg="white" , fg="black", command=rand)
    four.pack()
    five = tk.Button(window4, text="5", bg="white" , fg="black",command=rand)
    five.pack()

def signup():
    entry["text"]=email
    entry1["text"]=password
    
    def cou():
        os.system("cstrike.exe")

    def ticdef():
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
                
    
    #CREATING TK
    window1 = tk.Tk()

    #canvas height ra width kati bhanera...
    canvas = tk.Canvas(window1, height=20, width=100)
    canvas.pack()

    #label
    label3 = tk.Label(window1, text="CHOOSE WHAT YOU WANNA PLAY:", bg='white')
    label3.pack()

    #Keeping the button....
    quiz = tk.Button(window1, text="1.QUIZ", bg="white", fg="black", command=quizdef)
    quiz.pack()
    lot = tk.Button(window1, text="2-EURO BILLION  -« LOW CHANCE, CHEAP TICKETS »-", bg="white", fg="black", command=lotdef)
    lot.pack()
    tictac = tk.Button(window1, text="3.TIC TAC TOE", bg="white", fg="black", command=ticdef)
    tictac.pack()
    counter = tk.Button(window1, text="4.Counter Strike", bg="white", fg="black", command=cou)
    counter.pack()
    window1.mainloop()
    ##########
    ######## REAL TK
    ##########
    
###############################
###############################
###############################
#CREATING TK
window = tk.Tk()

#canvas height ra width kati bhanera...
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

#label
label = tk.Label(window, text="Email                             ", bg='white')
label.pack()

#text box
entry = tk.Entry(window, bg='white')
entry.pack()

#label
label1 = tk.Label(window, text="Password                      ", bg='white')
label1.pack()

#text box
entry1 = tk.Entry(window, bg='white')
entry1.pack()


#Keeping the button....
signup = tk.Button(window, text="LOGIN", bg="white", fg="black", command=signup)
signup.pack()

window.mainloop()
