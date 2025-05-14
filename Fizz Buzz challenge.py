def fizz_buzz():
    x = 0
    while x <= 100:
        if x%3 == 0:
            print("Fizz")
        elif x%2 == 0:
            print("Buzz")
        else:
            print(x)
        x+=1
fizz_buzz()
