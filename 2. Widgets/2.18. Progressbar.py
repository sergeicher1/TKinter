from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

ttk.Progressbar(orient="vertical", length=100, value=10).pack(pady=5)
ttk.Progressbar(orient="horizontal", length=150, value=20).pack(pady=5)

value_var = IntVar(value=30)
progrssbar = ttk.Progressbar(orient="horizontal", variable=value_var)
progrssbar.pack(fill=X, padx=5, pady=5)

label = ttk.Label(textvariable=value_var)
label.pack(anchor=NW, padx=6, pady=6)
root.mainloop()


from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")

value_var = IntVar()
progressbar = ttk.Progressbar(orient="horizontal", variable=value_var)
progressbar = ttk.Progressbar(orient="horizontal", mode="indeterminate")
progressbar.pack(fill=X, padx=10, pady=10)

label = ttk.Label(textvariable=value_var)
label.pack(anchor=NW, padx=6, pady=6)

def start(): progressbar.start(100)
def stop(): progressbar.stop()

start_btn = ttk.Button(text="Start", command=start)
start_btn = ttk.Button(text="Start", command=progressbar.start)
start_btn.pack(anchor=SW, side=LEFT, padx=10, pady=10)
stop_btn = ttk.Button(text="Stop", command=stop)
stop_btn = ttk.Button(text="Stop", command=progressbar.stop)
stop_btn.pack(anchor=SE, side=RIGHT, padx=10, pady=10)



root.mainloop()
