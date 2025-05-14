def approximation():
    User_choice = str(input("Enter 'N' if you want to round to nearest digit but 'P' to round to a particular decimal place : "))
    if User_choice.lower() == 'n':
        number1 = eval(input("Enter the digit : ")) 
        result1 = round(number1)
        print(f'{number1} to the closest integer = {result1} !')
    elif User_choice.lower() == 'p':
        number = eval(input("Enter the digit : ")) 
        decimal_places = int(input("What decimal place do you want it to be approximated to ? "))
        result = round(number, decimal_places)
        print(f'{number} to {decimal_places} Decimal places = {result} !')
while True:
    approximation()