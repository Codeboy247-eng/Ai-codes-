def user_name():
    first_name = str(input("Enter your firstname : "))
    last_name = str(input("Enter your lastname : "))
    full_name = first_name.title()+" "+last_name.title()
    print(f"Your firstname is {len(first_name.strip())} numbers long !")
    print(f"Your lastname is {len(last_name.strip())} numbers long !")
    print(f'Fullname :- {full_name}')
user_name()
