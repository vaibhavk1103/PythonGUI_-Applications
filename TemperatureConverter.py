from tkinter import *

window = Tk()
default_label = Label(window, text='Enter 1 if you want to convert from Celsius to Fahrenheit.,\n'
                                   'Enter 2 if you want to convert from Fahrenheit to Celsius.,\n'
                                   'Enter 3 if you want to convert from Celsius to Kelvin.\n'
                                   'Enter 4 if you want to convert from Kelvin to Celsius.\n'
                                   'Enter 5 if you want to convert from Fahrenheit to Kelvin.\n'
                                   'Enter 6 if you want to convert from Kelvin to Fahrenheit.',
                      font=("Times New Roman", 15))
default_label.grid(row=0, column=0, pady=5)
first_label = Label(window, text='', font=("Times New Roman", 15))
first_label.grid(row=1, column=0, pady=5, padx=10)
second_label = Label(window, text='', font=("Times New Roman", 15))
second_label.grid(row=2, column=0, pady=5, padx=10)


def choice():
    if int(choice_input.get()) == 1:
        first_label.config(text='Enter the temperature in Celsius:')
        tempinput = Entry(window, width=10)
        tempinput.grid(row=1, column=1, pady=5, padx=10)

        def conversion():
            fahrenheit = (((int(tempinput.get()) / 5) * 9) + 32)
            second_label.config(text=f'The temperature in Fahrenheit is:{fahrenheit}')

        tempbutton = Button(window, text='Click me to proceed', borderwidth=5, command=conversion)
        tempbutton.grid(row=1, column=2, pady=5, padx=10)
    elif int(choice_input.get()) == 2:
        first_label.config(text='Enter the temperature in Fahrenheit:')
        tempinput = Entry(window, width=10)
        tempinput.grid(row=1, column=1, pady=5, padx=10)

        def conversion():
            celsius = (((int(tempinput.get()) - 32) * 5) / 9)
            second_label.config(text=f'The temperature in Celsius is:{celsius}')

        tempbutton = Button(window, text='Click me to proceed', borderwidth=5, command=conversion)
        tempbutton.grid(row=1, column=2, pady=5, padx=10)
    elif int(choice_input.get()) == 3:
        first_label.config(text='Enter the temperature in Celsius:')
        tempinput = Entry(window, width=10)
        tempinput.grid(row=1, column=1, pady=5, padx=10)

        def conversion():
            kelvin = int(tempinput.get()) + 273
            second_label.config(text=f'The temperature in Kelvin is:{kelvin}')

        tempbutton = Button(window, text='Click me to proceed', borderwidth=5, command=conversion)
        tempbutton.grid(row=1, column=2, pady=5, padx=5)
    elif int(choice_input.get()) == 4:
        first_label.config(text='Enter the temperature in Kelvin:')
        tempinput = Entry(window, width=10)
        tempinput.grid(row=1, column=1, pady=5, padx=10)

        def conversion():
            celsius = int(tempinput.get()) - 273
            second_label.config(text=f'The temperature in Celsius is:{celsius}')

        tempbutton = Button(window, text='Click me to proceed', borderwidth=5, command=conversion)
        tempbutton.grid(row=1, column=2, pady=5, padx=10)
    elif int(choice_input.get()) == 5:
        first_label.config(text='Enter the temperature in Fahrenheit:')
        tempinput = Entry(window, width=10)
        tempinput.grid(row=1, column=1, pady=5, padx=10)

        def conversion():
            kelvin = ((((int(tempinput.get()) - 32) * 5) / 9) + 273)
            second_label.config(text=f'The temperature in Kelvin is:{kelvin}')

        tempbutton = Button(window, text='Click me to proceed', borderwidth=5, command=conversion)
        tempbutton.grid(row=1, column=2, pady=5, padx=10)
    elif int(choice_input.get()) == 6:
        first_label.config(text='Enter the temperature in Kelvin:')
        tempinput = Entry(window, width=10)
        tempinput.grid(row=1, column=1, pady=5, padx=10)

        def conversion():
            fahrenheit = ((((int(tempinput.get()) - 273) * 9) / 5) + 32)
            second_label.config(text=f'The temperature in Fahrenheit is:{fahrenheit}')

        tempbutton = Button(window, text='Click me to proceed', borderwidth=5, command=conversion)
        tempbutton.grid(row=1, column=2, pady=5, padx=10)
    else:
        first_label.config(text='Please enter valid choice.')


window.title('Temperature Converter')
window.geometry('685x230')
choice_input = Entry(window, width=10)
choice_input.grid(row=0, column=1, pady=5, padx=10)
choice_button = Button(window, text='Click me to proceed', borderwidth=5, command=choice)
choice_button.grid(row=0, column=2, pady=5, padx=10)
window.mainloop()
