import tkinter as tk
from keypad import Keypad

keys = list('789456123 0.')  # = ['7','8','9',...]

root = tk.Tk()
root.title("Calculator")
keypad = Keypad(root, keynames=keys, columns=3)
keypad.pack(expand=True, fill=tk.BOTH)
root.mainloop()