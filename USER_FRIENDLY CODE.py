#This program asks for a users details and prints them out in a user-friendly manner
def user_details():
    First_name = str(input("Enter your first name :"))
    Last_name = str(input("Enter your last name :"))
    name = First_name + Last_name
    Age = int(input("How old are you ?"))
    output = f"{name} is {Age} years old"
    print(output)
user_details()
    
