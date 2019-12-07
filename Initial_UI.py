import tkinter as ui
import re
import time
# window settings_START
window = ui.Tk()
window.title("Start")
window.configure(bg="grey")
screen = ui.Canvas(window, width=400, height=150,bg="grey", bd=0, highlightthickness=0)
screen.pack()
# variables:_START
amount_kids = 0
amount_beds = 0
# widgets_1_START
text2 = ui.Label(screen, text='Amount of children?',font=("arial", 20), width=15, bg="grey")
text3 = ui.Label(screen, text='Amount of beds?', font=("arial", 20), width=15, bg="grey")
amount_of_children = ui.Entry(screen, width=3)
amount_of_beds = ui.Entry(screen, width=3)
text_error = ui.Label(window, text="Please enter valid values", bg="red")
text_error_2 = ui.Label(window, text="Please enter values greater than 0", bg="red")

#CANVAS LAYOUT
layout_beds = ui.Frame(window,bg="grey",width = 500, height = 500)
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


def exit():
    window.quit()


# widgets_2_START(quit and confirm buttons)
confirm_button = ui.Button(screen, text="Confirm", command=note, width=6)
quit_button = ui.Button(screen, text="Quit", command=exit, width=6)
quit_button2 = ui.Button(layout_beds, text="Quit", command=exit, width=6)
# placements_START
quit_button2.place(x=230,y=478)
quit_button.place(x=185, y=125)
confirm_button.place(x=185, y=100)
text2.place(y=10, x=4)
text3.place(y=50, x=4)
amount_of_children.place(y=20, x=300)
amount_of_beds.place(y=60, x=300)
# window1_START
ui.mainloop()
