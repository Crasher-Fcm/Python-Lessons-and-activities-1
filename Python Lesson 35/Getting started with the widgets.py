from tkinter import *
from datetime import date
root = Tk()

root.title("Getting started with widgets")

root.geometry("500x300")

lbl = Label(text='Hey there!!', fg="black", bg='orange',height=1, width=300)

name_lbl = Label(text='Full Name', fg="black", bg='white')

name = Entry()

root.mainloop()