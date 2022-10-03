import math


def payment_percent_for_saving(label, begin_coast, save_date, month_pay):
    month_date = save_date * 12
    end_coast = month_date * month_pay
    x1 = -math.pow(end_coast / begin_coast, 1 / month_date) - 1
    x2 = math.pow(end_coast / begin_coast, 1 / month_date) - 1

    print(x2 * 100, x2 * 100 * 12)
    label(text='Percent for storage per month:'+str(round(x2 * 100, 4))+'\n'+'Percent for storage per year:'+str(round(x2 * 100 * 12, 4)))


def date_save(label, percent, month_pay, begin_coast):
    operation_cost = month_pay / ((1 + ((percent / 12)/100)) ** 1)
    date = begin_coast / (operation_cost)

    print(date)
    label(text='Storage term:' + str(round(date, 0)) + ' days')


def find_begin_coast(label, save_date, month_pay, percent):
    month_date = save_date * 12
    month_percent = percent/12
    begin_coast = (month_pay*month_date) / ((float(1) + month_percent / 100) ** month_date)

    print(begin_coast)
    label(text='Begin coast:' + str(round(begin_coast, 4)) + '$')
