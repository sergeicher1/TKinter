from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
root.rowconfigure(index=0, weight=1)
root.columnconfigure(index=0, weight=1)
people = [("Bill", 40, "bill@gmail.com"), ("Bob", 22, "bob@gmail.com"), ("Shon", 33, "shon@gmail.com"),
          ("Bill", 40, "bill@gmail.com"), ("Bob", 22, "bob@gmail.com"), ("Shon", 33, "shon@gmail.com"),
          ("Bill", 40, "bill@gmail.com"), ("Bob", 22, "bob@gmail.com"), ("Shon", 33, "shon@gmail.com"),
          ("Bill", 40, "bill@gmail.com"), ("Bob", 22, "bob@gmail.com"), ("Shon", 33, "shon@gmail.com"),
          ("Bill", 40, "bill@gmail.com"), ("Bob", 22, "bob@gmail.com"), ("Shon", 33, "shon@gmail.com"),
          ("Bill", 40, "bill@gmail.com"), ("Bob", 22, "bob@gmail.com"), ("Shon", 33, "shon@gmail.com"),
          ("Bill", 40, "bill@gmail.com"), ("Bob", 22, "bob@gmail.com"), ("Shon", 33, "shon@gmail.com"),
          ("Bill", 40, "bill@gmail.com"), ("Bob", 22, "bob@gmail.com"), ("Shon", 33, "shon@gmail.com"),
          ("Bill", 40, "bill@gmail.com"), ("Bob", 22, "bob@gmail.com"), ("Shon", 33, "shon@gmail.com")]

columns = ("name", "age", "email")
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
tree.grid(row=0, column=0, sticky="nsew")

tree.heading("name", text="Name", anchor=W)
tree.heading("age", text="Age", anchor=W)
tree.heading("email", text="Email", anchor=W)
tree.column("#1", stretch=NO, width=70)
tree.column("#2", stretch=NO, width=50)
tree.column("#3", stretch=NO, width=100)
for person in people:
    tree.insert("", END, values=person)
scroll_bar = ttk.Scrollbar(orient="vertical", command=tree.yview)
tree.configure(yscroll=scroll_bar.set)
scroll_bar.grid(row=0, column=1, sticky="ns")
root.mainloop()
