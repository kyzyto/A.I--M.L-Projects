import tkinter as tk
#from tkinter import messagebox
from functools import partial
from tkinter.tix import *

# Declaration of global variable
temp_Val = "Celsius"


# getting drop down value
def store_temp(set_temp):
    global temp_Val
    temp_Val = set_temp

    # Conversion of  temperature


def call_convert(result_label, inputn):
    temp = inputn.get()
    if temp.isnumeric() == True:
        
        if temp_Val == 'Celsius':
            # Conversion of celsius temperature to fahrenheit
            f = float((float(temp) * 9 / 5) + 32)
            result_label.config(text="%.1f degrees Celcius converts to %.1f degrees Fahrenheit" % (float(temp),f))
            #messagebox.showinfo("Temperature Converter", "Calculation Successful", )

        if temp_Val == 'Fahrenheit':

            # Conversion of fahrenheit temperature celcius
            # to celsius
            c = float((float(temp) - 32) * 5 / 9)
            result_label.config(text="%.1f degrees Fahrenheit converts to %.1f degrees Celsius" % (float(temp),c))
            #messagebox.showinfo("Temperature Converter", "Calculation Successful")
    else:
        #messagebox.showinfo("Temperature Converter", "ERROR: Please enter a numeric temperature to convert.")
        result_label.config(text="ERROR: Please enter a numeric temperature to convert.")
    return

# Set all input and output fields to be blank.


def clear_window(_event=None):
    result_label.configure(text="")
    input_entry.delete(0, END)
    input_entry.focus()

import sys

def close_window(_event = None):
    sys.exit()

# creating Tk window
window = tk.Tk()

# setting geometry of tk window
window.geometry("600x200")

# Using title() to display a message in the
# dialogue box of the message in the title bar
window.title('Temperature Converter')

# Lay out widgets
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)

inputNumber = tk.StringVar()
var = tk.StringVar()

# label
input_label = tk.Label(window, text="Enter temperature", padx=10, pady=10)
input_label.grid(row=1, column=0)

# entry
input_entry = tk.Entry(window, textvariable=inputNumber)
input_entry.grid(row=1, column=1)

result_label = tk.Label(window, padx=10, pady=10)
result_label.grid(row=3, columnspan=2)

# drop down setup
dropDownList = ["Celsius", "Fahrenheit"]
drop_down = tk.OptionMenu(window, var, *dropDownList, command=store_temp)

var.set(dropDownList[0])
drop_down.grid(row=1, column=2)

# button widget
call_convert = partial(call_convert, result_label, inputNumber)
result_button = tk.Button(window, text="Convert", command=call_convert)
result_button.grid(row=2, column=1)

clear_button = tk.Button(window, text="Clear", command = clear_window)
clear_button.grid(row=2, column=2 )

exit_button = tk.Button(window, text="Exit", command = close_window)
exit_button.grid(row=2, column=3)


label_status = tk.Label(window, text = '', width = 100)
label_status.grid(row = 5, columnspan = 2)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
window.mainloop()