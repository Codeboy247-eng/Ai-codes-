def perfect_square_root():
    perfect_square = int(input("Enter the number : "))
    num = 0
    while num ** 2 < perfect_square:
       num=1+num
       if num**2 == perfect_square:
            print(f'{num} and -{num} are the squareroot of {perfect_square}')
while True:
    perfect_square_root()
