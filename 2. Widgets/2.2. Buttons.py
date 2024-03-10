from tkinter import *
from tkinter import ttk

clicks = 0


def click_counter():
    global clicks
    clicks += 1
    btn["text"] = f"Clicks {clicks}"


root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+500+300")
btn = ttk.Button(text="Click Me", command=click_counter)
btn = ttk.Button(text="Click Me", state=["disabled"])

btn.pack()

root.mainloop()
