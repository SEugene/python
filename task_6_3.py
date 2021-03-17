with open('users.csv', 'r', encoding='utf-8') as fu, open('hobby.csv', 'r', encoding='utf-8') as fh:
    usrs = (el.strip() for el in fu.readlines())
    hbby = (el.strip() for el in fh.readlines())
    res_dict = dict.fromkeys(usrs)
    new_dict = dict(zip(res_dict.keys(), hbby))
    res_dict.update(new_dict)
    if len((list(hbby))) > 0:
        next(usrs)

    print(res_dict)
