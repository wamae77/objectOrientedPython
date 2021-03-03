# DIctionaries
Student={
"Fname":"wamae",
"Lname":"kevin",
"phoneNumber":748188534,
"email":"kelvinwamae77@gmail.com",
}
print(Student)

car = {
"brand":"Tesla",
"Electric":True,
"year":"2020",
"colors":["red","white","black"]
}
print(car)

#accessing items
car = {
"brand":"Ford",
"model":"mustang",
"year":1964
}
print(car["model"])
print(car.get("year"))

#get keys
print(car.keys())
#gey values
print(car.values())

if "model" in car:
  print("yes, the model is"+car["model"])

#change dictionary items

car["year"]=2020
print(car)


#removing items methods
#pop()
#popitem()
#del()
#clear()
car.pop("model")
print(car)

car.popitem()
print(car)



#loop through dictionary
for x in car:
  print(x,end='\n')
print("----------------")
for x in car.values():
  print(x,end='\n')
print("----------------")
for x in car.keys():
  print(x,end='\n')
print("----------------")
for x, y in car.items():
  print(x,y,end='\n')
  
  
  
myFamily ={
"child1":{
"name":"mary",
"age":20

},
"child2":{
"name":"Mark",
"age":15
},
"child3":{
"name":"john",
"age":10
},
}

for x in myFamily:
  print(x)
  
  
  #LIST
myList = ["yes", 6, True, 3.66]
print(myList)

#Add a key 
car["color"]=["red","orange","gray"]
print(car)
