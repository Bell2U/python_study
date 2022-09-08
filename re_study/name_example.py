from re import compile

pattern = compile("[a-zA-Z ]+$")
while True:
    Name = input("Please enter your name: ")
    if pattern.match(Name):
        break
    else:
        print("Error")
        print()