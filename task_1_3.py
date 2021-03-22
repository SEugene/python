num_list = []
for num in range(21):
    num_list.append(num)

for ind in range(len(num_list)):
    last_num_hun = num_list[ind] % 100
    last_num_ten = num_list[ind] % 10
    if 10 < last_num_hun < 15:
        print('{} процентов'.format(num_list[ind]))
    elif 1 < last_num_ten < 5:
        print('{} процента'.format(num_list[ind]))
    elif last_num_ten == 1:
        print('{} процент'.format(num_list[ind]))
    else:
        print('{} процентов'.format(num_list[ind]))
# алгоритм решения получился универсальным - не зависящим от диапазона, ниже добавил код, который определяет
# склонение слова "процент" при вводе любого целого числа
rand_num = int(input('Введите любое целое число для проверки склонения слова "процент": '))
last_num_hun = rand_num % 100
last_num_ten = rand_num % 10
if 10 < last_num_hun < 15:
    print('{} процентов'.format(rand_num))
elif 1 < last_num_ten < 5:
    print('{} процента'.format(rand_num))
elif last_num_ten == 1:
    print('{} процент'.format(rand_num))
else:
    print('{} процентов'.format(rand_num))
