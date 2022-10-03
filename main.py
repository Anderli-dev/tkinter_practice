import tkinter as tk

from callbacks import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # set window initial parameters
        self.title('Tkinter practice')
        self.geometry('1280x720')

        MainPage(self)


class MainPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self,  bg='#e8e8e8', *args, **kwargs)
        self.pack(side='top', fill='both', expand=True)

        # -------If in future will be needed to use border--------
        # input_border = tk.Frame(master=self, background='#6b6b6b', borderwidth=0)
        # input_border.pack(side='top', fill='both', expand=True)

        input_grid = InputGrid(self)
        answer_grid = AnswerGrid(self)
        ButtonsGrid(master=self, input_grid=input_grid, answer_grid=answer_grid)


class InputGrid(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self,  bg='#e8e8e8', *args, **kwargs)
        self.grid(row=1, column=1, sticky='w')


        input_label = tk.Label(master=self, text='Begin coast:', background='#e8e8e8')
        input_label.grid(row=1, column=1, sticky='w')
        self.begin_coast = tk.Entry(master=self, width=20, font=('Arial', 14))
        self.begin_coast.focus_set()
        self.begin_coast.grid(row=1, column=2, sticky='w', padx=5, pady=5)


        input_label = tk.Label(master=self, text='Storage term:', background='#e8e8e8')
        input_label.grid(row=2, column=1, sticky='w')
        self.save_date = tk.Entry(master=self, width=20, font=('Arial', 14))
        self.save_date.grid(row=2, column=2, sticky='w', padx=5, pady=5)


        input_label = tk.Label(master=self, text='Monthly payment:', background='#e8e8e8')
        input_label.grid(row=3, column=1, sticky='w')
        self.month_pay = tk.Entry(master=self, width=20, font=('Arial', 14))
        self.month_pay.grid(row=3, column=2, sticky='w', padx=5, pady=5)


        input_label = tk.Label(master=self, text='% for storage per year:', background='#e8e8e8')
        input_label.grid(row=4, column=1, sticky='w')
        self.percent = tk.Entry(master=self, width=20, font=('Arial', 14))
        self.percent.grid(row=4, column=2, sticky='w', padx=5, pady=5)


class AnswerGrid(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self,  bg='#e8e8e8', *args, **kwargs)
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

        input_btn1 = tk.Button(master=self,
                           text='Find % for storage per year.',
                           command=lambda: payment_percent_for_saving(answer_grid.change_text, float(input_grid.begin_coast.get()), float(input_grid.save_date.get()), float(input_grid.month_pay.get())))
        input_btn1.grid(row=1, column=1, sticky='w')

        input_btn2 = tk.Button(master=self,
                           text='Find storage term.',
                           command=lambda: date_save(answer_grid.change_text, float(input_grid.percent.get()), float(input_grid.month_pay.get()), float(input_grid.begin_coast.get())))
        input_btn2.grid(row=2, column=1, sticky='w')

        input_btn3 = tk.Button(master=self,
                           text='Find begin coast.',
                           command=lambda: find_begin_coast(answer_grid.change_text, float(input_grid.save_date.get()), float(input_grid.month_pay.get()), float(input_grid.percent.get())))
        input_btn3.grid(row=3, column=1, sticky='w')


if __name__ == '__main__':
    app = App()
    app.mainloop()
