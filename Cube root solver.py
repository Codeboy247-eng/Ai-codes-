#Finding the root of a perfect cube
x = int(input("Enter an integer : "))
ans = 0 
while ans**3< abs(x):
    ans = ans+1
    if ans**3 != abs(x):
        print(x, "is not a perfect cube")
    elif x<0:
        ans = -ans
        print('The cuberoot of ',x,' is ',ans)