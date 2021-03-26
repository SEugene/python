from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Людмила', 'Станислав']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tuple_gen = zip_longest(tutors, klasses, fillvalue=None)

print(f'тип "tuple_gen": {type(tuple_gen)}\n')
for _ in range(len(tutors)+1):
    print(next(tuple_gen))
