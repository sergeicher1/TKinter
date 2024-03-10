from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

editor = Text()
editor.pack(fill=BOTH, expand=1)
editor.insert("1.0", "Hello World")
editor.insert(END, "\nHello HERO!")

editor = Text(height=5)
editor.pack(anchor=N, fill=X)
editor.insert("1.0", "The Sun Is Shining")
label =ttk.Label()
label.pack(anchor=N, fill=BOTH)

def get_text():
    label["text"] = editor.get("1.0", "end")
def delete_text():
    editor.delete("1.0", END)
def edit_text():
    editor.replace("1.0", "1.3", "Moon")
button = ttk.Button(text="Replace", command=edit_text)
button.pack(side=BOTTOM)



root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

editor = Text(undo=True)
editor.grid(column=0, columnspan=2, row=0, sticky=NSEW)
def undo(): editor.edit_undo()
def redo(): editor.edit_redo()

redo_button = ttk.Button(text="Undo", command=undo)
redo_button.grid(column=0, row=1)
undo_button = ttk.Button(text="Redo", command=redo)
undo_button.grid(column=1, row=1)

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
def get_selection(): label["text"] = editor.selection_get()
def clear_selection(): editor.selection_clear()

editor = Text(height=5)
editor.pack(fill=X)
label = ttk.Label()
label.pack(anchor=NW)
get_button = ttk.Button(text="Get Selection", command=get_selection)
get_button.pack(side=LEFT)
clear_button = ttk.Button(text="Clear", command=clear_selection)
clear_button.pack(side=RIGHT)



from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

def on_modified(event): label["text"]=editor.get("1.0", END)
def on_modified(event): label["text"]=editor.selection_get()
editor = Text(height=5)
editor.pack(fill=X)
editor.bind("<<Selection>>", on_modified)

label = ttk.Label()
label.pack(anchor=NW)

root.mainloop()