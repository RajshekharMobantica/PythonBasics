#Python has a built-in package called re, which can be used to work with Regular Expressions
import re

#Search the string to see if it starts with "The" and ends with "Spain"
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

#find all
x = re.findall("ai", txt)
print(x)