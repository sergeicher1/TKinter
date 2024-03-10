from tkinter import *
from tkinter import ttk

root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")

position = {"padx": 6, "pady": 6, "anchor": NW}
python = "Python"
java = "Java"
javascript = "JavaScript"
lang = StringVar(value=java)
header = ttk.Label(textvariable=lang)
header.pack(**position)
python_btn = ttk.Radiobutton(text=python, value=python, variable=lang)
python_btn.pack(**position)
java_btn = ttk.Radiobutton(text=java, value=java, variable=lang)
java_btn.pack(**position)
javascript_btn = ttk.Radiobutton(text=javascript, value=javascript, variable=lang)
javascript_btn.pack(**position)
root.mainloop()


from tkinter import *
from tkinter import ttk

root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")

position = {"padx": 6, "pady": 6, "anchor": NW}
languages = ["Python", "JavaScript", "Java", "C#"]
selected_language = StringVar()
header = ttk.Label(text="Select your language")
header.pack(**position)


def select():
    header.config(text=f"Selected {selected_language.get()}")


for lang in languages:
    lang_btn = ttk.Radiobutton(text=lang, value=lang, variable=selected_language, command=select)
    lang_btn.pack(**position)

root.mainloop()


from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x600+800+500")
position = {"padx": 6, "pady": 6, "anchor": NW}
languages = [
    {"name" : "Python", "img" : PhotoImage(file="../python.png")},
    {"name": "CSharp", "img" : PhotoImage(file="../java.png")},
    {"name": "Java", "img" : PhotoImage(file="../csharp.png")},
]
lang = StringVar(value=languages[0]["name"])
header = ttk.Label(textvariable=lang)
header.pack(**position)
for i in languages:
    btn = ttk.Radiobutton(value=i["name"], text=i["name"] , variable=lang, image=i["img"], compound="top")
    btn.pack(**position)
root.mainloop()
