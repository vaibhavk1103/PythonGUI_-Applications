from tkinter import *                                                                                                   # Importing packages.
from covid import Covid                                                                                                 # Importing packages.

covid = Covid()
window = Tk()                                                                                                           # Creating the main window.
default_label = Label(window, text='Do you want the latest details on Corona Virus? [Y or N]:', justify=LEFT, anchor=W,
                      font=("Times New Roman", 15))                                                                     # Making and placing the labels in the main window.
default_label.grid(row=0, column=0, pady=5)
first_label = Label(window, text="", anchor=W)
first_label.grid(row=1, column=0, pady=5)
second_label = Label(window, text="", justify=LEFT, anchor=W)
second_label.grid(row=2, column=0, pady=1)
third_label = Label(window, text="", justify=LEFT, anchor=W, fg='green')
third_label.grid(row=3, column=0, pady=1)
fourth_label = Label(window, text="", justify=LEFT, anchor=W, fg='red')
fourth_label.grid(row=4, column=0, pady=1)
fifth_label = Label(window, text="", justify=LEFT, anchor=W, fg='brown')
fifth_label.grid(row=5, column=0, pady=1)
sixth_label = Label(window, text="", justify=LEFT, anchor=W)
sixth_label.grid(row=6, column=0, pady=1)
seventh_label = Label(window, text="", anchor=W)
seventh_label.grid(row=7, column=0, pady=1)
eighth_label = Label(window, text="", anchor=W, fg='orange')
eighth_label.grid(row=8, column=0, pady=1)                                                                              # Making and placing the labels in the main window.


def clicked1():                                                                                                         # Making function which is performed when the first button is clicked.
    if initialinput.get() == 'y':
        first_label.config(text=f"The latest details on Corona Virus: ", font=("Times New Roman", 15, "bold"))          # Modifying labels according to the function that is being performed.
        second_label.config(text=f"Total confirmed Covid-19 cases till date : {covid.get_total_confirmed_cases()}",
                            font=("Times New Roman", 15, "bold", 'underline'))
        third_label.config(text=f"Total recoveries from Covid-19 till date : {covid.get_total_recovered()}",
                           font=("Times New Roman", 15, "bold", 'underline'))
        fourth_label.config(
            text=f"The total number of active Covid-19 cases till date: {covid.get_total_active_cases()}",
            font=("Times New Roman", 15, "bold", 'underline'))
        fifth_label.config(text=f"Total deaths due to the Covid-19 till date : {covid.get_total_deaths()}",
                           font=("Times New Roman", 15, "bold", 'underline'))                                           # Modifying labels according to the function that is being performed.

        def clicked2():                                                                                                 # Creating the second function which provides the details for any country entered by the user.
            country = countryinput.get()
            b = covid.get_status_by_country_name(country)
            seventh_label.config(text=f'The details of the country of your choice are:\n{b}',                           # Modifying labels according to the function that is being performed.
                                 font=("Times New Roman", 15, "bold"))
            eighth_label.config(
                text=f'\nClean your hands often. Use soap and water, or an alcohol-based hand rub.\n'
                     f'Maintain a safe distance from anyone who is coughing or sneezing.\n'
                     f'Wear a mask when physical distancing is not possible.\n'
                     f'Don’t touch your eyes, nose or mouth.\n'
                     f'Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\n'
                     f'Stay home if you feel unwell.\n'
                     f'If you have a fever, cough and difficulty breathing, seek medical attention.\n',
                font=("Times New Roman", 15, "bold", 'underline'))

        sixth_label.config(text=f"Enter the name of the country for which you want the current details:",
                           font=("Times New Roman", 15, "bold"))                                                        # Modifying labels according to the function that is being performed.
        countryinput = Entry(window, width=10)                                                                          # Creating a box for country input.
        countryinput.grid(row=6, column=1, pady=1)
        enter2 = Button(window, text=f'Click me to proceed', borderwidth=5, command=lambda: clicked2())                 # Creating a button to perform a specific function.
        enter2.grid(row=6, column=2, pady=5, padx=5)
    elif initialinput.get() == 'n':                                                                                     # Second case for initial input.
        first_label.config(text=f"Stay safe and a have a nice day."                                                     # Modifying labels according to the function that is being performed.
                                f'\n\nClean your hands often. Use soap and water, or an alcohol-based hand rub.\n'
                                f'Maintain a safe distance from anyone who is coughing or sneezing.\n'
                                f'Wear a mask when physical distancing is not possible.\n'
                                f'Don’t touch your eyes, nose or mouth.\n'
                                f'Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\n'
                                f'Stay home if you feel unwell.\n'
                                f'If you have a fever, cough and difficulty breathing, seek medical attention.\n',
                           font=("Times New Roman", 15, "bold", 'underline'))
    elif initialinput.get != 'y' or 'n':                                                                                # Default case.
        first_label.config(text="Enter a valid input.")


window.title("Coronavirus Tracker")                                                                                     # Main window details.
window.geometry("1740x520")                                                                                             # Size of main window.
initialinput = Entry(window, width=10)                                                                                  # Yes or No input box.
initialinput.grid(row=0, column=1, pady=5)
enter1 = Button(window, text=f'Click me to proceed', borderwidth=5, command=clicked1)
enter1.grid(row=0, column=2, pady=5, padx=5)

window.mainloop()                                                                                                       # Main window execution.
