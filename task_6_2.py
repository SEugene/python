with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    head, center, tail = line.partition(' ')
    ips = {head: 1}
    max_times = 1
    spamer = head
    while line:
        line = f.readline()
        head, center, tail = line.partition(' ')
        if head in ips.keys():
            ips[head] += 1
        else:
            ips[head] = 1
        if ips[head] > max_times:
            max_times = ips[head]
            spamer = head

    print(f'IP-адрес спамера: {spamer}, количество запросов спамера: {max_times}')
