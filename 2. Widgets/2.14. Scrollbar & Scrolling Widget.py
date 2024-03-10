from tkinter import *

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
languages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go", "C",
             "T-SQL", "PL-SQL", "Typescript", "Assembly", "Fortran"]

languages_var = StringVar(value=languages)
listbox = Listbox(listvariable=languages_var)
listbox.pack(fill=BOTH, expand=1)
listbox.yview_scroll(number=1, what="units")
root.mainloop()
