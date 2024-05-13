print ("Create an Account now")

username = input ("Create a Username: ")
password = input("Create a secure password: ")

print(username, "Successfully created")
print("Login Now!!!")

username2 = input("Enter Your username: ")
password2 = input ("Enetr your password: ")

if (username2 == username and password2 == password):
    print(f"Welcome to {username} Dashboard")
else:
    print("wrong username or password")

