odd_cubed_list = []
new_list = []

# for ind in range(1000):
#     if ind % 2 != 0:
#         odd_cubed_list.append(ind**3)

for ind in range(1, 1001, 2):              # так код получился короче на 1 строку - не нужно ветвление
    odd_cubed_list.append(ind ** 3)

for ind2 in range(len(odd_cubed_list)):
    res_sum = 0
    counter = odd_cubed_list[ind2]
    while counter > 0:
        res_sum = res_sum + counter % 10
        counter = counter // 10
    if res_sum % 7 == 0:
        new_list.append(odd_cubed_list[ind2])
print()
print('ИТОГОВЫЙ список, состоящий из чисел, сумма цифр в которых кратна 7.')
print('Числа получены возведением в куб нечетных чисел в диапазоне от 0 до 1000:')
print(new_list)
print()

for ind3 in range(len(odd_cubed_list)):
    odd_cubed_list[ind3] += 17

for ind4 in range(len(odd_cubed_list)-1, -1, -1):  # цикл нужно запускать с конца диапазона, так как алгоритм
    res_sum = 0                                    # выбрасывает числа, некратные 7, сокращая список
    if ind4 <= len(odd_cubed_list):
        counter = odd_cubed_list[ind4]             # дополнительная переменная counter нужна, чтобы она изменялась в
    while counter > 0:                             # последующем цикле while, а элемент списка оставался неизменным
        res_sum += counter % 10
        counter = counter // 10                    # в Интернете нашел более лаконичный вариант counter //= 10
    if res_sum % 7 != 0:
        odd_cubed_list.pop(ind4)
print('Второй ИТОГОВЫЙ список, состоящий из чисел, сумма цифр в которых кратна 7.')
print('Числа получены увеличением каждого элемента изначального списка кубов нечетных чисел на 17:')
print(odd_cubed_list)
