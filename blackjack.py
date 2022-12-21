from tkinter import *

# setup
top = Tk()
top.geometry("600x450")
name = Label(top, text="Blackjack").place(x=300, y=100)
starbutton = Button(top, text="Start", fg="red")

top.mainloop()
