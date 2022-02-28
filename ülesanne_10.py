# Ülesanne 10
# Matis Russi
# IT-21
# 28.02.2022

# Moodulid

import re

# IP väljastamine

fh = open('lorem.txt')

for line in fh:
    if re.search("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", line):
         print(line,end='')

print('─────────────────')

# Parool

fh = open('lorem.txt')

for parool in fh:
    if re.search('^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$', parool):
         print(parool,end='')