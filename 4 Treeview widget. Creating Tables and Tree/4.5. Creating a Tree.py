from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

tree = ttk.Treeview()
tree.heading("#0", text="Departments", anchor=NW)
tree.pack(expand=1, fill=BOTH)
tree.insert("", END, iid=1, text="Administrative Department", open=True)
tree.insert("", END, iid=2, text="IT Department")
tree.insert("", END, iid=3, text="Sales")

tree.insert(1, index=END, text="Tom")
tree.insert(2, index=END, text="Bob")
tree.insert(3, index=END, text="Sam")
root.mainloop()
