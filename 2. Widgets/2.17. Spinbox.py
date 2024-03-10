from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

def change():
    label["text"] = spinbox.get()


spinbox_var = StringVar(value=22)
label = ttk.Label(textvariable=spinbox_var)
spinbox_var = StringVar()
languages = ["Python", "JavaScript", "JAVA", "C#", "C++"]
label = ttk.Label(textvariable=spinbox_var)
label.pack(anchor=NW)

spinbox = ttk.Spinbox(textvariable=spinbox_var, values=languages)
spinbox.pack(anchor=NW)

root.mainloop()
