a = 33
b = 200
if b > a:
  print("b is greater than a")

#Elif and else keyword
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

##Short hand If
if a > b: print("a is greater than b")

##Short hand if else
a = 2
b = 330
print("A") if a > b else print("B")

##and keyword
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

##not keyword 
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

##Nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")