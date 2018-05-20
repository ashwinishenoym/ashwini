import re
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batwoman and batman')
print(mo1.group(1))
