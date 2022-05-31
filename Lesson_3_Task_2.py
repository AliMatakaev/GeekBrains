def num_translate_adv(a):
    num_dict = {
        'one': 'один',
        'One': 'Один',
        'two': 'два',
        'Two': 'Два',
        'three': 'три',
        'Three': 'Три',
        'four': 'четыре',
        'Four': 'Четыре',
        'five': 'пять',
        'Five': 'Пять',
        'six': 'шесть',
        'Six': 'Шесть',
        'seven': 'семь',
        'Seven': 'Семь',
        'eight': 'восемь',
        'Eight': 'Восемь',
        'nine': 'девять',
        'Nine': 'Девять',
        'ten': 'десять',
        'Ten': 'Десять',
        'zero': 'ноль',
        'Zero': 'Ноль',
}
    if a in num_dict:
        result = num_dict[a]
        print(result)
    else:
        print('None')
num_translate_adv('Seven')

