from sys import argv
with open('bakery.csv', 'a', encoding='utf-8') as fw:
    fw.write(''.join(argv[1:]).rjust(18) + '\n')
