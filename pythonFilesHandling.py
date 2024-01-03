#open a file
f = open("/home/vivek/Raj/PyProjects/PythonBasicsConcepts/src/input_files/sample3.txt", "r")
print(f.read())

#Read one line of file
print(f.readline())

#Read file line by line
for x in f:
  print(x)

#Close file when finish with it
f.close()



##append content to file
f = open("sample3.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("sample3.txt", "r")
print(f.read())


##overwrite the content
f = open("/home/vivek/Raj/PyProjects/PythonBasicsConcepts/src/input_files/sample3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("/home/vivek/Raj/PyProjects/PythonBasicsConcepts/src/input_files/sample3.txt", "r")
print(f.read())


##Delete file
import os
os.remove("/home/vivek/Raj/PyProjects/PythonBasicsConcepts/src/input_files/sample3.txt")

#check if file exixts
if os.path.exists("/home/vivek/Raj/PyProjects/PythonBasicsConcepts/src/input_files/sample3.txt"):
  os.remove("/home/vivek/Raj/PyProjects/PythonBasicsConcepts/src/input_files/sample3.txt")
else:
  print("The file does not exist")

#Delete folder
os.rmdir("myfolder")