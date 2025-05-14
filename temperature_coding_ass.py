#write a python program to convert a given temperature from celsius to fahrenheit. use the formular F= (c*9/5)+32

#convert 32 degree celsius to fahrenheit


user_choice = str(input(f'Choose between celcius and fahrenheit conversion by inputting "celcius" or "fahrenheit" : '))


def celcius():
    celcius = float(input("Enter the celcius value : "))
    fahrenheit= (celcius * 9/5) + 32
    print(f'Your answer is {fahrenheit} degrees fahrenheit')

def fahrenheit():
    fahrenheit = float(input("Enter the fahrenheit value : "))
    celcius = (fahrenheit - 32)*5/9
    print(f'Your answer is {celcius} degrees celcius')

if user_choice.title() == "Celcius":
    celcius()

elif user_choice.title() == "Fahrenheit":
    fahrenheit()



