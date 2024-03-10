from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")


label_style= ttk.Style()
label_style.configure("My.TLabel", font="helvetica 20", foreground="red", padding=10, background="white")
ttk.Style().configure(".", font="helvetica 20", foreground="blue", padding=10, background="green")

label = ttk.Label(text="Hello HERO!", style="My.TLabel")
label.pack(anchor=CENTER, expand=1)
ttk.Button(text="Click").pack(anchor=NW, padx=6, pady=6)
root.mainloop()
