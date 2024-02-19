import tkinter as tk
from tkinter import ttk


class Keypad(tk.Frame):
    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        # set style of frame and button
        style = ttk.Style()
        style.configure("My1.TFrame", background="#CD5C5C")
        style.configure("My2.TFrame", background="#F08080")
        style.configure("Display.TFrame", background="white")
        style.configure("My.TButton", background="violet", padding=(10, 20),
                        font=("Arial", 12))
        style.configure("Color.TLabel", background="#FA8072",
                        foreground="black", font=("Arial", 36))

        # create frame
        self.display_frame = ttk.Frame(relief="flat", style="Display.TFrame")
        self.num_frame = ttk.Frame(self, relief="groove", borderwidth=2,
                                   style="My1.TFrame")
        self.op_frame = ttk.Frame(self, relief="groove", borderwidth=2,
                                  style="My2.TFrame")
        self.display_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.num_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.op_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        num_keys = self.keynames
        op_keys = ['*', '/', '+', '-', '^', '=']
        self.num_buttons = []
        self.op_buttons = []

        options = {'sticky': tk.NSEW}

        # Display label
        self.display_label = ttk.Label(self.display_frame, text="", anchor="e",
                                       style="Color.TLabel")
        self.display_label.pack(fill=tk.BOTH, expand=True)

        # create button for num_frame
        for i, key in enumerate(num_keys):
            button = ttk.Button(self.num_frame, text=key, width=10,
                                style="My.TButton",
                                command=lambda key=key: self.update_display(
                                    key))
            button.grid(row=(i // columns), column=(i % columns), padx=5,
                        pady=5, **options)
            self.num_buttons.append(button)

        # create button for op_frame
        for i, key in enumerate(op_keys):
            button = ttk.Button(self.op_frame, text=key, width=10,
                                style="My.TButton",
                                command=lambda key=key: self.update_display(
                                    key))
            button.grid(row=i, column=0, padx=5, pady=5, **options)
            self.op_buttons.append(button)

        # num_frame's row&column configure
        for i in range(len(num_keys)):
            self.num_frame.rowconfigure(i // columns, weight=1)
            self.num_frame.columnconfigure(i % columns, weight=1)

        # op_frame's row&column configure
        self.op_frame.columnconfigure(0, weight=1)
        for i in range(len(op_keys)):
            self.op_frame.rowconfigure(i, weight=1)

    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        for child in self.num_buttons:
            if isinstance(child, ttk.Button):
                child.bind(sequence, func, add)
        for child in self.op_buttons:
            if isinstance(child, ttk.Button):
                child.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        style = ttk.Style()
        for child in self.num_buttons:
            if isinstance(child, ttk.Button):
                style.configure(child.cget('style'), **{key: value})
        for child in self.op_buttons:
            if isinstance(child, ttk.Button):
                style.configure(child.cget('style'), **{key: value})

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        style = ttk.Style()
        for child in self.num_buttons:
            if isinstance(child, ttk.Button):
                return style.lookup(child.cget('style'), f"{key}")

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        style = ttk.Style()
        for key, value in kwargs.items():
            for child in self.num_buttons:
                if isinstance(child, ttk.Button):
                    style.configure(child.cget('style'), **{key: value})
            for child in self.op_buttons:
                if isinstance(child, ttk.Button):
                    style.configure(child.cget('style'), **{key: value})

    @property
    def frame(self):
        return self

    def update_display(self, text):
        current_text = self.display_label["text"]
        if text == "":
            # Clear the display if the button pressed is ""
            self.display_label["text"] = ""
        else:
            # Append the pressed key to the current text
            self.display_label["text"] = current_text + text