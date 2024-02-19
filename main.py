import tkinter as tk
from keypad_ui import KeypadUI

keys = list('789456123 0.')  # = ['7','8','9',...]

root = tk.Tk()
root.title("Calculator")
keypad = KeypadUI(root, keynames=keys, columns=3)
keypad.pack(expand=True, fill=tk.BOTH)
root.mainloop()