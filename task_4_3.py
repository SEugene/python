from requests import get
from datetime import date
from decimal import Decimal


def currency_rates(cur_cc):
    """
    Реализована с использованием только только методов класса str
    :param cur_cc: код валюты (<CharCode>), регистр не имеет значения
    :return: курс запрошенной валюты к рублю (с учетом номинала) в формае Decimal
             и дата из отчета сервера в формате date
    """
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    for idx in content.split('ID='):
        if idx.startswith('<?xml'):
            cur_date = idx[idx.find('Date="') + len('Date="'):idx.find('" name')]
            cur_date = date(int(cur_date.split('.')[-1]), int(cur_date.split('.')[-2]), int(cur_date.split('.')[-3]))
            continue
        if idx.find(cur_cc.upper()) > 0:
            val = idx[idx.find('<Value>') + len('<Value>'): idx.find('</Value>')].replace(',', '.')
            nom = idx[idx.find('<Nominal>') + len('<Nominal>'): idx.find('</Nominal>')].replace(',', '.')
            return f'{cur_cc.upper()}: {Decimal(val) / Decimal(nom)}, date: {cur_date}'
            #break
    #return None


print(currency_rates('usd'))
print(currency_rates('EUR'))
print(currency_rates('NNN'))
print(currency_rates('jPy'))
