from tkinter import *
from tkinter import ttk

root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")

label = ttk.Label(text="Hello HERO!", font=("Arial", 30))
label.pack()
python_tkinter = PhotoImage(file="../image.png")
label = ttk.Label(image=python_tkinter, text="TKinter", compound="top")
label.pack()

label = ttk.Label(text="Hello TKinter", borderwidth=2, relief="ridge", padding=8)
label.pack(expand=True)
root.mainloop()
