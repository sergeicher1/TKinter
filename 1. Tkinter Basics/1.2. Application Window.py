from tkinter import *

root = Tk()
root.update_idletasks()
print(root.geometry())
root.resizable(False, False)
root.minsize(200,150)

root.maxsize(400,300)
root.title("Hello HERO!")
root.iconbitmap("favicon.ico")
icon = PhotoImage(file="favicon.png")
root.iconphoto(False, icon)
root.geometry("800x500")


root.mainloop()