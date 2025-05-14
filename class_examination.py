# 1) List and explain 5 built-in functions

# a) The float() function is a function used to convert a certain data type to float type through a process called casting 
#example:
price = 2000
float_converted_price = float(price)
print(float_converted_price)

# b) The input() function takes user input...
#example:
user_input = input("What is your name ?")
#It takes the user input and stores it in the variable "user_input" in this case 

# c) The str() function is a function used to convert a certain data type to string type through a process called casting 
#example:
age= 17
string_converted_age = str(age)
print(string_converted_age)

# d) The strip() function is used to remove any space from the extreme left and right of inputs and outputs
language = "  yoruba  "
strip_language = language.strip()
print(strip_language)

# e) The upper() function is used to convert strings to upper case form
#example:
street = "Olaniyi yusuf street"
print(street.upper())
# 2) Write a python pseudocode of sum of AP formula
#first, by asking for the variables in the formula using input() function
d= int(input("input the value of d in the formula : "))
n= int(input("input the value of n in the formula : "))
a= int(input("input the value of a in the formula : "))
first_step = n-1 #evaluating (n-1)
second_step = d * first_step# Evaluating (n-1)d
third_step = (2 * a) + second_step#Evaluating (2a + (n-1)d)
fourth_step = n/2# Evaluating n/2
fifth_step = fourth_step * third_step#Evaluating n/2[2a+(n-1)d]
print("Answer : "+ str(fifth_step)) # Printing the value of S

# Write a python script asking for the user name and user year of birth and print the users name
user_name = input("Please input your name : ")
print(f"Hello + {user_name} !!!")
user_birth_year = int(input("Input your birth year : "))
user_age = 2024 -user_birth_year
print(f"Hello {user_name} you are {user_age} years old")