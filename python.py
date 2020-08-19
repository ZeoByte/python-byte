from tkinter import *

from tkinter import messagebox

window = Tk()

window.title("PythonByte")

window.geometry('500x350')

def clicked():

    messagebox.showinfo('True', 'You have clicked the messagebox!')

btn = Button(window,text='‏‏‎ ‎‏‏‎ ‎‏‏‎‏‏‎ ‎‏‏‎ ‎ ‎‏‏‎ Click‏‏‎ ‎‏‏‎ ‎‏‏‎‏‏‎ ‎‏‏‎ ‎ ‎‏‏‎ ', command=clicked)

btn.grid(column=0,row=0)

btn.place(relx=0.5, rely=0.5, anchor=CENTER)

lbl = Label(window, text="from github.com/ZeoByte")

lbl.grid(column=0, row=0)

lbl.place(relx=1.0, rely=1.0, anchor=SE)

window.mainloop()
