from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

main_menu = Menu()
main_menu.add_cascade(label="File")
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")
main_menu.add_cascade(label="Version")
root.config(menu=main_menu)
root.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
root.option_add("*tearOff", False)
main_menu = Menu()
file_menu = Menu()
settings_menu = Menu()
settings_menu.add_command(label="Save")
settings_menu.add_command(label="Open")
file_menu.add_cascade(label="Settings", menu=settings_menu)
file_menu.add_cascade(label="New")
file_menu.add_cascade(label="Save")
file_menu.add_cascade(label="Open")
file_menu.add_cascade(label="Save as")
file_menu.add_separator()
file_menu.add_cascade(label="Exit")

def edit_click():
    messagebox.showinfo("Edit","The edit menu is clicked")
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", command=edit_click)
main_menu.add_cascade(label="View")
main_menu.add_cascade(label="Version")
root.config(menu=main_menu)

root.mainloop()