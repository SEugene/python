import os

with open('config.yaml', 'r', encoding='utf-8') as source:
    for line in source.readlines():
        dir_name, file_name = os.path.split(line.strip())
        try:
            os.makedirs(dir_name)
        except FileExistsError as e:
            print(f'concrete error: {e}')
        with open(f'{line.strip()}', 'w'):
            pass
