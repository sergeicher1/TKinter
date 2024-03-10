from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

people = [("Tom", 33, "tom@gmail.com"), ("Bob", 44, "bob@gmail.com"), ("Alice", 22, "alice@gmail.com")]

columns = ("name", "age", "email")
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(expand=1, fill=BOTH)


def sort(col, reverse):
    l = [(tree.set(k, col), k) for k in tree.get_children("")]
    l.sort(reverse=reverse)
    for index, (_, k) in enumerate(l):
        tree.move(k, "", index)
    tree.heading(col, command=lambda: sort(col, not reverse))


tree.heading("name", text="Name", anchor=W, command=lambda: sort(0, False))
tree.heading("age", text="Age", anchor=W, command=lambda: sort(1, False))
tree.heading("email", text="Email", anchor=W, command=lambda: sort(2, False))
tree.column("#1", stretch=NO, width=70)
tree.column("#2", stretch=NO, width=50)
tree.column("#3", stretch=NO, width=110)
for person in people:
    tree.insert("", END, values=person)

root.mainloop()
