import re

pattern = re.compile(r'(.+)(?=[ -]{5}).+(?<=\[)(.+)(?=\]).+(?<=")(\w+[A-Z]).+(\/\w+\/\w+)'
                     r'.+(?<=\d"\s)(\d+).+(?<=\d"\s\d{3}\s)(\d+)')

with open('nginx_logs.txt', 'r', encoding='utf-8') as source:
    for line in source:
        res_tuple = pattern.search(line).groups()
