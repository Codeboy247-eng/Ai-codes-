#This program converts from hours to minutes and seconds...
def Conversion():
    def hour_to_minute():
        Hour = eval(input("Enter the value in hours : "))
        #Hour1 = float(input("Enter the value in hours : "))
        if isinstance(Hour, int):
            Minute = Hour*60
            print(f'{Hour} hour(s) to minute = {Minute} minutes')
        elif isinstance(Hour,float):
            Minute = (int(Hour)*60)+(Hour-int(Hour))
            print(f'{Hour} Hour(s) to minute is {Minute} minutes')
    
    def minute_to_seconds():
        minutes = eval(input("Enter the value in minutes : "))
        if isinstance(minutes, int):
            seconds = minutes*60
            print(f'{minutes} minute(s) to seconds = {seconds} seconds')
        elif isinstance(minutes, float):
            seconds = (int(minutes)*60)+(minutes-int(minutes))
            print(f'{minutes} minute(s) to seconds is {seconds}')

    def hours_to_seconds():
        Hour1 = eval(input("Enter the value in hours : "))
        #Hour1 = float(input("Enter the value in hours : "))
        if isinstance(Hour1, int):
            seconds = Hour1*3600
            print(f'{Hour1} hour(s) to seconds = {seconds}')
        elif isinstance(Hour1, float):
            seconds = (int(Hour1)*3600)+(Hour1-int(Hour1))
            print(f'{Hour1} Hour(s) to seconds is {seconds}')
    
    user_conversion = str(input("Input '1' to convert from Hour to minute and vice-versa, '2' for Minutes to seconds, '3' for Hour to seconds : "))
    if user_conversion == '1':
        hour_to_minute()
    elif user_conversion == '2':
        minute_to_seconds()
    elif user_conversion == '3':
        hours_to_seconds()
#while True:
Conversion()
