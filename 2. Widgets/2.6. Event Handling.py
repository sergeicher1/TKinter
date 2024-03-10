from tkinter import *
from tkinter import ttk

# def click():
#     print("Hello")


root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")


def entered(event):
    btn["text"] = "Entered"


def left(event):
    btn['text'] = "Left"


btn = ttk.Button(text="Click")
btn.pack(anchor=CENTER, expand=1)
btn.bind("<Enter>", entered)
btn.bind("<Leave>", left)
btn = ttk.Button(text="Click", command=click)

btn.pack()

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")


def single_click(event):
    btn["text"] = "Single Click"


def double_click(event):
    btn["text"] = "Double Click"


btn = ttk.Button(text="Click")
btn.pack(anchor=CENTER, expand=1)
btn.bind("<ButtonPress-1>", single_click)
btn.bind("<Double-ButtonPress-1>", double_click)
root.mainloop()

from tkinter import *
from tkinter import ttk

clicks = 0
root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")


def clicked(event):
    global clicks
    clicks = clicks + 1
    btn["text"] = f"{clicks} Clicks"


btn = ttk.Button(text="Click")
btn.pack(anchor=CENTER, expand=1)
root.bind_class("TButton", "<Double-ButtonPress-1>", clicked)
root.mainloop()
