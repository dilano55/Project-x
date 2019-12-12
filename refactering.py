import tkinter as ui
import re
import time
#root window
root = ui.Tk("start")
root.configure(bg="grey")
root.geometry("+600+400")
#canvas voor de hoeveelheid kinderen en bedden
screen = ui.Canvas(root,
width=400, height=150,
bg="grey",bd=0, highlightthickness=0)
screen.pack()
#frame beds
layout_beds = ui.Frame(root,
bg="grey",
width=500,height=500)
#canvas bed
bed = ui.Canvas(layout_beds,
bg="cyan",
width=20,height=20)
#variables
global kinderen
kinderen = 0 #het aantal kinderen
global bedden 
bedden = 0   #het aantal bedden
locatiex = 200
locatiey = 200
global count
count = 0
global aantal
aantal = 0
global checklist
checklist = []
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
text_error = ui.Label(screen,
text="Vul aub kloppende waardes in",
bg="red")
#entry's
hvl_kinderen = ui.Entry(screen,
width=3, bd=3)
hvl_bedden = ui.Entry(screen,
width=3,bd=3)
#functies(1)
def noteren(): #deze functie zal de waardes die ingevuld zijn aan een variable koppelen
    global kinderen,bedden
    var = str(hvl_kinderen.get()) #maakt een string van de hoeveelheid die ingevuld is en assigned die aan een variable 
    var_2 = str(hvl_bedden.get()) #maakt een string van de hoeveelheid die ingevuld is en assigned die aan een variable
    if re.match("[1-9]", var) and re.match("[1-9]", var_2): #checkt of de ingevulde waarde wel een cijfer is
        kinderen = hvl_kinderen.get() #geeft kinderen de waarde die daarvoor is ingevuld
        bedden = hvl_bedden.get() #geeft bedden de waarde die daarvoor is ingevuld
        text_error.pack_forget() # zorgt dat wanneer een juist waarde is ingevuld de error message er niet meer is
        time.sleep(0.2)# zorgt voor een kleine delay ( voor effect)
        screen.pack_forget()# haalt het scherm waar je de waardes invult weg
        layout_beds.pack() # zet het scherm voor de layout van de bedden erin
        volgende.pack_forget()
        layout_beds.focus_set()#zet de focus voor keyboard en mouse events op het layout beds frame
    else:
        text_error.grid(row=4) #plaatst de error messsage dat er kloppende waardes ingevuld moeten worden
def exit():#een knop die de window sluit
    root.quit()
def click(event):
    global count
    if count < int(bedden):
        var_beds = "bed" + str(count)
        globals()[var_beds].place(x=event.x,y=event.y)
        count += 1
        print("bedden",int(bedden))
        print("count:",count)
        layout_beds.unbind("<Button-1>")

def back():
    global count, aantal
    if count != 0 and aantal !=0:
        print("bedden",int(bedden))
        print("count:",count)
        count -= 1
        aantal -= 1
        print("nieuwe count",count)
        lolol = "bed"+str(count)
        print(lolol)
        globals()[lolol].place_forget()
    else:
        pass
def toevoegen_rechtop():
    global aantal,checklist
    layout_beds.bind("<Button-1>",click)
    if aantal < int(bedden):
        bed_lol = "bed" + str(aantal)
        if bed_lol not in checklist:
            checklist.append(bed_lol)
            globals() [bed_lol] = ui.Canvas(layout_beds,bg="black",width=50,height=100,)
            aantal+=1
        else:
            globals()[bed_lol].configure(width=50,height=100)
            aantal+=1
def toevoegen():
    global aantal,checklist
    layout_beds.bind("<Button-1>",click)
    if aantal < int(bedden):
        bed_lol = "bed" + str(aantal)
        if bed_lol not in checklist:
            checklist.append(bed_lol)
            globals() [bed_lol] = ui.Canvas(layout_beds,bg="black",width=100,height=50,)
            aantal += 1
        else:
            globals()[bed_lol].configure(width=100,height=50)
            aantal += 1    
#widgets
volgende = ui.Button(root,text="volgende",command=noteren, width=7)
sluit_knop = ui.Button(root,text="sluiten",command=exit,width=7)
bed_toevoegen = ui.Button(layout_beds,text="+",command=toevoegen,width=2,height=1)
bed_toevoegen_rechtop = ui.Button(layout_beds,text="+",command=toevoegen_rechtop,width=2,height=1)
stap_terug = ui.Button(layout_beds, text="stap terug",command=back,height=1)
text2 = ui.Label(layout_beds,text="staand",bg="grey")
text3 = ui.Label(layout_beds,text="liggend",bg="grey")
#plaatsen
volgende.pack()
sluit_knop.pack(side='bottom')
text.grid(row=0,sticky="E")
text1.grid(row=1,sticky="E")
hvl_kinderen.grid(row=0,column=1,sticky="E")
hvl_bedden.grid(row=1,column=1,sticky="E")
bed_toevoegen.place(x=10,y=20)
bed_toevoegen_rechtop.place(x=70,y=20)
stap_terug.place(x=430,y=20)
text2.place(x=65,y=5)
text3.place(x=5,y=5)
# stop_knop.place(x=200,y=20)
#binds

#main loop
root.mainloop()