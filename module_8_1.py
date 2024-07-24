def add_everything_up(a, b):
    """
    :param a - может быть как числами(int, float), так и строками(str)
    :param b - может быть как числами(int, float), так и строками(str)
    """
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
