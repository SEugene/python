duration = [38, 25, 74, 255, 3600, 5000, 70000, 100000, 1000000, 5000000, 25000000, 50000000, 500000400]

for ind in duration:
    print('Промежуток времени {} сек, что составляет:'.format(ind))
    years = ind // 31536000
    months = ind % 31536000 // 2592000
    days = ind % 31536000 % 2592000 // 86400
    hours = ind % 31536000 % 2592000 % 86400 // 3600
    minutes = ind % 31536000 % 2592000 % 86400 % 3600 // 60
    seconds = ind % 31536000 % 2592000 % 86400 % 3600 % 60
    if ind >= 31536000:
        print('{} лет, {} мес, {} дн, {} час, {} мин, {} сек'.format(years, months, days, hours, minutes, seconds))
    elif ind >= 2592000:
        print('{} мес, {} дн, {} час, {} мин, {} сек'.format(months, days, hours, minutes, seconds))
    elif ind >= 86400:
        print('{} дн, {} час, {} мин, {} сек'.format(days, hours, minutes, seconds))
    elif ind >= 3600:
        print('{} час, {} мин, {} сек'.format(hours, minutes, seconds))
    elif ind >= 60:
        print('{} мин, {} сек'.format(minutes, seconds))
    else:
        print('{} сек'.format(seconds))
