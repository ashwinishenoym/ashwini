import re
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batwowoman Batwoman')
print(mo1.group())
