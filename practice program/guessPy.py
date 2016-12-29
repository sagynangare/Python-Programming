highest=10
answer=7
guess=raw_input("Guess a number from 0 to %d:"%highest)
while(int(guess)!=answer):
    if(int(guess)<answer):
        print("answer is higher")
    else:
        print"Answer is lower"
    guess=raw_input("Guess a number from 0 to %d:"%highest)
raw_input("You are a winner")
