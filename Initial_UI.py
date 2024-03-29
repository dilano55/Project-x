import tkinter as ui
import re
import time
# window settings_START
window = ui.Tk()
window.title("Start")
window.configure(bg="grey")
screen = ui.Canvas(window, width=400, height=150,bg="grey", bd=0, highlightthickness=0)
screen.pack()
#CANVAS LAYOUT
layout_beds = ui.Frame(window,bg="grey",width = 500, height = 500)
button_canvas = ui.Canvas(layout_beds,bg="grey")
# variables:_START
varx= 20
vary= 40
amount_kids = 0
amount_beds = 0
movement = False
x = window.winfo_pointerx()
y = window.winfo_pointery()
# widgets_1_START
text2 = ui.Label(screen, text='Amount of children?',font=("arial", 20), width=15, bg="grey")
text3 = ui.Label(screen, text='Amount of beds?', font=("arial", 20), width=15, bg="grey")
amount_of_children = ui.Entry(screen, width=3)
amount_of_beds = ui.Entry(screen, width=3)
text_error = ui.Label(window, text="Please enter valid values", bg="red")
text_error_2 = ui.Label(window, text="Please enter values greater than 0", bg="red")
# functions_2_START
def note():
    var = str(amount_of_children.get())
    var_2 = str(amount_of_children.get())
    if re.match("[0-9]", var) and re.match("[0-9]", var_2):
        amount_beds = amount_of_beds.get()
        amount_kids = amount_of_children.get()
        text_error_2.pack_forget()
        text_error.pack_forget()
        time.sleep(0.3)
        screen.pack_forget()
        layout_beds.pack()
        button_canvas.place(x=50,y=50)
        layout_beds.focus_set()
        
        if int(amount_beds) > 0 and int(amount_kids) > 0:
            print(amount_kids, amount_beds)
        elif int(amount_beds) <= 0 or int(amount_kids) <= 0:
            text_error.pack_forget()
            text_error_2.pack()
            print("error values must be greater then 0")
    else:
        print("please enter valid values")
        text_error_2.pack_forget()
        text_error.pack()
def mouseclick(event):
    global x,y
    x = event.x
    y = event.y
    return True
def exit():
    window.quit()
def move_it():
    # varx = window.winfo_pointerx() - window.winfo_rootx()
    # vary = window.winfo_pointery() - window.winfo_rooty()
    bed_test.pack_forget()
    button_canvas.place_forget()
    if mouseclick:
        print("clicked")
        bed_test.pack()
        button_canvas.place(x=(x+10),y=(y+10))


    
#BINDS
layout_beds.bind("<Key>",mouseclick)
# button_canvas.bind("<Key>",mouseclick)



# widgets_2_START(quit and confirm buttons, and more)
confirm_button = ui.Button(screen, text="Confirm", command=note, width=6)
quit_button = ui.Button(screen, text="Quit", command=exit, width=6)
quit_button2 = ui.Button(layout_beds, text="Quit", command=exit, width=6)
bed_test = ui.Button(button_canvas,text="bed",bg="cyan",command=move_it)
# placements_START
bed_test.pack()
quit_button2.place(x=230,y=478)
quit_button.place(x=185, y=125)
confirm_button.place(x=185, y=100)
text2.place(y=10, x=4)
text3.place(y=50, x=4)
amount_of_children.place(y=20, x=300)
amount_of_beds.place(y=60, x=300)
# window1_START
ui.mainloop()
