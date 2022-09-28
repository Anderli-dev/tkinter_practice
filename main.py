from tkinter import *
from callbacks import *

window = Tk()

window['bg'] = '#e8e8e8'
window.title('')
window.geometry('1280x720')


input_border = Frame(master=window, background='#6b6b6b', borderwidth=0)
input_frame = Frame(master=input_border, background='#e8e8e8')

second_input_grid = Frame(master=input_frame, background='#e8e8e8')
second_input_grid.grid(row=1, column=1, sticky='w')

input_label = Label(master=second_input_grid, text='Початкова вартість:', background='#e8e8e8')
input_label.grid(row=1, column=1, sticky='w')
begin_coast = Entry(master=second_input_grid, width=20, font=('Arial', 14))
begin_coast.focus_set()
begin_coast.grid(row=1, column=2, sticky='w', padx=5, pady=5)


input_label = Label(master=second_input_grid, text='Tермін зберігання:', background='#e8e8e8')
input_label.grid(row=2, column=1, sticky='w')
save_date = Entry(master=second_input_grid, width=20, font=('Arial', 14))
save_date.grid(row=2, column=2, sticky='w', padx=5, pady=5)


input_label = Label(master=second_input_grid, text='Щомісячна плата:', background='#e8e8e8')
input_label.grid(row=3, column=1, sticky='w')
month_pay = Entry(master=second_input_grid, width=20, font=('Arial', 14))
month_pay.grid(row=3, column=2, sticky='w', padx=5, pady=5)


input_label = Label(master=second_input_grid, text='% за зберігання в рік:', background='#e8e8e8')
input_label.grid(row=4, column=1, sticky='w')
percent = Entry(master=second_input_grid, width=20, font=('Arial', 14))
percent.grid(row=4, column=2, sticky='w', padx=5, pady=5)


input_frame.pack(fill=X)
input_border.pack(fill=X)



answer_grid = Frame(master=input_frame, background='#e8e8e8')
answer_grid.grid(row=1, column=2, sticky='n')

a_label = Label(master=answer_grid, text='Відповідь:', background='#e8e8e8')
a_label.grid(row=1, column=1, sticky='w')


answer_label = Label(master=answer_grid, text='', background='#e8e8e8')
answer_label.grid(row=1, column=2, sticky='w')



input_grid = Frame(master=input_frame, background='#e8e8e8')
input_grid.grid(row=2, column=1, sticky='w')

input_btn1 = Button(master=input_grid,
                   text='Знайти % за зберігання продукції.',
                   command=lambda: payment_percent_for_saving(answer_label, float(begin_coast.get()), float(save_date.get()), float(month_pay.get())))
input_btn1.grid(row=1, column=1, sticky='w')

input_btn2 = Button(master=input_grid,
                   text='Знайти термін зберігання продукції.',
                   command=lambda: date_save(answer_label, float(percent.get()), float(month_pay.get()), float(begin_coast.get())))
input_btn2.grid(row=2, column=1, sticky='w')

input_btn3 = Button(master=input_grid,
                   text='Знайти початкову вартість зберігання продукції.',
                   command=lambda: find_begin_coast(answer_label, float(save_date.get()), float(month_pay.get()), float(percent.get())))
input_btn3.grid(row=3, column=1, sticky='w')


window.mainloop()
