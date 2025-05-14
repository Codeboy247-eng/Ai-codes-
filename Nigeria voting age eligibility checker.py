#This program checks if you're eligible to vote
def users_eligibility():
    Age = int(input("Input your age : "))
    if Age>=18:
        print("You're eligible!")
    elif Age<18:
        print("You're not eligible!")
    else:
        print("Invalid input")
users_eligibility()