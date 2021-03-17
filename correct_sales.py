from sys import argv
with open('bakery.csv', 'r+', encoding='utf-8') as fc:
    # находим последнюю строку - при вводе номера больше последней строки - сбой
    fc.seek(0, 2)
    last_line = fc.tell() // 20
    fc.seek(0)

    if int(argv[1]) > last_line:
        print('Такой строки в файле нет')
    else:
        fc.seek((int(argv[1]) - 1) * 20)
        fc.write(''.join(argv[2:]).rjust(18) + '\n')
