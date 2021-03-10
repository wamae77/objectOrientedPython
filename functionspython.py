def my_function():
  print("hello world")

my_function()

  print("---------arguments----------")
    def Addition(x, y):
      return x +y
      
 Addition(5, 6)
 
 
 
def Multiplication():
    a = input("please give a number ")
    b= input("please give a second  number ")
    return int(a) * int(b)
    
 Multiplication()
 
 
def Multiplication2(x,y,z):

  return int(x) * int(y)*int(z)

print(Multiplication2(3,5,6))


#if you dont know the number of arguments to be povided use *args
def courses(*args):
  for subject in args:
    print(subject)

courses("Big data","ML","Data science")
print("----------------------")

#key word arguments **kwargs
def courses(**kwargs):
  for key,value in kwargs.items():
    print("{}:{}".format(key,value))

courses(first= "Big data",second= "ML",third = "Data science")
print("----------------------")


#override default arguments
def quotient(x = 50, y= 60):
  print(x/y)

quotient()
print("---------overriding-------------")
quotient(50,2)
print("----------------------")


#passing a list as an argument
def myFunction(mylist):
  for x in mylist:
    print(x)

mylist1 = [2,34,75,75,33,"mwalim",["hello","sir"]]
myFunction(mylist1)


#passing a list or dictionary as an argument
def myFunction(mylist):
  for x in mylist:
    print(x)

mylist1 = [2,34,75,75,33,"mwalim",["hello","sir"]]
mydictionary = {
     "name":"wamae",
     "reg no":"bbit",
     "phone":748188534,
}
print("--------------list----------")
myFunction(mylist1)

print("--------------dictionary----------")
myFunction(mydictionary)

#pass statement
def my_function():
  pass
  
  
  #Area of a circle
import math
def AreaOfACircle():
  radius = int(input("provide a radius: "))
  pi =  math.pi
  answer = pi * radius * radius
  print("your Area is",answer)
AreaOfACircle()

#Volumeofacylinder
print("---------Volume of a cylinder-- = Area(pi*r*r) *Height---------")
def Volumeofacylinder():
   radius = int(input("provide a radius: "))
   height = int(input("provide a height for the cylinder: "))
   pi =  math.pi
   area = pi * radius * radius
   volume = height * area
   print("your Volume of a cylinder is",volume)
Volumeofacylinder()


#Area of a rectangle
print("----------Area of a Rectangle--------------")
def AreaOfARectangle():
     length = input("provide a length: ")
     width = int(input("provide a width: "))
     area = length * width
     print("Area Of A Rectangle: ",area)
AreaOfARectangle()

#volume of sphere
print("-------volume of a sphere = 4/3 * pi * r *r * r")
def volumeofasphere():
  pi =  math.pi
  r = int(input("provide a radius: "))
  a = 4/3
  volume= a * pi * r * r * r
  print("volumeofasphere is: ",volume)
volumeofasphere()
