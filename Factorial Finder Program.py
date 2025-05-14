# I can't say how happy i am to build this program, at my current level, it took me hours to figure out the algorithmic path to take so

def factorial_finder_program():
    n_input = int(input("Enter the number : "))
    n = n_input
    if n_input > 1:
        while n>1 and n_input>1:
            while n_input>1:
                n*=n_input-1
                n_input-=1 
                if n_input - 1<=0:
                    print(f'{n_input}! : {n}')
while True:
    factorial_finder_program()
# Created by Damilola Bamidele...
