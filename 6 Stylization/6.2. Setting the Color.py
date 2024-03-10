from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")


def get_rgb(rgb):
    return "#%02x%02x%02x" % rgb


label = ttk.Label(text="Hello HERO", padding=8, foreground=get_rgb((0, 77, 64)), background=get_rgb((128, 203, 196)))
label.pack(anchor=CENTER, expand=1)
root.mainloop()
