import re
string = "Python is a case sensitive language"

print("Length of string = ", len(string))
print("String in Reverse:", string[::-1])
New_string= string[10:26]
print("New String = ", New_string)
print(string.replace("a case sensitive", "object oriented"))
print("Index of 'a': ",[match.start() for match in re.finditer("a", string)])
print(string.replace(" ", ""))