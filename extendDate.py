#3. Write a python program to extract the date and year from a given string.
#(use standard function)

import re, datetime
s = "I have a meeting on 2018-12-10 in New York"
match = re.search('\d{4}-\d{2}-\d{2}', s)
date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
print(date)