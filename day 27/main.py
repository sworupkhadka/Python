from tkinter import *

window = Tk()
window.title("my first gui program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=100)

# Label
my_label = Label(text="i am a label", font=("Arial", 25, "bold"))
my_label.grid(column=0, row=0)

# Button click function
def button_clicked():
    print("i got clicked")
    new_text=input.get()
    my_label.config(text=new_text)

# Button
button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

# Button
button = Button(text="click me", command=button_clicked)
button.grid(column=2, row=0)

#input
input=Entry(width=10)
input.grid(column=3 , row=2)

# Run the GUI
window.mainloop()  # must always be at the end
