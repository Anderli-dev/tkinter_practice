def validate_input_data(func):
    def wrapper_check_input(change_text, *args):
        # this for check all string on correctness
        for i in args:
            if not is_digit(i):
                if i.replace(" ", "") == '':
                    change_text(text='Some input is empty')
                else:
                    change_text(text='Data contain letters!!!')
                return 0

        # this is for the number to check on the negative
        for i in args:
            if not float(i) >= 0:
                change_text(text='Data contain negative numbers!!!')
                return 0
        func(change_text, float(args[0]), float(args[1]), float(args[2]))
    return wrapper_check_input


def is_digit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
