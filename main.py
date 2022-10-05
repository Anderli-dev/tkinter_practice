import tkinter as tk

from callbacks import *
from input import Input


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # set window initial parameters
        self.title('Tkinter practice')
        self.geometry('1280x720')

        MainPage(self)


class MainPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, bg='#e8e8e8', *args, **kwargs)
        self.pack(side='top', fill='both', expand=True)

        # -------If in future will be needed to use border--------
        # input_border = tk.Frame(master=self, background='#6b6b6b', borderwidth=0)
        # input_border.pack(side='top', fill='both', expand=True)

        input_grid = InputGrid(self)
        answer_grid = AnswerGrid(self)
        ButtonsGrid(master=self, input_grid=input_grid, answer_grid=answer_grid)


class InputGrid(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, bg='#e8e8e8', *args, **kwargs)
        self.grid(row=1, column=1)

        self.begin_coast = Input(master=self, text='Begin coast:', focus_set=True)
        self.begin_coast.grid(row=1, column=1, sticky='ew', padx=5, pady=5)

        self.save_date = Input(master=self, text='Storage term:')
        self.save_date.grid(row=2, column=1, sticky='ew', padx=5, pady=5)

        self.month_pay = Input(master=self, text='Monthly payment:')
        self.month_pay.grid(row=3, column=1, sticky='ew', padx=5, pady=5)

        self.percent = Input(master=self, text='% for storage per year:')
        self.percent.grid(row=4, column=1, sticky='ew', padx=5, pady=5)


class AnswerGrid(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, bg='#e8e8e8', *args, **kwargs)
        self.grid(row=1, column=2, sticky='n')

        a_label = tk.Label(master=self, text='Answer:', background='#e8e8e8')
        a_label.grid(row=1, column=1, sticky='w')

        self.answer_label = tk.Label(master=self, text='', background='#e8e8e8')
        self.answer_label.grid(row=1, column=2, sticky='w')

    def change_text(self, text):
        self.answer_label.config(text=text)


class ButtonsGrid(tk.Frame):
    def __init__(self, input_grid, answer_grid, *args, **kwargs):
        tk.Frame.__init__(self, bg='#e8e8e8', *args, **kwargs)
        self.grid(row=2, column=1, sticky='w')

        self.input_grid = input_grid
        self.answer_grid = answer_grid

        tk.Button(master=self,
                  text='Find % for storage per year.',
                  command=lambda: payment_percent_for_saving(
                      answer_grid.change_text,
                      float(input_grid.begin_coast.entry.get()),
                      float(input_grid.save_date.entry.get()),
                      float(input_grid.month_pay.entry.get())
                  )).grid(row=1, column=1, sticky='w')

        tk.Button(master=self,
                  text='Find storage term.',
                  command=lambda: date_save(
                      answer_grid.change_text,
                      float(input_grid.percent.entry.get()),
                      float(input_grid.month_pay.entry.get()),
                      float(input_grid.begin_coast.entry.get())
                  )).grid(row=2, column=1, sticky='w')

        tk.Button(master=self,
                  text='Find begin coast.',
                  command=lambda: find_begin_coast(
                      answer_grid.change_text,
                      float(input_grid.save_date.entry.get()),
                      float(input_grid.month_pay.entry.get()),
                      float(input_grid.percent.entry.get())
                  )).grid(row=3, column=1, sticky='w')


if __name__ == '__main__':
    app = App()
    app.mainloop()
