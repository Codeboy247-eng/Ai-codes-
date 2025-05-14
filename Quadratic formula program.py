#This solves quadratic equations using the formula method
import math
def quadratic_formula_syntax():
    print("Enter the coeffiecients of the powers of x...")
    a = eval(input("Enter the value of a : "))
    b = eval(input("Enter the value of b : "))
    c = eval(input("Enter the value of c : "))
    determinant = math.sqrt((b**2) - (4*a*c))
    numerator1 = -b + determinant
    numerator2 = -b - determinant
    result1 = numerator1/(2*a)
    result2 = numerator2/(2*a)
    print(f'The solutions to the quadratic equation are : \n {result1} or {result2}')
while True:
    quadratic_formula_syntax()
#I timed myself 15 minutes but i was able to finish it in 7 minutes huge progress from then 😁