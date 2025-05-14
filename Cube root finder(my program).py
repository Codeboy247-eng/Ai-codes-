#This program finds the root of perfect cube numbers
def calculations():
    num = int(input("Enter the number : "))
    cube_root = num**(1/3)
    if isinstance(cube_root,int):
        print('Cube root : ',cube_root)
    elif isinstance(cube_root,float):
        print(f"{num} is not a perfect cube, but it's approximated cube is {round(cube_root,2)}.")
    else:
        print("Invalid input.")
        exit()
calculations()