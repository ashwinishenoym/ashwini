##import re
##import os.path
##
##def file_to_str():
##	"""Returns the contents of filename as a string."""
##	f = open('numbers.txt')
##	return f.read()
##
##results = re.findall(r'\d{3}-\d{3}-\d{4}', file_to_str())
##print(results)
##print('Count :' + str(len(results)))

import re
import os.path

f = open('numbers.txt', 'r')
line=0
for word in f:

    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phoneNumRegex.search(word)

    if (mo):
            print("Found the phone number: " + mo.group(0) + "in line number " + str(line))
            line+=1
            
    else:
            line+=1
