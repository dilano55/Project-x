import tkinter as ui
import re
import time
#window
window = ui.Tk("start")
window.configure(bg="grey")
#canvas
screen = ui.Canvas(window,
width=400, height=150,
bg="grey",bd=0, highlightthickness=0)
screen.pack()
#frame beds
layout_beds = ui.Frame(window,
bg="grey",
width=500,height=500)
#canvas for the button
button_canvas = ui.Canvas(layout_beds,
bg="grey")
#variables
kinderen = 0 #het aantal kinderen
bedden = 0   #het aantal bedden
#text
text = ui.Label(screen,
text="Hoeveel kinderen zijn er?",
font=("arial", 20),
width=15,
bg = "grey")
text1 = ui.Label(screen,
text="Hoeveel bedden zijn er?",
font=("arial", 20),
width=15,
bg= "grey")
text_error = ui.Label(window,
text="Vul aub kloppende waardes in",
bg="red")
text_error1 = ui.Label(window,
text="Vul waardes groter dan 0 in",
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
    if re.match("[0-9]", var) and re.match("[0-9]", var_2): #checkt of de ingevulde waarde wel een cijfer is
        kinderen = hvl_kinderen.get() #geeft kinderen de waarde die daarvoor is ingevuld
        bedden = hvl_bedden.get() #geeft bedden de waarde die daarvoor is ingevuld
        text_error.pack_forget() # zorgt dat wanneer een juist waarde is ingevuld de error message er niet meer is
        text_error1.pack_forget()# zorgt dat wanneer een juiste waard is ingevuld de error message er niet meer is
        time.sleep(0.2)# zorgt voor een kleine delay ( voor effect)
        screen.pack_forget()# haalt het scherm waar je de waardes invult weg
        layout_beds.pack() # zet het scherm voor de layout van de bedden erin
        button_canvas.place(x=250,y=250)#plaatst het canvas voor de knop om een bed te plaatsen. de bedoeling is dat dit canvas gaat verplaatsen en niet het knopje
        layout_beds.focus_set()#zet de focus voor keyboard en mouse events op het layout beds frame
        if int(hvl_bedden) > 0 and int(hvl_kinderen) > 0:#checkt of de waarde die ingevuld zijn groter dan 0 zijn
            print(hvl_bedden,".",hvl_kinderen) # als dit zo is print het ter controle de waardes
        elif int(hvl_bedden) <= 0 or int(hvl_kinderen) <= 0: #kijkt of de ingevulde waardes kleiner dan 0 zijn
            text_error.pack_forget()#zorgt dat de andere error er niet is
            text_error1.pack() #plaatst de error message dat de waarde groter dan 0 moet zijn
    else:
        text_error1.pack_forget() #zorgt dat de andere error message er niet is
        text_error.pack() #plaatst het de error messsage dat er kloppende waardes ingevuld moeten worden


        