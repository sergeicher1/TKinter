from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

editor = Text()
editor.pack(fill=BOTH, expand=1)
char_editor = Text(height=5,wrap="char")
char_editor.pack(anchor=N, fill=X)

word_editor = Text(height=5, wrap="word")
word_editor.pack(anchor=S, fill=X)

from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
st = ScrolledText(root, width=50, height=10)
st.pack(fill=BOTH, side=LEFT, expand=True)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
editor = Text(wrap="none")
editor.grid(column=0, row=0, sticky=NSEW)
ys = ttk.Scrollbar(orient="vertical", command=editor.yview)
ys.grid(column=1, row=0, sticky=NS)
xs = ttk.Scrollbar(orient="horizontal", command=editor.xview)
xs.grid(column=0, row=1, sticky=EW)
editor["yscrollcommand"] = ys.set
editor["xscrollcommand"] = xs.set



root.mainloop()
