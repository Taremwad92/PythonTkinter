from tkinter import *
window = Tk()
#set calculator size
window.geometry("460x435")
#set calculator background colour
window.config(background ="grey")
#set calculator title
window.title("DUNCANCALC")
#the calculator window shouldnt be maximisable
window.resizable(0,0)
# equation is a string variable to screen display
equation = StringVar()
#this will be shown when you switch your computer on
equation.set("cos0 = 1, sin0 = 0")
expres = "" # this varible stores string entered from the user
total = "" # this variable stores the result of evaluation
# when a number or operator is pressed, this function is called
def pres(num):
    global total
    global expres

    if equation.get() != total:
        expres = expres + str(num)
        equation.set(expres)
    elif num in "*,-,+,/" and equation.get() == total:
        expres = total + str(num)
        equation.set(expres)
    else:
        expres = num
        equation.set(num)
#when equal sign is pressed call this function
def equalpres():
    global total
    global expres
    #check whether the last string character is an operator
    if expres[-1].isdigit():
        try:
            total = str(eval(expres))
            equation.set(total)
            expres = total
        except:
             equation.set("Error")
             expres = ""
    else:
        # if yes remove it from the expression
        expres= expres[:-1]

        try:
            total = str(eval(expres))
            equation.set(total)
            expres = total
        except:
             equation.set("Error")
             expres = ""

#this function clears the screen
def clear():
    global expres
    expres = ""
    equation.set("")
# this function is called when delete button is pressed
def deletbutton():
    global expres
    global total
    if equation.get() == total:
        equation.set("")
    else:
        newexpres = expres[:-1]
        expres = newexpres
        equation.set(newexpres)
#create the screen using the entry widget
displayText = Entry(window,state ="disabled",textvariable = equation,foreground ="yellow", font = "times 16 bold",background = "blue",relief = SUNKEN, bd = 10,width =33).grid(padx = 25,pady = 10,columnspan =30)
#create the buttons
button1 = Button(window,text ="1",relief = RAISED,bd = 10,foreground = "green",background = "purple",activebackground = "yellow",width = 5, font = "times 18 bold italic",command = lambda: pres("1")).grid(padx =5, pady = 5,row =1,column =0)
button2 = Button(window,text ="2",relief = RAISED,bd = 10,foreground = "green",activebackground = "yellow",width = 5, font = "times 18 bold italic",command = lambda: pres("2")).grid(padx =2, pady = 3,row =2,column =0)
button3 = Button(window,text ="3",relief = RAISED,bd = 10,foreground = "green",background = "black",activebackground = "yellow",width = 5, font = "times 18 bold italic",command = lambda: pres("3")).grid(padx =2, pady = 3,row =3,column =0)
button0 = Button(window,text ="0",relief = RAISED,bd = 10,foreground = "green",activebackground = "yellow",width = 5, font = "times 18 bold italic",command = lambda: pres("0")).grid(padx =2, pady = 3,row =5,column =0)
button5 = Button(window,text ="5",relief = RAISED,bd = 10,foreground = "green",activebackground = "yellow",width = 10, font = "times 18 bold italic",command = lambda: pres("5")).grid(padx =2, pady = 3,row =4,column =2)
button6 = Button(window,text ="6",relief = RAISED,bd = 10,background ="purple",foreground = "green",activebackground = "yellow",width = 10, font = "times 18 bold italic",command = lambda: pres("6")).grid(padx =2, pady = 3,row =3,column =2)
button7 = Button(window,text ="7",relief = RAISED,bd = 10,background ="blue",foreground = "green",activebackground = "yellow",width = 10, font = "times 18 bold italic",command = lambda: pres("7")).grid(padx =2, pady = 3,row =2,column =2)
button8 = Button(window,text ="8",relief = RAISED,bd = 10,foreground = "green",activebackground = "yellow",width = 10, font = "times 18 bold italic",command = lambda: pres("8")).grid(padx =2, pady = 3,row =1,column =2)
button9 = Button(window,text ="9",relief = RAISED,bd = 10,background ="black",foreground = "green",activebackground = "yellow",width = 10, font = "times 18 bold italic",command = lambda: pres("9")).grid(padx =2, pady = 3,row =1,column =3,columnspan =2)
buttonplus = Button(window,text ="+",relief = RAISED,bd = 10,foreground = "green",activebackground = "yellow",width = 4, font = "times 18 bold italic",command = lambda: pres("+")).grid(padx =2, pady = 3,row =2,column =3)
buttonminus = Button(window,text ="-",relief = RAISED,bd = 10,background ="purple",foreground = "green",activebackground = "yellow",width = 4, font = "times 18 bold italic",command = lambda: pres("-")).grid(padx =2, pady = 3,row =2,column =4)
buttonmulti = Button(window,text ="*",relief = RAISED,bd = 10,background ="blue",foreground = "green",activebackground = "yellow",width = 4, font = "times 18 bold italic",command = lambda: pres("*")).grid(padx =2, pady = 3,row =3,column =4)
buttondiv = Button(window,text ="/",relief = RAISED,bd = 10,foreground = "green",activebackground = "yellow",width = 4, font = "times 18 bold italic",command = lambda: pres("/")).grid(padx =2, pady = 3,row =3,column =3)
buttonpoint = Button(window,text =".",relief = RAISED,bd = 10,background ="black",foreground = "green",activebackground = "yellow",width = 4, font = "times 18 bold italic",command = lambda: pres(".")).grid(padx =2, pady = 3,row =4,column =3)
buttondel = Button(window,text ="DEL",relief = RAISED,bd = 10,foreground = "green",activebackground = "yellow",width = 4, font = "times 18 bold italic",command = lambda: deletbutton()).grid(padx =2, pady = 3,row =4,column =4)
buttonequal = Button(window,text ="=",relief = RAISED,bd = 10,background ="blue",foreground = "green",activebackground = "yellow",width = 10, font = "times 18 bold italic",command = lambda: equalpres()).grid(padx =2, pady =3,row =5,column =2)
button4 = Button(window,text ="4",relief = RAISED,bd = 10,foreground = "green",background ="blue",activebackground = "yellow",width = 5, font = "times 18 bold italic",command = lambda: pres("4")).grid(padx =2, pady = 3,column =0,row =4)
buttonclear = Button(window,text ="AC",relief = RAISED,bd = 10,foreground = "green",background = "grey",activebackground = "yellow",width = 10, font = "times 18 bold italic",command = lambda: clear()).grid(padx =2, pady = 3,row =5,column =3,columnspan =2)



window.mainloop()