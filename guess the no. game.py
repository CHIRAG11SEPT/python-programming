from random import *

computer_num= randrange(1,101)
score=10
while True:
    user_num = int(input("guess the no. between 1 to 100 : "))
    if user_num==computer_num:
        print("you win with score:",score)
    elif user_num> computer_num:
        print("too large")
    else:
        print("too small")
    score -= 1