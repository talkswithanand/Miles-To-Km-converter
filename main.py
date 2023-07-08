from tkinter import *

def calculate():
    miles = float(input_miles.get())
    km = round(miles * 1.609)
    label3.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

input_miles = Entry(width=15)
input_miles.place(x=90, y=10)

label1 = Label(text="Miles")
label1.place(x=190, y=10)

label2 = Label(text="is equal to")
label2.place(x=15, y=30)

button = Button(text="Calculate", command=calculate)
button.place(x=100, y=50)

label3 = Label(text="0")
label3.place(x=120, y=30)

label4 = Label(text="Km")
label4.place(x=200, y=30)

window.mainloop()