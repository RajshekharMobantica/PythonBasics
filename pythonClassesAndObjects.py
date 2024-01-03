#create class
class MyClass:
  x = 5

#create object
p1 = MyClass()
print(p1.x)


#__init__() function is called automatically every time the class is being used to create a new object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
#print(p1.name)
#print(p1.age)
p1.myfunc()
