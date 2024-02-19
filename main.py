import tkinter as tk
from keypad_ui import Keypad_ui

keys = list('789456123 0.')  # = ['7','8','9',...]

root = tk.Tk()
root.title("Calculator")
keypad = Keypad_ui(root, keynames=keys, columns=3)
keypad.pack(expand=True, fill=tk.BOTH)
root.mainloop()