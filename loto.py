import tkinter as tk
import time
import random






class myapp:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("loto")
        self.root.geometry("640x480")
        self.root.configure(background="black")
        self.loto= tk.Listbox(background="black",foreground="white")
        self.loto.pack(padx=10,pady=10)
        for a in range(10):
            self.loto.insert("0",str(random.randint(1,50)))


root=tk.Tk()
apps=myapp(root)
root.mainloop()