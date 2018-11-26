correct_password = "python123"
name = input("Enter name: ")
surname = input("Enter surname: ")
password = input("Enter password: ")

while correct_password != password:
    password = input("Invalid password! Enter again: ")

message = "Hi %s %s, you are loggged in." % (name, surname)
print(message)