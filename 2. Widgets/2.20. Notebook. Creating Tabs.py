from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)
python_logo = PhotoImage(file="../python.png")
java_logo = PhotoImage(file="../java.png")
csharp_logo = PhotoImage(file="../csharp.png")
notebook.add(frame1, text="Pyhon", image=python_logo, compound=LEFT)
notebook.add(frame2, text="JAVA", image=java_logo, compound=LEFT)
notebook.add(frame3, text="CSharp", image=csharp_logo, compound=LEFT)



root.mainloop()
