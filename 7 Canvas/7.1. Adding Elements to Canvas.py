import cgitb
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
h = ttk.Scrollbar(orient=HORIZONTAL)
v = ttk.Scrollbar(orient=VERTICAL)
canvas = Canvas(scrollregion=(0,0,1000,1000), bg="white", yscrollcommand=v.set, xscrollcommand=h.set)
h["command"] = canvas.xview
v["command"] = canvas.yview

canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
canvas.create_rectangle(10,10,300,300, fill="red")


root.mainloop()








canvas = Canvas(bg="white", width=250, height=250)
canvas.pack(anchor=CENTER, expand=1)


canvas.create_line(10,10,200,50, activefill="red", fill="blue", dash=2)
canvas.create_line(10,50,200,90, activefill="red", fill="blue", dash=2)
canvas.create_rectangle(10,20,200, 60, fill="blue", outline="red")
canvas.create_oval(10, 10, 200, 50, fill="grey", outline="green")
canvas.create_polygon(10,30,200,200,200,30, fill="blue", outline="red")
points = (
    (10, 30),
    (200,200),
    (200,30),
)
canvas.create_polygon(*points, fill="red", outline="green")
canvas.create_arc((10,10), (200,200), fill="grey", outline="red")
canvas.create_text(50,50, text="Hello", fill="red")
canvas.create_text(100, 100,anchor=NW, text="World!", fill="blue")
python_img =  PhotoImage(file="../python.png")
canvas.create_image(10,10, anchor=NW, image=python_img)
btn = ttk.Button(text="Click")
canvas.create_window(10,20, anchor="nw", window=btn, width=100, height=100)
