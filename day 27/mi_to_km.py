from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Input field
miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

# Labels
miles_label = Label(text="Miles", font=("Arial", 25))
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to", font=("Arial", 25))
equal_label.grid(row=1, column=0)

kilometer_result_label = Label(text="0", font=("Arial", 25))
kilometer_result_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 25))
km_label.grid(row=1, column=2)

# Function to convert miles to km
def miles_to_km():
    miles = float(miles_input.get())  # now correctly refers to the Entry
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km:.2f}")

# Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1, pady=20)

window.mainloop()
