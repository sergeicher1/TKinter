from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, OK, INFO

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")


def open_info():
    showinfo(title="Information", message="Announcement")

def open_warning():
    showwarning(title="Warning", message="Alert message")

def open_error():
    showerror(title="Error", message="Error message")

info_button = ttk.Button(text="Information", command=open_info)
info_button.pack(anchor=CENTER, expand=1)
warning_button = ttk.Button(text="Warning", command=open_warning)
warning_button.pack(anchor=CENTER, expand=1)
error_button = ttk.Button(text="Error", command=open_error)
error_button.pack(anchor=CENTER, expand=1)
def click():
    result = askyesnocancel(title="Confirmation", message="Confirm or no?")
    if(result == None): showinfo("Result", "Operation suspended")
    elif(result): showinfo("Result", "operation confirmed")
    else: showinfo("Result", "operation canceled")
def click():
    showinfo(title="Hello Hero!", message="Welcome to zero-to-hero.dev!", detail="Hello World!", icon=INFO, default=OK)


ttk.Button(text="Click", command=click).pack(anchor=CENTER, expand=1)
root.mainloop()
