tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Людмила', 'Станислав']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

for _ in range(len(tutors) - len(klasses)):
    klasses.append(None)

tuple_gen = (tuple((tutors[idx], klasses[idx])) for idx in range(len(tutors)+1))

print(f'{type(tuple_gen)}\n')
for _ in range(len(tutors)):
    print(next(tuple_gen))
