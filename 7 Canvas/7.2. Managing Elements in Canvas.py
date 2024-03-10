from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

red = "red"
blue = "blue"
selected_color = StringVar(value=red)

canvas = Canvas(bg="white", width=350, height=200)
canvas.pack(anchor=CENTER, expand=1)


def select():
    canvas.itemconfigure(line, fill=selected_color.get())


red_btn = ttk.Radiobutton(text=red, value=red, variable=selected_color, command=select, padding=6)
red_btn.pack(anchor="nw")
blue_btn = ttk.Radiobutton(text=blue, value=blue, variable=selected_color, command=select, padding=6)
blue_btn.pack(anchor="nw")

line = canvas.create_line(10, 10, 200, 100, fill=selected_color.get())
root.mainloop()

y = 0
direction = -10
btn_height = 40
canvas_height = 200
def clicked_button():
    global y, direction
    if y >= canvas_height - btn_height or y <=0 : direction = direction * -1
    y = y + direction
    canvas.coords(btnId, 10, y)

#
# def remove_button():
#     canvas.delete(btnId)
#
btn = ttk.Button(text="Click", command=clicked_button)
btnId = canvas.create_window(10,y, anchor=NW, window=btn, width=100, height=btn_height)
