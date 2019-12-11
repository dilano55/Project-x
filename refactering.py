import tkinter as ui
import re
import time
#root window
root = ui.Tk("start")
root.configure(bg="grey")
#canvas voor de hoeveelheid kinderen en bedden
screen = ui.Canvas(root,
width=400, height=150,
bg="grey",bd=0, highlightthickness=0)
screen.pack()
#frame beds
layout_beds = ui.Frame(root,
bg="grey",
width=500,height=500)
#variables
kinderen = 0 #het aantal kinderen
bedden = 0   #het aantal bedden
#text
text = ui.Label(screen,
text="Hoeveel kinderen zijn er?",
font=("arial", 18),
width=20,
bg = "grey")
text1 = ui.Label(screen,
text="Hoeveel bedden zijn er?",
font=("arial", 18),
width=20,
bg= "grey")
text_error = ui.Label(root,
text="Vul aub kloppende waardes in",
bg="red")
#entry's
hvl_kinderen = ui.Entry(screen,
width=3)
hvl_bedden = ui.Entry(screen,
width=3)
#functies(1)
def noteren(): #deze functie zal de waardes die ingevuld zijn aan een variable koppelen
    var = str(hvl_kinderen.get()) #maakt een string van de hoeveelheid die ingevuld is en assigned die aan een variable 
    var_2 = str(hvl_bedden.get()) #maakt een string van de hoeveelheid die ingevuld is en assigned die aan een variable
    if re.match("[1-9]", var) and re.match("[1-9]", var_2): #checkt of de ingevulde waarde wel een cijfer is
        kinderen = hvl_kinderen.get() #geeft kinderen de waarde die daarvoor is ingevuld
        bedden = hvl_bedden.get() #geeft bedden de waarde die daarvoor is ingevuld
        text_error.pack_forget() # zorgt dat wanneer een juist waarde is ingevuld de error message er niet meer is
        time.sleep(0.2)# zorgt voor een kleine delay ( voor effect)
        screen.pack_forget()# haalt het scherm waar je de waardes invult weg
        layout_beds.pack() # zet het scherm voor de layout van de bedden erin
        layout_beds.focus_set()#zet de focus voor keyboard en mouse events op het layout beds frame
    else:
        text_error.pack() #plaatst de error messsage dat er kloppende waardes ingevuld moeten worden
def exit():#een knop die de window sluit
    root.quit()
#widgets
volgende = ui.Button(screen,text="volgende",command=noteren, width=7)
sluit_knop = ui.Button(screen,text="sluiten",command=exit,width=7)
sluit_knop2 = ui.Button(layout_beds,text="sluiten",command=exit,width=7)
#plaatsen
sluit_knop.place(x=185,y=125)
sluit_knop2.place(x=230,y=478)
volgende.place(x=185,y=100)
text.place(x=-5,y=10)
text1.place(x=-10,y=50)
hvl_kinderen.place(x=300,y=20)
hvl_bedden.place(x=300,y=60)
#main loop
root.mainloop()