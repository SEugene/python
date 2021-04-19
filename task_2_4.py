staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names = []
for idx in staff:
    ar = idx.split(' ')
    name = ar.pop().capitalize()
    print(f'Привет, {name}!')
    names.append(name)             # Необязательная операция. Список имен можно не создавать
print(names)
print()
