def num_translate_adv(num, vocabulary):
    result = voc.get(num.lower())
    if num.istitle():
        result = result.capitalize()
    return result


voc = {'zero': 'ноль',
       'one': 'один',
       'two': 'два',
       'three': 'три',
       'four': 'четыре',
       'five': 'пять',
       'six': 'шесть',
       'seven': 'семь',
       'eight': 'восемь',
       'nine': 'девять'}

number = input('Введите числительное от 0 до 9 на английском языке: ')
print(num_translate_adv(number, voc))
