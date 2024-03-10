

root.grid_rowconfigure(index=0, weight=1)
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=1)
text_editor = Text()
text_editor.grid(column=0, columnspan=2, row=0)


def open_file():
    file_path = filedialog.askopenfilename()
    if file_path != "":
        with open(file_path, "r") as file:
            text = file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)


def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path != "":
        text = text_editor.get("1.0", END)
        with open(file_path, "w") as file:
            file.write(text)


open_button = ttk.Button(text="Open File", command=open_file)
open_button.grid(column=0, row=1, sticky=NSEW, padx=10)
save_button = ttk.Button(text="Save File", command=save_file)
save_button.grid(column=1, row=1, sticky=NSEW, padx=10)

label = ttk.Label(text="Hello World!")
label.pack(anchor=NW, padx=10, pady=10)

def font_changed(font):
    label["font"] = font

def select_font():
    root.tk.call("tk", "fontchooser", "configure", "-font", label["font"], "-command", root.register(font_changed))
    root.tk.call("tk", "fontchooser", "show")
open_button = ttk.Button(text="Select a font", command=select_font)
open_button.pack(anchor=NW, padx=1, pady=10)



from tkinter import *
from tkinter import colorchooser
from tkinter import ttk

root = Tk()
root.title("Hello HERO!")
root.geometry("300x300+800+500")
label = ttk.Label(text="Hello World!")
label.pack(anchor=NW, padx=10, pady=10)
def select_coloor():
    result = colorchooser.askcolor(initialcolor="green")
    label["foreground"] = result[1]
open_button = ttk.Button(text="Select a color", command=select_coloor)
open_button.pack(anchor=NW, padx=1, pady=10)
root.mainloop()
