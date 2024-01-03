##Python comments

##Single Line comment
#Python Indentation

##multiline commnents
""" Indentation refers to the spaces at the beginning of a code line.
 Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
 Python uses indentation to indicate a block of code."""

if 5 > 2:
  print("Five is greater than two!")


##Python Variables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


##Python Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x,y,z)

#Get the datatype 
x = 5
y = "John"
print(type(x))
print(type(y))

##Single or Double quote
x = "John"
print(x)
# is the same as
x = 'John'
print(x)


##Python is case sensitive
a = 4
A = "Sally"
#A will not overwrite a
print(a, A)

##Legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

##Illegal variable names
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

##Assign many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

##Assign one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

##Random number generation in python
import random
print(random.randrange(1, 10))

##Get character from string
a = "Hello, World!"
print(a[1])

##Looping on string
for x in "banana":
  print(x)

##Get length of string
a = "Hello, World!"
print(len(a))

##Check if text is available in string
txt = "The best things in life are free!"
print("free" in txt)

##Check if text is not available in string
txt = "The best things in life are free!"
print("expensive" not in txt)

##Get the characters from position 2 to position 5 (not included)
b = "Hello, World!"
print(b[2:5])

##Slice from the start
b = "Hello, World!"
print(b[:5])

##Slice to the end
b = "Hello, World!"
print(b[2:])

##Negative indexing for string slicing
b = "Hello, World!"
print(b[-5:-2])

##Modify strings

##Uppercase
a = "Hello, World!"
print(a.upper())

##Lowercase
a = "Hello, World!"
print(a.lower())

##Remove whitespaces
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

##Replace string
a = "Hello, World!"
print(a.replace("H", "J"))

##splitting of string
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

##String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))