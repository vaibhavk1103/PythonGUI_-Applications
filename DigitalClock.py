# Importing necessary libraries.
from tkinter import *
from time import strftime

# Creating the main window.
window = Tk()
window.title("Digital Clock")


# Defining function to get the time from the system.
def time():
    computer_time = strftime("%H:%M:%S")                                             # %p for am or pm
    lbl.config(text=computer_time)
    lbl.after(1000, time)


# Creating the label in which the time will be displayed.
lbl = Label(window, font=("times new roman", 160, "bold"), bg="black", fg="cyan")
lbl.pack(anchor="center", fill="both", expand=0)
time()
window.mainloop()
