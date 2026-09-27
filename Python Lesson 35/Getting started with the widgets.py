from tkinter import *
from datetime import date
root = Tk()

root.title("Getting started with widgets")

root.geometry("500x300")

lbl = Label(text='Hey there!!', fg="black", bg='orange',height=1, width=300)

name_lbl = Label(text='Full Name', fg="black", bg='white')

name_entry = Entry()

def display():

    name = name_entry.get()

    global message

    message = "welcome to the application! \nToday's date is : "

    greet = "Hello " + name + "\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height = 3)

btn = Button(text = "Click Me !", command = display, height = 1, bg = "pink", fg = "green")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()