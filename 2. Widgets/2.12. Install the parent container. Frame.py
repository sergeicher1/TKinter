from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])

label = ttk.Label(frame, text="Enter name")
label.pack(anchor=NW)

entry = ttk.Entry(frame)
entry.pack(anchor=NW)

frame.pack(anchor=NW, fill=X, padx=5, pady=5)
root.mainloop()
