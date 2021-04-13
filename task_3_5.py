import random


def get_jokes(n, fl='нет'):
    """
    Функция выбирает 3 случайных элемента - по одному из каждого списка и объединяет их в шуточную фразу.
    Если слова в шутках не повторяются, количество шуток ограничено количеством слов в каждом из списков - 5
    Для выполнения условия "нет повторений, слова случайны" использовано перемешивание списков /random.shuffle/
    с последующим их склеиванием через zip
    Если слова в шутках повторяются, используется метод .choice
    Фразы в количестве от 1 до n записываются в новый список
    :param n: количество шуток, которые можно сгенерировать (<=5 при fl = "нет")
    :param fl: допускаются ли повторения - да / нет
    :return: список с n шутками для последующей обработки в основном коде
    """
    jokes = []
    random.shuffle(nouns)
    random.shuffle(adverbs)
    random.shuffle(adjectives)
    if fl == 'нет':
        if n >= 5:
            n = 5
        for noun, adverb, adjective in zip(nouns, adverbs, adjectives):
            jokes.append(f'{noun} {adverb} {adjective}')
    for idx in range(n):
        jokes.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')

    return jokes[:n]


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(f'Вызов функции с указанием только аргумента n = 8 (шуток 5, т.к. fl = "нет" по умолчанию)\n{get_jokes(8)}\n')
print(f'Вызов функции со значением аргументов n = 6, fl = "да" \n{get_jokes(fl="да", n=6)}\n')
