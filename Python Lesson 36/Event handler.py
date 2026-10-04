from tkinter import *

root = Tk()

root.title("Event Handler")

root.geometry("300x280")

def handle_keypress(event):
    """
    print the character associated to the key pressed.
    """

    print(event.char)

root.bind("<Key>", handle_keypress)

def handle_click(event):
        print("\nThe button was clicked")

button = Button(text = "Click Me!")        
button.pack()

button.bind("<Button-1>", handle_click)

root.mainloop()