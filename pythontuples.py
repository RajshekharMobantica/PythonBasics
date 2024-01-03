##Creating the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

##Tuples allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

##Create tuple with one item
#This is tuple remember a comma
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#tuples can contain different types of datatypes
thistuple = ("abc", 34, True, 40, "male")
print(thistuple)

##Access tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

##negative indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])  #will print last item

##Since tuples are unchangeble here how to update the tuple below

#change Tuple values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Add item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#Remove item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


