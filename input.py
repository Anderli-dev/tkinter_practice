import tkinter as tk


class Input(tk.Frame):
    def __init__(self, text, focus_set=False, *args, **kwargs):
        tk.Frame.__init__(self, bg='#e8e8e8', *args, **kwargs)
        self.text = text
        self.grid_columnconfigure(1, weight=1)

        self.label = tk.Label(master=self, text=text, background='#e8e8e8')
        self.label.grid(row=1, column=1, sticky='w')

        self.space = tk.Frame(master=self,  bg='#e8e8e8', width=10)
        self.space.grid(row=1, column=2)

        self.entry = tk.Entry(master=self, width=20, font=('Arial', 14))
        self.entry.grid(row=1, column=3, sticky='e')

        if focus_set:
            self.entry.focus_set()
