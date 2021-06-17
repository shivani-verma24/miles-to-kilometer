from tkinter import *

def button_clicked():
    miles = miles_entry.get()
    km = float(miles) * 1.609
    output_label.config(text = km)

window = Tk()
window.title("Miles to Kilometer Converter")

window.config(padx= 20, pady = 20)


label1 = Label(text = "Miles")
label1.grid(row = 0, column = 2)
label2 = Label(text = "is equal to")
label2.grid(row = 1, column = 0)
label3 = Label(text = "Km")
label3.grid(row = 1, column = 2)
output_label = Label(text = "0")
output_label.grid(row = 1, column = 1)

miles_entry = Entry(width = 8)
miles_entry.grid(row = 0,column = 1)


button = Button(text ="Calculate", command = button_clicked)
button.grid(row = 2, column = 1)

window.mainloop()

# Project by Shivani Verma