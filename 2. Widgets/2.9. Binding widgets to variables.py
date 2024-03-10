from tkinter import *
from tkinter import ttk


message = StringVar()
label = ttk.Label(textvariable=message)
label.pack(anchor="nw", padx=6, pady=6)

entry = ttk.Entry(textvariable=message)
entry.pack(anchor="nw", padx=6, pady=6)

button = ttk.Button(textvariable=message)
button.pack(side=LEFT, anchor="n", padx=6, pady=6)
def click_button():
    value = clicks.get()
    clicks.set(value + 1)


root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")
clicks = IntVar(value=0)
btn = ttk.Button(textvariable=clicks, command=click_button)
btn.pack(anchor=CENTER, expand=1)
root.mainloop()


from tkinter import *
from tkinter import ttk


def check(*args):
    print(name)
    if name.get() == "admin":
        result.set("Forbidden")
    else:
        result.set("OK")


root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")
name = StringVar()
result = StringVar()
name_entry = ttk.Entry(textvariable=name)
name_entry.pack(padx=5, pady=5, anchor=NW)

check_label = ttk.Label(textvariable=result)
check_label.pack(padx=5, pady=5, anchor=NW)
name.trace_add("write", check)
root.mainloop()
