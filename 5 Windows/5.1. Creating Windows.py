from tkinter import *
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("New Window")
        self.geometry("300x300+200+500")
        self.close_button = ttk.Button(self, text="Close window")
        self.close_button["command"] = self.button_clicked
        self.close_button.pack(anchor=CENTER, expand=1)

    def button_clicked(self):
        self.destroy()


root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")


def click():
    window = Window()

window = Tk()
window.title("New Window")
window.geometry("300x300+200+500")
close_button = ttk.Button(window, text="Close window", command=lambda : window.destroy())
close_button.pack(anchor=CENTER, expand=1)
label = ttk.Label(window, text="A completely new window")
label.pack(anchor=CENTER, expand=1)


button = ttk.Button(text="Create New Window", command=click)
button.pack(anchor=CENTER, expand=1)


from tkinter import *
from tkinter import ttk


def dismiss(window):
    window.grab_release()
    window.destroy()


def click():
    window = Toplevel()
    window.title("New Window")
    window.geometry("300x300+200+500")
    window.protocol("WM_DELETE_WINDOW", lambda: dismiss(window))
    close_button = ttk.Button(window, text="Close window", command=lambda: dismiss(window))
    close_button.pack(anchor="center", expand=1)
    window.grab_set()


root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

open_button = ttk.Button(text="Create window", command=click)
open_button.pack(anchor=CENTER, expand=1)
root.mainloop()
