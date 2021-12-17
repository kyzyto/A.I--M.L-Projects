from tkinter.tix import *
import sys

window = Tk()
window.geometry("640x320")
window.minsize(width = 600, height = 300)
window.title("Space Eaters")

tooltip = Balloon(window)

# Function to perform the validation and calculation.
def calculate_rectangle(_event = None):
    # Input.
    # Validate the input.
    try:
        # Is the input a number?
        valid_length = float(text_length_input.get())
        valid_width = float(text_width_input.get())

        # Is the input a positive number?
        if valid_length > 0 and valid_width > 0:

            # Processing.
            # Calculate the perimeter and area.
            perimeter = valid_length * 2 + valid_width * 2
            area = valid_length * valid_width
            # Output the perimeter and area.
            label_perimeter_output.configure(text = perimeter)
            label_area_output.configure(text = area)
            label_status.configure(text = "Calculation successful!")

    # If the input is not positive, display an error message.
        else:
            label_status.configure(text = "ERROR: Length and width must both be positive.")
    # If the input is not a number, display an error message.
    except:
        label_status.configure(text = "ERROR: Length and width must both be numeric.")


# Function to clear all fields; window returns to its default state.
def clear_window(_event = None):
    # Set all input and output fields to be blank.
    label_area_output.configure(text = "")
    label_perimeter_output.configure(text = "")
    text_length_input.delete(0, END)
    text_width_input.delete(0, END)
    label_status.configure(text = "All fields cleared.")
    # Put the focus back on the first input control for fast data entry.
    text_length_input.focus()

def close_window(_event = None):
    sys.exit()

# Row 0 controls
# Prompting label for the input length.
label_length = Label(window, text="Length", padx=10, pady=10)
label_length.grid(row = 0, column = 0)
# Text entry for the input length.
text_length_input = Entry(window, width=20)
text_length_input.grid(row = 0, column = 1)

# Row 1 controls
# Prompting label for the input width.
label_width = Label(window, text="Width", padx=10, pady=10)
label_width.grid(row = 1, column = 0)
# Text entry for the input width.
text_width_input = Entry(window, width = 20)
text_width_input.grid(row = 1, column = 1)

# Row 2 controls
# Display label for the area output
label_area = Label(window, text="Area", padx=10, pady=10)
label_area.grid(row = 2, column = 0)
# Output label for the area output
label_area_output = Label(window, text='' ,width = 20)
label_area_output.grid(row = 2, column = 1)

# Row 3 controls
# Display label for the perimeter output
label_perimeter = Label(window, text="Perimeter", padx=10, pady=10)
label_perimeter.grid(row = 3, column = 0)
# Output label for the perimeter output
label_perimeter_output = Label(window, text='', width = 20)
label_perimeter_output.grid(row = 3, column = 1)

# Row 4 controls
# Calculate button
calculate_button = Button(window, text="Calculate", padx=10, pady=6, command=calculate_rectangle)
calculate_button.grid(row = 4, column = 0)
# Clear button
clear_button = Button(window, text="Reset", padx=10, pady=6, command=clear_window)
clear_button.grid(row=4, column = 1)
# Exit button
exit_button = Button(window, text="Exit", padx=10, pady=6, command=close_window)
exit_button.grid(row = 4, column = 2)


# Row 5 control
# This label acts as a status bar in case hover text or some other form of messaging is useful.
label_status = Label(window, width = 100, borderwidth = 1, relief = SOLID)
tooltip.bind_widget(label_status, msg = "Displays status and error messages")
label_status.grid(row = 5, columnspan = 3, sticky = S)

window.mainloop()