from tkinter import *
from tkinter import ttk

root = Tk()
root.title("HERO!")
root.geometry("300x300+800+500")
for item in range(3): root.rowconfigure(index=item, weight=1)
for item2 in range(3): root.columnconfigure(index=item2, weight=1)
btn1 = ttk.Button(text="button 1")
btn1.grid(row=0,column=1, rowspan=2, ipadx=6, ipady=55,padx=5,pady=5)
btn2 = ttk.Button(text="button 2")
btn2.grid(row=0,column=0, ipadx=6, ipady=6,padx=5,pady=5)
btn3 = ttk.Button(text="button 3")
btn3.grid(row=1,column=0,  ipadx=6, ipady=6,padx=5,pady=5)
for item in range(3):
    for item2 in range(3):
        btn = ttk.Button(text=f"{item}, {item2}")
        btn.grid(row=item,column=item2, ipadx=6, ipady=6, padx=4, pady=4, sticky=NSEW)

root.mainloop()
