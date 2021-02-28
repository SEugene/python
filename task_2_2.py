phrase = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_phrase = []
dig_el = []                                         # вспомогательный список для вывода фразы без лишних пробелов
for idx in range(len(phrase)):
    if not(phrase[idx].isalnum()):
        new_phrase.append('"')
        dig_el.append(idx+new_phrase.count('"'))
        ar = list(phrase[idx])
        if len(phrase[idx]) < 3:
            ar.insert(1, '0')
        phrase[idx] = ''.join(ar)
        new_phrase.append(phrase[idx])
        new_phrase.append('"')
    elif phrase[idx].isdigit():
        new_phrase.append('"')
        dig_el.append(idx+new_phrase.count('"'))
        if len(phrase[idx]) < 2:
            new_phrase.append('0' + phrase[idx])
        else:
            new_phrase.append(phrase[idx])
        new_phrase.append('"')
    else:
        new_phrase.append(phrase[idx])
print(new_phrase)

for idx_2 in dig_el:                                # часть кода для вывода на печать фразы без лишних пробелов
    new_phrase[idx_2] = f'"{new_phrase[idx_2]}"'    # до и после числовых элементов
for idx_3 in reversed(dig_el):
    new_phrase.pop(int(idx_3+1))
    new_phrase.pop(int(idx_3-1))


print(' '.join(new_phrase))
