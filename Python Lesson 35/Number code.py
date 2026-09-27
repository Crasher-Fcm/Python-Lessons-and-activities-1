from tkinter import *

root = Tk()

root.title("Nmber Pad")

root.geometry("250x300")

frame = Frame(master = root, height = 200, width = 360, bg = "darkgray")

num = [[9,8.7],
       [6,5,4],
       [3,2,1],
        ['#',0, '*']]

root.mainloop()