from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

def change(new_val):
    label["text"] = new_val


label = ttk.Label()
label.pack(anchor=NW)
scale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, command=change)
scale.pack(anchor=NW)

val = IntVar(value=10)
ttk.Label(textvariable=val).pack(anchor=NW)
verticalScale = ttk.Scale(orient=VERTICAL, length=200, from_=1.0, to=100.0, variable=val )
verticalScale.pack(anchor=NW)

horizontalScale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, value=30)
horizontalScale.pack()

root.mainloop()
