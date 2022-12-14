import tkinter as tk

from callbacks import *
from input import Input


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # set window initial parameters
        self.title('Tkinter practice')
        self.geometry('800x300')
        self.resizable(False, False)
        self.configure(background='#e8e8e8')

        MainPage(self)


class MainPage(tk.Frame):
    """ Block with 2 main part """
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, bg='#e8e8e8', *args, **kwargs)
        self.pack(fill='x', expand=True)
        self.columnconfigure(2, weight=1)

        # -------If in future will be needed to use border--------
        # input_border = tk.Frame(master=self, background='#6b6b6b', borderwidth=0)
        # input_border.pack(side='top', fill='both', expand=True)

        # creating global var for using in other part of program
        global answer_grid
        answer_grid = AnswerGrid(self)
        TaskFrame(master=self)


class TaskFrame(tk.Frame):
    """ Block with buttons and inputs """
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, bg='#e8e8e8', *args, **kwargs)
        self.grid(row=1, column=1)

        input_grid = InputGrid(self)
        # use this variable to collect data by buttons
        ButtonsGrid(master=self, input_grid=input_grid)


class InputGrid(tk.Frame):
    """ Inputs block """
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


class ButtonsGrid(tk.Frame):
    """ Buttons block """
    def __init__(self, input_grid, *args, **kwargs):
        tk.Frame.__init__(self, bg='#e8e8e8', *args, **kwargs)
        self.grid(row=2, column=1, pady=(10, 0))

        self.input_grid = input_grid

        global answer_grid
        self.answer_grid = answer_grid

        tk.Button(master=self,
                  text='Find % for storage per year.',
                  command=lambda: payment_percent_for_saving(
                      answer_grid.change_text,
                      input_grid.begin_coast.entry.get(),
                      input_grid.save_date.entry.get(),
                      input_grid.month_pay.entry.get()
                  )).grid(row=1, column=1, sticky='ew')

        tk.Button(master=self,
                  text='Find storage term.',
                  command=lambda: date_save(
                      answer_grid.change_text,
                      input_grid.percent.entry.get(),
                      input_grid.month_pay.entry.get(),
                      input_grid.begin_coast.entry.get()
                  )).grid(row=2, column=1, sticky='ew')

        tk.Button(master=self,
                  text='Find begin coast.',
                  command=lambda: find_begin_coast(
                      answer_grid.change_text,
                      input_grid.save_date.entry.get(),
                      input_grid.month_pay.entry.get(),
                      input_grid.percent.entry.get()
                  )).grid(row=3, column=1, sticky='ew')


class AnswerGrid(tk.Frame):
    """ Answer block """
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, bg='#e8e8e8', *args, **kwargs)
        self.grid(row=1, column=2, sticky='nsew')
        self.columnconfigure(0, weight=1)

        a_label = tk.Label(master=self, font=('Arial', 16), text='ANSWER', background='#e8e8e8')
        a_label.grid(sticky='ew')

        self.answer_label = tk.Label(master=self, font=('Arial', 16), text='', background='#e8e8e8')
        self.answer_label.grid()

    # this function gives button ability to change text when clicked
    def change_text(self, text):
        self.answer_label.config(text=text)


if __name__ == '__main__':
    app = App()
    app.mainloop()
