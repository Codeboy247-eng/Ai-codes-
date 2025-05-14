#Exploring the sep and end function today, lets GOOO
'''From what i understand, sep acts as a seperator between strings, while end adds a string to the end of the string syntax'''
#For Example, this is a program that asks for user's name and age(casts it to str) and then uses sep and end to punctuate properly
def user():
    user_name = str(input("Please enter your name : "))
    user_age = eval(input("How old are you ? "))
    print(f"Dear {user_name}","You say you're "+str(user_age) + " years old ", sep =", ", end = "?")
    print("")
    print("YOU'RE WELCOME !!!")
user()
