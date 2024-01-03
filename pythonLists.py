##Create the List
thislist = ["apple", "banana", "cherry"]
print(thislist)

##Python lists allow duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

##List can contain different datatypes
list1 = ["abc", 34, True, 40, "male"]

##List constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

##Access items from list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

##Negative indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

##Below will return third, fourth and fifth items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

##check if item exist in list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

##Change list item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

##Change a range of items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

##insert item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

##Append/Add item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

##extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

##Add tuple to list
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

##Remove specific item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

##remove by index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

##Remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

##remove first item
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

##delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist

##Clear the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

##Loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

##Loop through the index 
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

##Using while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

##Sort the list alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

##Sort descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

##Customized sorting
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

##Reverse the order of list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

##Make a copy of list 
#Using copy method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#using list constructor
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

