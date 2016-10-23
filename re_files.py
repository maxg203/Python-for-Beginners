import re

text = open('shakespeare.txt')

for line in text:
    line = line.rstrip()
    if re.search('^[A-Z]{3,6}.*$', line):
        print(line)

# Regular Expressions
'^[A-Z]{3,6}.*$'
'^[A-Z]{6}.*$'
'^[A-Z]{6}.+$'
'^[A-Z]{5}.+$'
'^A.+again.$'
'^T.+t.+!$'
