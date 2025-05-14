import time
import sys

# Helper function for printing text with a delay
def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

type_text('''
A vacation is when you take a trip to some __________________ place 
with your __________________ family. Usually you go to some place 
that is near a/an __________________ or up on a/an __________________.
A good vacation place is one where you can ride __________________
or play __________________ or go hunting for __________________ . I like 
to spend my time ________________________ or ________________________.
When parents go on a vacation, they spend their time eating 
three __________________ a day, and fathers play golf, and mothers 
sit around ________________________. Last summer, my little brother 
fell in a/an __________________ and got poison __________________ all 
over his________________________. My family is going to go to (the) 
__________________, and I will practice ________________________. Parents 
need vacations more than kids because parents are always very 
__________________ and because they have to work__________________
hours every day all year making enough __________________ to pay 
for the vacation''')