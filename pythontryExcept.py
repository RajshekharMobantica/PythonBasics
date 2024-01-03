#here x is not defined so will throw an error
try:
  print(x)
except:
  print("An exception occurred")


#multiple except blocks
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


#else block with try-except
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


#with finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


#with else and finally
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")

