def personal_sum(numbers):
    """
    :return: result - сумма чисел, incorrect_data - кол-во некорректных данных.
    """
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result, incorrect_data


def calculate_average(numbers):
    """
    count_numbers - список из чисел, переданных в numbers
    """
    try:
        total = personal_sum(numbers)
        count_numbers = [i for i in numbers if isinstance(i, int) or isinstance(i, float)]
        mean_arithmetic = total[0] / len(count_numbers)  # среднее арифметическое = возьмем сумму чисел/кол-во чисел
        return mean_arithmetic
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных.')


# Пример выполнения программы:
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
