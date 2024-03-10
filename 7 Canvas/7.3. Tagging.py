from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
red = "red"
blue = "blue"
green = "green"
selected_color = StringVar(value=red)
canvas = Canvas(bg="white", width=250, height=150)
canvas.pack(anchor="nw")

canvas.create_rectangle((10, 80, 130, 130), fill=selected_color.get(), outline="black", tags="house")
canvas.create_polygon((10, 80), (70, 30), (130, 80), fill=selected_color.get(), outline="black", tags="house")


def select():
    canvas.itemconfigure("house", fill=selected_color.get())


ttk.Radiobutton(text=red, value=red, variable=selected_color, command=select, padding=6).pack(anchor="nw")
ttk.Radiobutton(text=blue, value=blue, variable=selected_color, command=select, padding=6).pack(anchor="nw")
ttk.Radiobutton(text=green, value=green, variable=selected_color, command=select, padding=6).pack(anchor="nw")
root.mainloop()
