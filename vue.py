 
from tkinter import * 

fenetre = Tk()

#########################################
# identifiant

id = Frame(fenetre)
id.pack(side=LEFT, padx=30, pady=30)

# Ajout de labels
Label(id, text="n° identifiant: ").pack(padx=10, pady=10)

e = Entry(fenetre, width=30)
e.pack(side=LEFT, padx=10, pady=10)


#########################################
# identifiant

mdp = Frame(fenetre)
mdp.pack(side=LEFT, padx=30, pady=30)

# Ajout de labels
Label(mdp, text="mot de passe: ").pack(padx=10, pady=10)

e = Entry(fenetre, width=30)
e.pack(side=LEFT, padx=10, pady=10)



def myClick():
        hello = "Hello " + e.get()
        myLabel = Label(fenetre, text=hello)
        myLabel.pack(side=LEFT, padx=10, pady=10)

myButton = Button(fenetre, text="Valider", command=myClick)
myButton.pack(side=LEFT, padx=10, pady=10)




fenetre.mainloop()
