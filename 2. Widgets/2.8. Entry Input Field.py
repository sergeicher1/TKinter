from tkinter import *
from tkinter import ttk


def show_message():
    label["text"] = entry.get()


def clear():
    entry.delete(0, END)


root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")
label = ttk.Label()
label.pack(anchor="nw", padx=6, pady=6)
entry = ttk.Entry()
entry.pack(anchor="nw", padx=6, pady=6)
entry.insert(0, "Hello HERO!")

btn = ttk.Button(text="Display", command=show_message)
btn.pack(anchor="nw", padx=6, pady=6)
clear_btn = ttk.Button(text="Clear", command=clear)
clear_btn.pack(side=LEFT, anchor="n", padx=6, pady=6)

root.mainloop()


import re
from tkinter import *
from tkinter import ttk


def is_valid(new_value):
    result = re.match(r"^\+\d{0,11}$", new_value) is not None
    if not result and len(new_value) <= 12:
        errmsg.set("The desired format is +xxxxxxxxxxx")
    else:
        errmsg.set("")
    return result


root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")
check = (root.register(is_valid), "%P")
errmsg =  StringVar()

phone_entry = ttk.Entry(validate="key", validatecommand=check)
phone_entry.pack(padx=5, pady=6, anchor="nw")
error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.pack(padx=5, pady=5, anchor="nw")
root.mainloop()
