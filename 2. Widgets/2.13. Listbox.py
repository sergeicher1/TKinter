languages = ["Python", "JavaScript", "C#", "Java"]
languages_var = Variable(value=languages)

languages_listbox = Listbox(listvariable=languages_var)
languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)


from tkinter import *
from tkinter import ttk


def delete():
    selection = languages_listbox.curselection()
    languages_listbox.delete(selection[0])


def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)


root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
root.columnconfigure(index=0, weight=4)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)
root.rowconfigure(index=2, weight=1)

language_entry = ttk.Entry()
language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
ttk.Button(text="Add", command=add).grid(column=1, row=0, padx=6, pady=6)

languages_listbox = Listbox()
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)
languages_listbox.insert(END, "Python")
languages_listbox.insert(END, "C#")
ttk.Button(text="DELETE", command=delete).grid(row=2, column=1, padx=5, pady=5)
root.mainloop()
def add():
    new_language = language_entry.get()
    # languages_listbox.insert(0, new_language)
    languages.append(new_language)
    languages_var.set(languages)
root.columnconfigure(index=0, weight=4)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)



from tkinter import *
from tkinter import ttk



root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
def selected(event):
    selected_indeces = languages_listbox.curselection()
    selected_langs = ",".join([languages_listbox.get(i) for i in selected_indeces])
    msg = f"You've selected: {selected_langs}"
    selection_label["text"] = msg


languages = ["Python", "C#", "JAVA", "JS"]
languages_var = StringVar(value=languages)
selection_label = ttk.Label()
selection_label.pack(anchor=NW, fill=X, padx=5, pady=5)

languages_listbox = Listbox(listvariable=languages_var,selectmode=EXTENDED)
languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
languages_listbox.bind("<<ListboxSelect>>", selected)
root.mainloop()



from tkinter import *

from tkinter import ttk


root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

languages = ["Python", "C#", "JAVA", "JS"]
languages_var = StringVar(value=languages)

languages_listbox = Listbox(listvariable=languages_var, selectmode=EXTENDED)
languages_listbox.pack(expand=1, fill=BOTH)
languages_listbox.select_set(first=1, last=2)
root.mainloop()
