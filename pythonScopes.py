##Local Scope
def myfunc():
  x = 300
  print(x)

myfunc()

#Function inside function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


##Global Scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)


#Global in local scope/chage value of global
x = 200
def myfunc():
  global x
  x = 400

myfunc()

print(x)