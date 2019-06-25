def string_both_ends(str):
  if len(str) < 2:
    return 'empty string'
  return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))

x=input("enter a name")
a=x[:2]
b=x[-2:]
print(a+b)
if len(x)<2:
    print("empty string")

