from sys import argv
with open('bakery.csv', 'r', encoding='utf-8') as fr:
    fr.seek(0, 2)
    last_line = fr.tell() // 20
    fr.seek(0)
    end = last_line
    if len(argv) == 1:
        start = 0
    elif len(argv) == 2:
        start = int(argv[1])
        fr.seek((start - 1) * 20)
    else:
        start = int(argv[1])
        fr.seek((start - 1) * 20-1)
        end = int(argv[2])
    print(start, end)

    print(fr.tell())
    for _ in range(end - start + 2):
        print(f'{fr.readline().strip().lstrip()}')
