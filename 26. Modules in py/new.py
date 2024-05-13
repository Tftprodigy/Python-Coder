def sayHi():
    print("Hello and Hi")

class user():
    name = input("Enter username: ")
    password = input("Enter password: ")
    age = int(input("Enter your Age: "))

print(f"Hello {user.name} you are {user.age} years old")