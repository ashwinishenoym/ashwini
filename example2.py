##import re
##
##print(re.findall(r'^\w+', 'guru99,education is fun'))

##import re
##print(re.split(r'\s', 'guru99,education is fun'))
##print(re.split(r'\W', 'guru99,education is fun'))
##print(re.split(r'\,', 'guru99,education is fun'))
##print(re.split(r'^\W', 'guru99,education is fun'))

##import re
##
##list = ["guru get", "guru,give", "guru takes"]
##
##for element in list:
##
##    mo = re.match("(g\w+)\W(g\w+)", element)
##
##    if mo:
##
##        print((mo.groups()))
        
##import re
##
##pattern1 = ["Life is good", "Enjoy each moment"]
##pattern2 = ["Life is good"]
##
##for element in pattern1:
##    mo = re.search(element, pattern2)
##
##    if mo:
##        print("match found")
##    else:
##        print("match not found")

import re

pattern1 = ["Life is good", "Enjoy every day"]
pattern2 = ["Life is good"]

for element in pattern1:
   # mo = re.search(element, pattern2)

    if re.search(element, pattern2):
        print("match found")
    else:
        print("match not found")
