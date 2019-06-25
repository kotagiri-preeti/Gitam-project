import re
result = re.search(r'Tutorials', 'TP Tutorials Point TP')
print(result)
result1 = re.match(r'Tutorials', 'TP Tutorials Point TP')
print(result1)
result2 = re.match(r'TP', 'TP Tutorials Point TP')
print(result2)
result2 = re.search(r'TP', 'TP Tutorials Point TP')
print(result2)