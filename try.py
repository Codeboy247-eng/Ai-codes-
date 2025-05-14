'''I can't say how happy i am to build this program, at my current level, it took me hours to figure out the algorithmic path to take so 
i am deeply happy and i feel fufilled LETSS GOOOO!!!!, we winning apex mode way'''

def factorial_finder_program():
    n_input = int(input("Enter the number : "))
    n = n_input
    if n_input > 1:
        while n>1 and n_input>1:
            while n_input>1:
                n*=n_input-1
                n_input-=1 
                if n_input - 1<=0:
                    print(f'Factorial : {n}')
factorial_finder_program()
while True:
    factorial_finder_program()
#Created by Damilola Bamidele...
