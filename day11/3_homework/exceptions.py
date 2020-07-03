
def zero_err():
    try:
        if y == 0 in user_div(x, y):
            raise ZeroDivisionError
    except ZeroDivisionError as err:
        print(f"На ноль делить нельзя! - {err}")