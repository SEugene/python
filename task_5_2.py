MAX_NUM = 19
odds_to_MN = (num for num in range(1, MAX_NUM + 1) if num % 2 != 0)

for _ in range(int((MAX_NUM + 1) / 2)):
    print(next(odds_to_MN))
