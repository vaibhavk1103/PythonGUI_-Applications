from tkinter import *                                                                                                   # Importing the required packages.
import tkinter as tk                                                                                                    # Importing the required packages.
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from PyDictionary import PyDictionary
from googletrans import Translator                                                                                      # Importing the required packages.

root = tk.Tk()                                                                                                          # Creating the main window.
root.title('Dictionary')
root.geometry('600x300')
root['bg'] = 'white'
frame = Frame(root, width=200, height=300, borderwidth=1, relief=RIDGE)
frame.grid(sticky="W")


def get_meaning():                                                                                                      # Function to get the meaning of the entered word.
    dictionary = PyDictionary()
    get_word = entry.get()                                                                                              # Taking the inputted word.
    languages = language.get()                                                                                          # Taking the inputted language.

    if get_word == "":                                                                                                  # Checking for correct word.
        messagebox.showerror('Dictionary', 'please write the word')

    elif languages == 'English-to-English':                                                                             # Getting the meaning of the word in English.
        d = dictionary.meaning(get_word)
        output.insert('end', d['Noun'])

    elif languages == 'English-to-Hindi':                                                                               # Translating the word into Hindi.
        translator = Translator()
        t = translator.translate(get_word, dest='hi')
        output.insert('end', t.text)


def quit():                                                                                                             # Function to end the program and exit.
    root.destroy()


img = ImageTk.PhotoImage(Image.open('dict.png'))                                                                        # Loading an image for representational purposes.
pic = Label(root, image=img)
pic.place(x=40, y=70)

word = Label(root, text="Enter Word", bg="white", font=('verdana', 10, 'bold'))                                         # Text to be shown above the input box.
word.place(x=250, y=23)

a = tk.StringVar()                                                                                                      # For languages.
language = ttk.Combobox(root, width=20, textvariable=a, state='readonly', font=('verdana', 10, 'bold'), )

language['values'] = (
    'English-to-English',
    'English-to-Hindi',

)

language.place(x=380, y=10)                                                                                             # Placing the language combobox.
language.current(0)

entry = Entry(root, width=50, borderwidth=2, relief=RIDGE)                                                              # Taking input from the user.
entry.place(x=250, y=50)

search = Button(root, text="Search", font=('verdana', 10, 'bold'), cursor="hand2", relief=RIDGE, command=get_meaning)   # Button to initialize the search of the meaning of the word.
search.place(x=430, y=80)

quit = Button(root, text="Quit", font=('verdana', 10, 'bold'), cursor="hand2", relief=RIDGE, command=quit)              # Button to exit the program.
quit.place(x=510, y=80)

meaning = Label(root, text="Meaning", bg="white", font=('verdana', 15, 'bold'))                                         # Text to be shown above the box which displays the meaning of the word.
meaning.place(x=230, y=120)

output = Text(root, height=8, width=40, borderwidth=2, relief=RIDGE)
output.place(x=230, y=160)

root.mainloop()
