#while loop
i = 1
while i < 6:
  print(i)
  i += 1

#break statements
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#Continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#Else in while
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#For loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Break i for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Range function
for x in range(6):
  print(x)

#Range starting from
for x in range(2, 6):
  print(x)

##Else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

##Nested for loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

