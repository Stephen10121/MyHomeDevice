#This will be a multi purpose controller
import time as T
import os as OS

# The Start
def __init__():
  filesize = OS.path.getsize("name.txt")
  if filesize == 0:
    #Configure Device
    def getname():
      print("This Device is not yet configured")
      print("Lets configure it!!")
      print("Your name has to be less than 16 characters.")
      name = input("What is your name? ")
      namesize = len(name)
      return name , namesize
    name , namesize = getname()
    if namesize > 16:
      print("Too Big")
      getname()
    else:
      putname = open('name.txt' , mode='w')
      putname.write(name)
      print("Success. Hello " + name)
  else:
    #Configured the Device
    getname = open('name.txt' , mode='r')
    name = getname.read()
    getname.close()
    print("Welcome " + name)

__init__()
