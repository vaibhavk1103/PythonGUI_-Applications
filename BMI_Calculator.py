from tkinter import *

window = Tk()
first_label = Label(window, text='Enter your weight in kilograms:(in digits)',
                    font=("Times New Roman", 15))
first_label.grid(row=0, column=0, pady=10)
weight_input = Entry(window, width=15)
weight_input.grid(row=0, column=1, padx=10, pady=10)
second_label = Label(window, text='Enter your height in metres:(in digits)',
                     font=("Times New Roman", 15))
second_label.grid(row=1, column=0, pady=10)
third_label = Label(window, text='', font=("Times New Roman", 15))
third_label.grid(row=4, column=0, pady=10)
fourth_label = Label(window, text='', font=("Times New Roman", 15))
fourth_label.grid(row=5, column=0, pady=10)
height_input = Entry(window, width=15)
height_input.grid(row=1, column=1, padx=10, pady=10)


def click():
    BMI = float(weight_input.get()) / (float(height_input.get()) * float(height_input.get()))
    third_label.config(text=f'Your BMI is {BMI}', font=("Times New Roman", 15))
    if BMI > 25.0:
        fourth_label.config(text="Watch out, you're overweight.", fg='red')
    elif 18.5 < BMI < 24.9:
        fourth_label.config(text="Congratulations, you're healthy.", fg='green')
    else:
        fourth_label.config(text="Watch out, you're underweight.", fg='red')


proceed = Button(window, text='Click me to proceed', borderwidth=5, command=click)
proceed.grid(row=3, column=1)
window.title('BMI Calculator')
window.geometry('475x225')
window.mainloop()
