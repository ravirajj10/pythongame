import random


def snakewatergungame():
    n = 1
    userwoncount = 0
    compwoncount = 0
    while(n<4):
        print(f"Attempt:{n}")
        choicelist = ["Snake", "Water", "Gun"]
        print("Choose any between: ", choicelist)
        userchoice = input("Enter choice ")
        compchoice = random.choice(choicelist)
        if userchoice == "Snake" and compchoice == "Water":
            print(f"User:{userchoice} and Computer:{compchoice}")
            compwoncount += 1
            print("Computer wins")
        elif userchoice == "Water" and compchoice == "Snake":
            print(f"User:{userchoice} and Computer:{compchoice}")
            userwoncount += 1
            print("You won")
        elif userchoice == "Gun" and compchoice == "Water":
            print(f"User:{userchoice} and Computer:{compchoice}")
            print("Computer wins")
            compwoncount += 1
        elif userchoice == "Water" and compchoice == "Gun":
            print(f"User:{userchoice} and Computer:{compchoice}")
            print("You won")
            userwoncount += 1
        elif userchoice == "Snake" and compchoice == "Gun":
            print(f"User:{userchoice} and Computer:{compchoice}")
            print("Computer wins")
            compwoncount += 1
        elif userchoice == "Gun" and compchoice == "Snake":
            print(f"User:{userchoice} and Computer:{compchoice}")
            print("You won")
            userwoncount += 1
        print(f"User winning streak:{userwoncount} and Computer winning streak:{compwoncount}")
        n += 1
    if userwoncount > compwoncount:
        print("You have won the game !")
    else:
        print("Computer have won the game !")


snakewatergungame()