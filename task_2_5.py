prices = [25.2, 33.02, 15, 48.05, 101.3, 224, 51.4, 7.6, 125.08, 200.4, 83.04, 97.9, 65.03]
price_str = []
for idx in range(len(prices)):
    pr_st = [str(round(prices[idx] * 100 // 100)), f' руб {round(prices[idx] * 100 % 100):02d} коп']
    price_str.append(''.join(pr_st))

print(f'\nЗадание 5А \n{price_str}')

print(f'\nЗадание 5B')
print(f'Начальный список: {prices}, адрес: {id(prices)}')
prices.sort()
print(f'Отсортированный список: {prices}, адрес: {id(prices)}')

prices = [25.2, 33.02, 15, 48.05, 101.3, 224, 51.4, 7.6, 125.08, 200.4, 83.04, 97.9, 65.03]
sorted_pr = sorted(prices, reverse=True)
print(f'\nЗадание 5С')
print(f'Начальный список: {prices}, адрес: {id(prices)}')
print(f'Отсортированный список: {sorted_pr}, адрес: {id(sorted_pr)}')

prices = [25.2, 33.02, 15, 48.05, 101.3, 224, 51.4, 7.6, 125.08, 200.4, 83.04, 97.9, 65.03]
print(f'\nЗадание 5D')
prices.sort()
print(f'5 наиболее дорогих товара по возрастанию цены: {prices[-5:]}')
