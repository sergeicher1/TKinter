from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
languages = ["Python", "C#", "JAVA", "Ruby"]
languages_var = StringVar(value=languages[0])

label = ttk.Label(textvariable=languages_var)
label.pack(anchor=NW, padx=6, pady=6)

combobox = ttk.Combobox(textvariable=languages_var, values=languages)
combobox.pack(anchor=NW, padx=6, pady=6)

print(combobox.get())
root.mainloop()



from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
languages = ["Python", "C#", "JAVA", "Ruby"]


def selected(event):
    selection = combobox.get()
    print(selection)
    label["text"] = f"You've selected {selection}"


label = ttk.Label()
label.pack(anchor=NW, fill=X, padx=5, pady=5)

combobox = ttk.Combobox(values=languages, state="readonly")
combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
combobox.bind("<<ComboboxSelected>>", selected)
root.mainloop()
