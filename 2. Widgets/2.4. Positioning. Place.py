from tkinter import *
from tkinter import ttk

root = Tk()
root.title("HERO!")
root.geometry("300x300+800+300")

btn = ttk.Button(text="Click Me")
btn.place(x=20,y=20)
btn.place(relx=0.4, rely=0.25)
btn.place(relx=0.5, rely=0.5, anchor="c")
btn.place(relx=0.5, rely=0.5, anchor="c", width=100, height=60)
btn.place(relx=0.5, rely=0.5, anchor="c", relwidth=0.33, relheight=0.25)
root.mainloop()
