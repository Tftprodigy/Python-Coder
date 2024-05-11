# class myClass:
#     x = 5
    
# print(myClass().x)

# p1 = myClass()
# print(p1.x)

###############################


#this code block contain a class containing objects of the 
# person i.e name & age 
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = person("john", 25) #manually inputing the attriubutes

#making it more interactive by asking the user for details
# name = input ("Enter your name: ")
# age = int(input("Enter your age: "))
# p1 = person(name, age)

# Deleting an object property from a class
del p1.age

print(p1.age)