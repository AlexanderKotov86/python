number = input('Введите число на английском языке: ')


def num_translate(number):
    """This function translates English numbers from 1 to 10 in Russian"""

    dict_numbers = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    translate_number_raw = dict_numbers.get(str.lower(number))
    if str.isupper(number[0]):
        translate_number = str.capitalize(translate_number_raw)
    else:
        translate_number = translate_number_raw
    print(translate_number)


num_translate(number)
