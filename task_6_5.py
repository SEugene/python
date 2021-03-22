from sys import argv
with open(argv[1], 'r', encoding='utf-8') as fu, open(argv[2], 'r', encoding='utf-8') as fh:
    with open(argv[3], 'a', encoding='utf-8') as ff:
        line = fh.readline().strip()
        while line:
            line_2 = fu.readline().strip()
            if len(line_2) < 2:
                mistake = 1 / 0                       # для выполнения условия "выйти с кодом 1, если количество
                break                                 # пользователей меньше, чем количество хобби
            ff.write(f'{line_2}: {line}\n')
            line = fh.readline().strip()

        line = fu.readline().strip()
        while line:
            ff.write(f'{line}: {None}\n')
            line = fu.readline().strip()
