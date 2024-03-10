from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
for theme in ttk.Style().theme_names():
    print(theme)
ttk.Style().theme_use("classic")
ttk.Button(text="Click").pack(anchor=CENTER, expand=1)

selected_theme = StringVar()
style = ttk.Style()


def change_theme():
    style.theme_use(selected_theme.get())


ttk.Label(textvariable=selected_theme, font="Helvetica 40").pack(anchor=NW)

for theme in style.theme_names():
    ttk.Radiobutton(text=theme, value=theme, variable=selected_theme, command=change_theme).pack(anchor=NW)
root.mainloop()
