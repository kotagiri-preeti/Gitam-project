import re
line = " cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line)
if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
    print ("matchObj.groups() : ", matchObj.groups())
else:
    print ("No match!!")
