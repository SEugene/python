import re


def email_parse(email_address):
    try:
        pattern = re.compile(r'(?P<username>[\w|а-яА-ЯЁё]+)(?=@).(?<=[&@])(?P<domain>\w+\.\w{2,3})')
    except Exception:
        raise ValueError
    return pattern.search(email_address).groupdict()


if __name__ == '__main__':
    email_adrs = 'User_name_20@mail.рф'
    try:
        print(email_parse(email_adrs))
    except Exception as e:
        print(f'ValueError: wrong email: {email_adrs}')
