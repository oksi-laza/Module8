class Car:
    """
    :param model (str) - название автомобиля
    :param __vin (int) - vin-номер автомобиля
    :param __numbers (str) - номер автомобиля
    """
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):
        """
        Метод проверяет на корректность vin_number
        :return: True, если vin_number корректный, в других случаях выбрасывает исключение
        """
        if not isinstance(vin_number, int):  # если передано не целое число
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif not vin_number in range(1000000, 10000000, 1):  # если число не в диапазоне от 1млн. до 9999999 включ-но
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        """
        Метод проверяет корректное введение типа данных для номера и его длину
        :return: True, если номер корректный,  в других случаях выбрасывает исключение
        """
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message  # подробное описание ошибки


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message    # подробное описание ошибки


# Пример выполняемого кода:
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
