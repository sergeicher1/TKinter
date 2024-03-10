from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from tkinter import  font
root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
for font in font.families():
    print(font)
font1 = font.Font(family="Arial", size=20, weight="normal", slant="roman", underline=True, overstrike=True)
label1 = ttk.Label(text="Hello World!", font=font1)
label1.pack(anchor=NW)


font2 = font.Font(family="Verdana", size=30, weight="normal", slant="roman")
label2 = ttk.Label(text="Hello HERO!", font=font2)
label2.pack(anchor=NW)
root.mainloop()
