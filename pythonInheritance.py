#Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Child class (inherits features and properties of Person class)
class Student(Person):
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

#from child class access parent class features
x = Student("Mike", "Olsen")
x.printname()

