##Create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)

##Duplicates not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

##Same for False and 0
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

##Set can contain different datatypes
set1 = {"abc", 34, True, 40, "male"}
print(set1)

##Add items to set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

##Add set into set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


##Remove item from set
#using remove mothod
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#using discard ethod
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

##to clear the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

##delete the set
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

##looping through set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

##Join sets

#Join 2 sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#Using update method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Keep the items that exists in both set (duplicate items)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#Keep all but not duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

