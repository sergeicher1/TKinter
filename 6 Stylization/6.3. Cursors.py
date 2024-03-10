from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

ttk.Label(text="Hello World!", cursor="pencil").pack(anchor=CENTER, expand=1)

root.config(cursor="watch")

root.mainloop()
