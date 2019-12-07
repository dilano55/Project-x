import tkinter as ui
import re
import time
# window settings_START
x = "ok"
window = ui.Tk()
window.title("Start")
window.configure(bg="black")
screen = ui.Canvas(window, width=400, height=150,
                   bg="black", bd=0, highlightthickness=0)
screen.pack()
# second window settings
window_2 = ui.Tk()
window_2.title("Layout")
window_2.geometry("400x400")
window_2.configure(bg="black")
# variables:_START
amount_kids = 0
amount_beds = 0
# widgets_1_START
text2 = ui.Label(screen, text='Amount of children?', fg="white",
                 bg="black", font=("arial", 20), width=15)
text3 = ui.Label(screen, text='Amount of beds?', fg="white",
                 bg="black", font=("arial", 20), width=15)
amount_of_children = ui.Entry(screen, width=3)
amount_of_beds = ui.Entry(screen, width=3)
text_error = ui.Label(window, text="Please enter valid values", bg="red")
text_error_2 = ui.Label(
    window, text="Please enter values greater than 0", bg="red")
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
        window.destroy()
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


# widgets_2_START
confirm_button = ui.Button(screen, text="Confirm", command=note, width=6)
quit_button = ui.Button(screen, text="Quit", command=exit, width=6)
# placements_START
quit_button.place(x=185, y=125)
confirm_button.place(x=185, y=100)
text2.place(y=10, x=4)
text3.place(y=50, x=4)
amount_of_children.place(y=20, x=300)
amount_of_beds.place(y=60, x=300)
# window1_START
window.mainloop()

# window 2 start
