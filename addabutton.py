
import Tkinter
from Tkinter import*
window=Tk()

window.title("Welcome")

bt=Button(window,text="Click me!!",bg="pink",fg="red").grid(column=0,row=0)
window.geometry('300x300')

window.mainloop()
