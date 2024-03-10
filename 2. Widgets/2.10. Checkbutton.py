from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")


def checkbutton_changed():
    showinfo(title="info", message=enabled.get())
    if enabled.get() == 1:
        showinfo(title="info", message="ENABLED")
    else:
        showinfo(title="info", message="DISABLED")


enabled = IntVar()
enabled_checkbutton = ttk.Checkbutton(text="Enable", variable=enabled, offvalue="Disabled", onvalue="Enabled",
                                      command=checkbutton_changed)
enabled_checkbutton.pack(padx=6, pady=6, anchor=N)
W enabled_label = ttk.Label(textvariable=enabled)
enabled_label.pack(padx=6, pady=6, anchor=NW)

root.mainloop()


from tkinter import *
from tkinter import ttk

from tkinter.messagebox import showinfo

root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")

def checkbutton_changed():
    showinfo(title="info", message=enabled.get())

enabled_on = "Enabled"
enabled_off = "Disabled"

enabled = StringVar(value=enabled_on)
enabled_checkbutton = ttk.Checkbutton(textvariable=enabled, variable=enabled, offvalue=enabled_off, onvalue=enabled_on)
enabled_checkbutton.pack(padx=6, pady=6, anchor=N)

root.mainloop()


from tkinter import *
from tkinter import ttk

root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")


def select():
    result = "Selected: "
    if python.get() == 1: result = f"{result} Python"
    if js.get() == 1: result = f"{result} JS"
    if c.get() == 1: result = f"{result} C"
    languages.set(result)


position = {"padx": 6, "pady": 6, "anchor": NW}
languages = StringVar()
languages_label = ttk.Label(textvariable=languages)
languages_label.pack(**position)

python = IntVar()
python_checkbutton = ttk.Checkbutton(text="Python", variable=python, command=select)
python_checkbutton.pack(**position)

js = IntVar()
js_checkbutton = ttk.Checkbutton(text="JavaScript", variable=js, command=select)
js_checkbutton.pack(**position)

c = IntVar()
c_checkbutton = ttk.Checkbutton(text="C", variable=c, command=select)
c_checkbutton.pack(**position)
root.mainloop()
