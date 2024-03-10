from tkinter import *

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

canvas = Canvas(bg="white", width=250, height=150)
canvas.pack(fill=BOTH, expand=1)
big_size = (60, 60, 150, 150)
small_size = (60, 60, 100, 100)


def make_big(event): canvas.coords(id, big_size)


def make_small(event): canvas.coords(id, small_size)


id = canvas.create_rectangle(small_size, fill="red")
canvas.tag_bind(id, "<Enter>", make_big)
canvas.tag_bind(id, "<Leave>", make_small)

root.mainloop()
