 
from tkinter import * 

fenetre = Tk()

fenetre.geometry("350x270+300+200")
nb1 = ""


#########################################
# identifiant

cadre1 = LabelFrame(fenetre)
cadre1.pack(padx=5, pady=5)

etiquette1 = Label(cadre1, text='n° identifiant: ')
etiquette1.pack(padx=5, pady=5, side=LEFT)

valueId = StringVar()
valueId.set("")
entree1 = Entry(cadre1, textvariable=valueId)
entree1.pack(padx=5, pady=5, side=LEFT)

#########################################
# mdp
cadre2=LabelFrame(fenetre)
cadre2.pack(padx=5, pady=5)

etiquette2 = Label(cadre2, text='mot de passe: ')
etiquette2.pack(padx=5, pady=5, side=LEFT)

value = StringVar()
value.set(nb1)
entree2 = Entry(cadre2, show="*", textvariable=value)
entree2.pack(padx=5, pady=5, side=LEFT)

#########################################
# paveNum

def ajout(nb):
    global nb1
    nb1 += nb
    value.set(nb1)

def num1():
    ajout("1")

def num2():
    ajout("2")

def num3():
    ajout('3')

def num4():
    ajout("4")

def num5():
    ajout("5")

def num6():
    ajout("6")

def num7():
    ajout("7")

def num8():
    ajout("8")

def num9():
    ajout("9")

def zero():
    ajout("0")

def clear():
    global nb1,nb2
    nb1 = ""
    nb2 = ""
    value.set("")

def valid():
    hello = "Hello " + entree1.get()
    myLabel = Label(fenetre, text=hello)
    myLabel.pack(side=LEFT, padx=10, pady=10)


# label = Label(fenetre,text="")
# label.place(x=10,y=10)
button = Button(fenetre,text="  5  ",command=num5).place(x=100,y=110)
button = Button(fenetre,text="  8  ",command=num8).place(x=160,y=110)
button = Button(fenetre,text="  2  ",command=num2).place(x=220,y=110)
button = Button(fenetre,text="  0  ",command=zero).place(x=100,y=150)
button = Button(fenetre,text="  1  ",command=num1).place(x=160,y=150)
button = Button(fenetre,text="  3  ",command=num3).place(x=220,y=150)
button = Button(fenetre,text="  6  ",command=num6).place(x=100,y=190)
button = Button(fenetre,text="  4  ",command=num4).place(x=160,y=190)
button = Button(fenetre,text="  9  ",command=num9).place(x=220,y=190)
button = Button(fenetre,text="  X  ",command=clear).place(x=100,y=230)
button = Button(fenetre,text="  7  ",command=num7).place(x=160,y=230)
button = Button(fenetre,text="  V  ",command=valid).place(x=220,y=230)

########################################

fenetre.mainloop()