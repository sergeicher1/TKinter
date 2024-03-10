from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
people = [("Tom", 33, "tom@gmail.com"), ("Bob", 44, "bob@gmail.com"), ("Alice", 22, "alice@gmail.com")]

label = ttk.Label()
label.pack(anchor=N, fill=X)
columns = ("name", "age", "email")
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(expand=1, fill=BOTH)
tree.heading("name", text="Name", anchor=W)
tree.heading("age", text="Age", anchor=W)
tree.heading("email", text="Email", anchor=W)
tree.column("#1", stretch=NO, width=70)
tree.column("#2", stretch=NO, width=70)
tree.column("#3", stretch=NO, width=120)
for person in people:
    tree.insert("", END, values=person)


def item_selected(event):
    selected_people = ""
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        person = item["values"]
        selected_people = f"{selected_people}{person}\n"
    label["text"] = selected_people


tree.bind("<<TreeviewSelect>>", item_selected)
root.mainloop()
