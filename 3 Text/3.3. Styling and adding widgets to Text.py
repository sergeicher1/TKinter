from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

editor = Text(wrap="none")
editor.pack(expand=1, fill=BOTH)
editor.insert("1.0", "Hello ")
editor.tag_add("highlightline", "1.0", "1.2")
editor.insert("end", "World", "highlightline")
editor.insert("end", "\n Hello Hero!")

editor.tag_configure("highlightline", background="#ccc", foreground="red", font="TkFixedFont", relief="raised")

editor = Text()
editor.pack(expand=1, fill=BOTH)
def click(): editor.insert("2.0", "Click\n")
btn = ttk.Button(editor, text="Click", command=click)
editor.window_create("1.0", window=btn)
python_img = PhotoImage(file="../python.png")
editor.image_create("1.0", image=python_img)
root.mainloop()