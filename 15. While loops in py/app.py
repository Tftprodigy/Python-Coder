# i = 1
# while i < 10:
#     print(i)
#     i += 1


# name = input("Enter your name: ")

# if name == "":
#     print
# else:
#     print(f"Hello {name}")
    
##THIS WILL ASK THE USER TO INPUT THEIR NAME AND END


## WHAT IF THE CODE IS REQUIRED TO KEEP ASKING THE USER
## FOR AN INPUT IF INPUT IS ENPTY?

# name = input("Enter Your Name: ")

# if name == "":
#     print('You did not enter your name')
#     name = input("Enter Your Name: ")
    
# else:
#     print(f"Hello {name}")
    
# # USING THE SAME LOGIC, LETS ASK THE USER FOR THEIR
## AGE WHILE MAKING SURE AGE IS NOT NEGATIVE.

# age = int(input("Enter Your age: "))

# while age < 0:
#     print('Age cannot be Negative')
#     age = int(input("Enter Your age: "))
    
# print(f"you are {age} years old")


#ANOTHER EXAMPLE, ASK THE USER A FOOD THEY LIKE AND ASK THEM
# TILL THEY EXIT THE PROGRAM

# food = input ('Enter a food you like (q to quit): ')
    
# while not food == "q":
#     print(f"you like {food}")
#     food = input ('Enter a another food you like (q to quit: )') 
    
    
# print('you left the playing arena')





# ?another Example
# ASKING USER TO ENETR A NUMBER BETWEEN 1 - 10
# NUMBER GREATER THAN OR LESS THAN ARE INVALID
# ALSO MAKE USE OF 'OR' LOGICAL OPERATOR

num = int(input('Enter a number between 1 - 10: '))

while num < 0 or num > 10:
    print(f"{num} is invalid")
    num = int(input('Enter a number between 1 - 10: '))

print(f"The Number You Entered is {num}")