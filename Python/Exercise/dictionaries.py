student = {"name" : "Enock Benz" , "age" : 19 , "Town" : "Olbutyo" }
 
del student ["age"] 
# print(student ["name"]) 
# print(student ["age"])
# print(student ["Town"])

student ["age"] = 20

for key , value in student.items():
    print (f"{key}:{value}")

    