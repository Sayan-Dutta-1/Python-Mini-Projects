import random
num = random.randint(1,100) 
level = input("Do you want to play on the hard level or easy level: H/E\n").lower()
if level == "h":
    count = 5
elif level == "e":
    count = 10
for i in range (count):
    print(f"You have {count-i} guess remaining")
    choice = int(input("Chose a number between 1 and 100: "))  
    if num > choice:
        print('You are too low')
    elif num < choice:
        print ('you are to high')
    else:
        print (f"Congrats! You won! The answer was {num}")
        exit()
else :
    print(f"You failed! The answer was {num}\nBetter luck next time.")