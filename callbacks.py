"""
    Functions for calculating answer
"""

import math
from validate_input_data import validate_input_data


@validate_input_data
def payment_percent_for_saving(change_text, begin_coast, save_date, month_pay):
        month_date = save_date * 12
        end_coast = month_date * month_pay
        x1 = -math.pow(end_coast / begin_coast, 1 / month_date) - 1
        x2 = math.pow(end_coast / begin_coast, 1 / month_date) - 1

        print(x2 * 100, x2 * 100 * 12)
        if x2 * 100 < 0:
            change_text(text='Percent is negative'
                             + '\n' +
                             'Check data')
        else:
            change_text(text='Percent for storage per month: ' + str(round(x2 * 100, 4))
                             + '\n' +
                             'Percent for storage per year:' + str(round(x2 * 100 * 12, 4)))


@validate_input_data
def date_save(change_text, percent, month_pay, begin_coast):
    operation_cost = month_pay / ((1 + ((percent / 12)/100)) ** 1)
    date = begin_coast / operation_cost
    print(date)

    change_text(text='Storage term: ' + str(round(date, 1)) + ' days')


@validate_input_data
def find_begin_coast(change_text, save_date, month_pay, percent):
    month_date = save_date * 12
    month_percent = percent/12
    begin_coast = (month_pay*month_date) / ((float(1) + month_percent / 100) ** month_date)

    print(begin_coast)
    change_text(text='Begin coast: ' + str(round(begin_coast, 4)))
