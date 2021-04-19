phrase = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
dig_el = []                                         # вспомогательный список для вывода фразы без лишних пробелов
idx = 0
while idx < len(phrase):
    if not(phrase[idx].isalnum()):
        ar = list(phrase[idx])
        if len(phrase[idx]) < 3:
            ar.insert(1, '0')
        phrase[idx] = ''.join(ar)
        phrase.insert(idx, '"')
        dig_el.append(idx+1)
        phrase.insert(idx + 2, '"')
        idx += 3
    elif phrase[idx].isdigit():
        ar = list(phrase[idx])
        if len(phrase[idx]) < 2:
            ar.insert(0, '0')
        phrase[idx] = ''.join(ar)
        phrase.insert(idx, '"')
        dig_el.append(idx+1)
        phrase.insert(idx + 2, '"')
        idx += 3
    else:
        idx += 1
print(phrase)
for idx_2 in dig_el:                                # часть кода для вывода на печать фразы без лишних пробелов
    phrase[idx_2] = f'"{phrase[idx_2]}"'            # до и после числовых элементов
for idx_3 in reversed(dig_el):
    phrase.pop(int(idx_3+1))
    phrase.pop(int(idx_3-1))

print(' '.join(phrase))
