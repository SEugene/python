import os
import collections
import json


def num_digits(number):
    # функция для подсчета количества цифр в числе
    counter = 1
    while number > 0:
        if number // 10 > 0:
            counter += 1
            number = number // 10
        else:
            break
    return counter


intermed_dict = collections.defaultdict(list)
for root, dirs, files in os.walk('D:/Info/GeekBrains/PY_tests/Seltcov_Eugene_dz_7'):
    for file in files:
        if not file.startswith('.'):
            head, exts = os.path.splitext(file)
            intermed_dict[(10 ** num_digits(os.path.getsize(os.path.join(root, file))))].append(exts)

final_dictionary = dict.fromkeys(sorted(intermed_dict.keys()))
for key in intermed_dict.keys():
    c = collections.Counter()
    for word in intermed_dict[key]:
        c[word] += 1
    final_dictionary.update({key: (sum(c.values()), list(c))})

with open(f'{os.path.basename(os.getcwd())}_summary.json', 'w', encoding='utf-8') as sum_file:
    json.dump(final_dictionary, sum_file)
